// Quiz-engine: rendert MC-, open- en inzichtvragen en geeft feedback.
const Quiz = (() => {

  const shuffle = (arr) => {
    const a = arr.slice();
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
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

  const renderQuestionHeader = (q, idxInfo) => {
    const chips = [];
    chips.push(`<span class="chip">${q.type === "mc" ? "Meerkeuze" : q.type === "open" ? "Open" : "Inzicht"}</span>`);
    if (q.moeilijkheid) {
      const cls = q.moeilijkheid === "lastig" ? "bad" : q.moeilijkheid === "gemiddeld" ? "warn" : "brand";
      chips.push(`<span class="chip ${cls}">${q.moeilijkheid}</span>`);
    }
    return `<div class="row between" style="margin-bottom:8px">
      <div class="chips">${chips.join("")}</div>
      ${idxInfo ? `<span class="muted">${idxInfo}</span>` : ""}
    </div>`;
  };

  // Rendert één vraag in `host`. Roept `onAnswered(correct: boolean)` aan zodra
  // de leerling de vraag heeft afgesloten (na zelfbeoordeling bij open vragen).
  const render = (host, q, { idxInfo, onAnswered } = {}) => {
    host.innerHTML = "";
    const card = document.createElement("div");
    card.className = "card";
    card.innerHTML = renderQuestionHeader(q, idxInfo) +
      `<h3 style="margin-top:4px">${escapeHtml(q.vraag)}</h3>`;
    host.appendChild(card);

    if (q.type === "mc") {
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
    } else {
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
        // mini-hint
        if (pct === 100) {
          const ok = document.createElement("p");
          ok.className = "muted";
          ok.style.margin = "8px 0 0";
          ok.textContent = "Tip: alle kernwoorden zaten erin — dat is een goed teken.";
          card.appendChild(ok);
        }
      };
    }
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

  return { render, shuffle, escapeHtml, matchKernwoorden };
})();
