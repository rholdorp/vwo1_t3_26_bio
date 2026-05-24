// Quiz-engine: rendert MC-, open-, inzicht-, aanwijs- en begrip-vragen en geeft feedback.
const Quiz = (() => {

  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  };

  // -------- SVG loader (gedeeld met Aanwijzen-modus) -----------------------
  const SVG_VERSION = "6";
  const _svgCache = {};
  const loadSvg = (path) => {
    if (!_svgCache[path]) {
      _svgCache[path] = fetch(`${path}?v=${SVG_VERSION}`, { cache: "no-cache" })
        .then(r => { if (!r.ok) throw new Error(`Kon ${path} niet laden (${r.status})`); return r.text(); });
    }
    return _svgCache[path];
  };

  const normalize = (s) =>
    (s || "").toLowerCase()
      .normalize("NFD").replace(/[\u0300-\u036f]/g, "")
      .replace(/[^\p{L}\p{N}\s]/gu, " ")
      .replace(/\s+/g, " ").trim();

  const matchKernwoorden = (answer, kernwoorden) => {
    const norm = normalize(answer);
    return (kernwoorden || []).map(k => ({
      word: k,
      found: norm.includes(normalize(k))
    }));
  };

  const typeLabel = (q) => {
    if (q.type === "aanwijs") return "Aanwijzen";
    if (q.type === "begrip")  return "Begrip";
    if (q.type === "mc")      return "Meerkeuze";
    if (q.type === "open")    return "Open";
    return "Inzicht";
  };

  const renderQuestionHeader = (q, idxInfo) => {
    const chips = [];
    chips.push(`<span class="chip">${typeLabel(q)}</span>`);
    if (q.moeilijkheid) {
      const cls = q.moeilijkheid === "lastig" ? "bad" : q.moeilijkheid === "gemiddeld" ? "warn" : "brand";
      chips.push(`<span class="chip ${cls}">${q.moeilijkheid}</span>`);
    }
    return `<div class="row between" style="margin-bottom:8px">
      <div class="chips">${chips.join("")}</div>
      ${idxInfo ? `<span class="muted">${idxInfo}</span>` : ""}
    </div>`;
  };

  const renderImage = (afb, bron) => {
    if (!afb) return "";
    const cap = bron ? `<div class="img-cap">${escapeHtml(bron)}</div>` : "";
    return `<figure class="qimg"><a href="${escapeHtml(afb)}" target="_blank" rel="noopener">
      <img loading="lazy" src="${escapeHtml(afb)}" alt="" /></a>${cap}</figure>`;
  };

  // Interactieve aanwijs-renderer — gedeeld door de Aanwijzen-modus en Quiz.
  // onDone(grade) wordt aangeroepen met grade 0/1/2.
  const renderAanwijsInteractive = async (card, a, onDone) => {
    const wrapId = "anat-wrap-" + Math.random().toString(36).slice(2);
    const fbId = "anat-fb-" + Math.random().toString(36).slice(2);
    const actId = "anat-act-" + Math.random().toString(36).slice(2);
    const hintHtml = a.hint ? `<p class="muted" style="margin:0 0 8px">💡 ${escapeHtml(a.hint)}</p>` : "";
    card.insertAdjacentHTML("beforeend", `
      ${hintHtml}
      <div class="anat-wrap" id="${wrapId}">Laden…</div>
      <div id="${fbId}" class="muted" style="margin-top:8px"></div>
      <div id="${actId}" class="row" style="margin-top:10px; justify-content:center"></div>
    `);
    const wrap = card.querySelector("#" + wrapId);
    const fb = card.querySelector("#" + fbId);
    const actions = card.querySelector("#" + actId);

    let svgText;
    try { svgText = await loadSvg(a.svg); }
    catch (e) { wrap.textContent = "Fout bij laden afbeelding."; onDone && onDone(0); return; }
    wrap.innerHTML = svgText;
    const svg = wrap.querySelector("svg");
    svg.classList.add("anat-svg");

    let attempts = 0;
    let done = false;

    const finish = (grade) => {
      actions.innerHTML = "";
      const btn = document.createElement("button");
      btn.className = "primary";
      btn.textContent = "Volgende →";
      btn.onclick = () => onDone && onDone(grade);
      actions.appendChild(btn);
    };

    svg.addEventListener("click", (e) => {
      if (done) return;
      const r = e.target.closest(".region");
      if (!r) return;
      attempts++;
      const clicked = r.dataset.region;
      if (clicked === a.region) {
        done = true;
        r.classList.add("correct");
        fb.innerHTML = `✅ <b>Goed!</b> Dit is de <b>${escapeHtml(a.naam.toLowerCase())}</b>.` +
          (attempts > 1 ? ` <span class="muted">(${attempts} pogingen)</span>` : "");
        finish(attempts === 1 ? 2 : 1);
      } else if (attempts < 2) {
        r.classList.add("wrong");
        fb.innerHTML = `❌ Nog een keer proberen. Dat was niet de <b>${escapeHtml(a.naam.toLowerCase())}</b>.`;
        setTimeout(() => r.classList.remove("wrong"), 900);
      } else {
        done = true;
        r.classList.add("wrong");
        const target = svg.querySelector(`.region[data-region="${a.region}"]`);
        if (target) target.classList.add("hint");
        fb.innerHTML = `❌ Het juiste antwoord (blauw) is de <b>${escapeHtml(a.naam.toLowerCase())}</b>.`;
        finish(0);
      }
    });

    const giveUp = document.createElement("button");
    giveUp.className = "ghost";
    giveUp.textContent = "Toon antwoord";
    giveUp.onclick = () => {
      if (done) return;
      done = true;
      const target = svg.querySelector(`.region[data-region="${a.region}"]`);
      if (target) target.classList.add("hint");
      fb.innerHTML = `Het juiste antwoord (blauw) is de <b>${escapeHtml(a.naam.toLowerCase())}</b>.`;
      finish(0);
    };
    actions.appendChild(giveUp);
  };

  // Rendert één vraag in `host`. Roept `onAnswered(correct: boolean)` aan zodra
  // de leerling de vraag heeft afgesloten (na zelfbeoordeling bij open vragen).
  const render = (host, q, { idxInfo, onAnswered } = {}) => {
    host.innerHTML = "";
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = renderQuestionHeader(q, idxInfo) +
      renderImage(q.afbeelding, q.bron) +
      `<h3 style="margin-top:4px">${escapeHtml(q.vraag)}</h3>`;
    host.appendChild(card);

    if (q.type === "aanwijs") {
      renderAanwijsInteractive(card, q.aanwijs, (grade) => {
        onAnswered && onAnswered(grade >= 1);
      });
      return;
    }

    if (q.type === "mc" || q.type === "begrip") {
      const opts = q.opties.map((opt, i) => ({ text: opt, originalIndex: i }));
      const shuffled = shuffle(opts);
      const wrap = document.createElement("div");
      card.appendChild(wrap);

      let answered = false;
      shuffled.forEach((opt) => {
        const btn = document.createElement("button");
        btn.className = "option";
        btn.textContent = opt.text;
        btn.onclick = () => {
          if (answered) return;
          answered = true;
          const correct = opt.originalIndex === q.antwoord_index;
          [...wrap.children].forEach((b, i) => {
            b.disabled = true;
            if (shuffled[i].originalIndex === q.antwoord_index) b.classList.add("correct");
            else if (b === btn) b.classList.add("wrong");
          });
          const fb = document.createElement("div");
          fb.className = "feedback " + (correct ? "good" : "bad");
          fb.innerHTML = (correct ? "✅ Goed!" : "❌ Niet helemaal.") +
            (q.uitleg ? `<br/><span class="muted">Uitleg:</span> ${escapeHtml(q.uitleg)}` : "");
          card.appendChild(fb);
          appendNext(card, () => onAnswered && onAnswered(correct));
        };
        wrap.appendChild(btn);
      });
      return;
    }

    // open / inzicht
    const ta = document.createElement("textarea");
    ta.placeholder = "Typ hier je antwoord…";
    card.appendChild(ta);
    const actions = document.createElement("div");
    actions.className = "row";
    actions.style.marginTop = "10px";
    const checkBtn = document.createElement("button");
    checkBtn.className = "primary";
    checkBtn.textContent = "Controleer mijn antwoord";
    actions.appendChild(checkBtn);
    card.appendChild(actions);

    checkBtn.onclick = () => {
      ta.disabled = true;
      checkBtn.disabled = true;

      const matches = matchKernwoorden(ta.value, q.kernwoorden);
      const hitCount = matches.filter(m => m.found).length;
      const totalKW = matches.length || 1;
      const pct = Math.round((hitCount / totalKW) * 100);

      const fb = document.createElement("div");
      fb.className = "feedback info";
      const chipsHtml = matches.length
        ? `<div style="margin:6px 0"><span class="muted">Kernwoorden gevonden (${hitCount}/${matches.length}):</span> ` +
            matches.map(m => `<span class="kernwoord ${m.found ? 'found' : ''}">${escapeHtml(m.word)}</span>`).join(" ") +
          "</div>"
        : "";
      fb.innerHTML =
        chipsHtml +
        `<div><span class="muted">Modelantwoord:</span><br/>${escapeHtml(q.antwoord)}</div>` +
        `<hr/><div><b>Vergelijk je antwoord met het modelantwoord en beoordeel zelf:</b></div>`;
      card.appendChild(fb);

      const grade = document.createElement("div");
      grade.className = "row";
      grade.style.marginTop = "10px";
      const mk = (label, klass, correct) => {
        const b = document.createElement("button");
        b.className = klass;
        b.textContent = label;
        b.onclick = () => {
          grade.querySelectorAll("button").forEach(x => x.disabled = true);
          const tag = document.createElement("span");
          tag.className = "chip " + (correct ? "brand" : "bad");
          tag.style.marginLeft = "8px";
          tag.textContent = correct ? "Beoordeeld: goed" : "Beoordeeld: nog leren";
          grade.appendChild(tag);
          appendNext(card, () => onAnswered && onAnswered(correct));
        };
        return b;
      };
      grade.appendChild(mk("Goed gedaan", "primary", true));
      grade.appendChild(mk("Half goed",   "ghost", false));
      grade.appendChild(mk("Fout",        "ghost", false));
      card.appendChild(grade);
      if (pct === 100) {
        const ok = document.createElement("p");
        ok.className = "muted";
        ok.style.margin = "8px 0 0";
        ok.textContent = "Tip: alle kernwoorden zaten erin — dat is een goed teken.";
        card.appendChild(ok);
      }
    };
  };

  const appendNext = (card, cb) => {
    const r = document.createElement("div");
    r.className = "row";
    r.style.marginTop = "12px";
    const b = document.createElement("button");
    b.className = "secondary";
    b.textContent = "Volgende →";
    b.onclick = () => cb && cb();
    r.appendChild(b);
    card.appendChild(r);
  };

  const escapeHtml = (s) =>
    String(s).replace(/[&<>"']/g, (c) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[c]));

  return { render, renderImage, shuffle, escapeHtml, matchKernwoorden,
           renderAanwijsInteractive, loadSvg };
})();
