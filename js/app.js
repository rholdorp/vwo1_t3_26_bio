// Hoofd-app: routing + alle modi (home, leren, begrippen, oefenen, verbanden, toets).
(() => {
  const view = document.getElementById("view");
  const modesEl = document.getElementById("modes");
  const subtitle = document.getElementById("subtitle");
  const errorEl = document.getElementById("error");
  const resetBtn = document.getElementById("resetBtn");
  const esc = Quiz.escapeHtml;

  let content = null;

  const showError = (msg) => {
    errorEl.textContent = msg;
    errorEl.classList.remove("hidden");
  };

  const setActive = (mode) => {
    modesEl.querySelectorAll("button").forEach(b => {
      b.classList.toggle("active", b.dataset.mode === mode);
    });
  };

  const go = async (mode) => {
    setActive(mode);
    view.innerHTML = "";
    try {
      if (!content) content = await Data.load();
      switch (mode) {
        case "home":      return renderHome();
        case "leren":     return renderLeren();
        case "begrippen": return renderBegrippen();
        case "oefenen":   return renderOefenen();
        case "verbanden": return renderVerbanden();
        case "toets":     return renderToetsConfig();
        case "boek":      return renderBoek();
      }
    } catch (e) {
      showError(e.message || String(e));
      throw e;
    }
  };

  modesEl.addEventListener("click", (e) => {
    if (e.target.tagName === "BUTTON" && e.target.dataset.mode) go(e.target.dataset.mode);
  });

  resetBtn.addEventListener("click", () => {
    if (confirm("Weet je zeker dat je alle voortgang wilt wissen?")) {
      Storage.clearAll();
      go("home");
    }
  });

  // ---------- HOME ----------
  const renderHome = () => {
    subtitle.textContent = `${content.vak} · ${content.niveau} · ${content.proefwerk}`;

    const allLearnIds = [
      ...content.begrippen.map(b => "b:" + b.id),
      ...content.feiten.map(f => "f:" + f.id),
    ];
    const s = SRS.stats(allLearnIds);

    view.innerHTML = `
      <div class="card">
        <h2>Hoi! Klaar om te leren voor je proefwerk?</h2>
        <p>Je hebt <b>${content.begrippen.length}</b> begrippen, <b>${content.feiten.length}</b> feiten,
        <b>${content.verbanden.length}</b> kruisverbanden en <b>${content.vragen.length}</b> oefenvragen.</p>
        <div class="stats">
          <span><b>${s.learned}</b> geleerd</span>
          <span><b>${s.dueNow}</b> nu te herhalen</span>
          <span><b>${s.neverSeen}</b> nog nooit gezien</span>
        </div>
        <div class="progress" style="margin-top:10px"><span style="width:${
          s.total ? Math.round((s.learned / s.total) * 100) : 0
        }%"></span></div>
      </div>

      <div class="grid">
        <div class="tile" data-go="leren">
          <h3>🃏 Leren (flashcards)</h3>
          <p>Begrippen + feiten met slim herhaalsysteem (SR). Begin hier.</p>
        </div>
        <div class="tile" data-go="begrippen">
          <h3>📖 Begrippenlijst</h3>
          <p>Overzicht per hoofdstuk om snel iets op te zoeken.</p>
        </div>
        <div class="tile" data-go="oefenen">
          <h3>📝 Oefenvragen</h3>
          <p>MC + open vragen per hoofdstuk, met feedback.</p>
        </div>
        <div class="tile" data-go="verbanden">
          <h3>🔗 Kruisverbanden</h3>
          <p>Snap je hoe begrippen en hoofdstukken samenhangen?</p>
        </div>
        <div class="tile" data-go="toets">
          <h3>🎯 Proeftoets</h3>
          <p>Realistische test op tijd. Eindscore + alles nakijken.</p>
        </div>
        <div class="tile" data-go="boek">
          <h3>📷 Boekpagina's</h3>
          <p>Door alle foto's van het boek bladeren. Handig bij het opzoeken.</p>
        </div>
      </div>

      <div class="card" style="margin-top:18px">
        <h3>3-daagse aanpak</h3>
        <ol>
          <li><b>Dag 1:</b> Begrippen + feiten leren via flashcards (twee rondes).</li>
          <li><b>Dag 2:</b> Oefenvragen per hoofdstuk + kruisverbanden doornemen.</li>
          <li><b>Dag 3:</b> Eén of twee Proeftoetsen, en de gemiste vragen apart herhalen.</li>
        </ol>
      </div>
    `;
    view.querySelectorAll(".tile").forEach(t => t.onclick = () => go(t.dataset.go));
  };

  // ---------- LEREN (flashcards) ----------
  const renderLeren = () => {
    subtitle.textContent = "Leren — flashcards met spaced repetition";

    const items = [
      ...content.begrippen.map(b => ({
        id: "b:" + b.id, hoofdstuk: b.hoofdstuk, front: b.term, back: b.definitie, kind: "Begrip",
        afbeelding: b.afbeelding, bron: b.bron,
      })),
      ...content.feiten.map(f => ({
        id: "f:" + f.id, hoofdstuk: f.hoofdstuk, front: "Feit (" + Data.chapterTitle(content, f.hoofdstuk) + ")",
        back: f.feit, kind: "Feit", afbeelding: f.afbeelding,
      })),
    ];
    const byId = Object.fromEntries(items.map(i => [i.id, i]));
    const order = SRS.dueItems(items.map(i => i.id));

    if (order.length === 0) {
      view.innerHTML = `<div class="card"><h2>🎉 Niets te herhalen!</h2>
        <p>Alle items zijn gezien en nog niet aan herhaling toe. Probeer <b>Oefenen</b> of <b>Proeftoets</b>.</p></div>`;
      return;
    }

    let i = 0;
    const renderCard = () => {
      if (i >= order.length) {
        view.innerHTML = `<div class="card"><h2>✅ Sessie klaar</h2>
          <p>Je hebt ${order.length} kaarten herhaald. Goed bezig!</p>
          <button class="primary" id="again">Nieuwe sessie</button>
          <button class="ghost"   id="home">Terug naar start</button></div>`;
        document.getElementById("again").onclick = () => renderLeren();
        document.getElementById("home").onclick  = () => go("home");
        return;
      }
      const it = byId[order[i]];
      view.innerHTML = `
        <div class="row between" style="margin-bottom:10px">
          <span class="chip">${it.kind} · ${esc(Data.chapterTitle(content, it.hoofdstuk))}</span>
          <span class="muted">${i + 1} / ${order.length}</span>
        </div>
        <div class="flash" id="flash">
          <div>
            <div id="face">${esc(it.front)}</div>
            <div class="hint">Klik om antwoord te zien</div>
          </div>
        </div>
        <div id="actions" class="row" style="margin-top:14px; justify-content:center"></div>
      `;
      let flipped = false;
      document.getElementById("flash").onclick = () => {
        if (flipped) return;
        flipped = true;
        const imgHtml = it.afbeelding
          ? `<figure class="qimg flash-img"><a href="${esc(it.afbeelding)}" target="_blank" rel="noopener">
               <img loading="lazy" src="${esc(it.afbeelding)}" alt="" /></a>
               ${it.bron ? `<div class="img-cap">${esc(it.bron)}</div>` : ""}</figure>`
          : "";
        document.getElementById("face").innerHTML = imgHtml + `<div>${esc(it.back)}</div>`;
        const a = document.getElementById("actions");
        a.innerHTML = "";
        const buttons = [
          { label: "❌ Fout",    grade: 0, klass: "ghost" },
          { label: "😬 Lastig",  grade: 1, klass: "ghost" },
          { label: "🙂 Goed",    grade: 2, klass: "primary" },
          { label: "😎 Makkelijk", grade: 3, klass: "secondary" },
        ];
        buttons.forEach(b => {
          const btn = document.createElement("button");
          btn.className = b.klass;
          btn.textContent = b.label;
          btn.onclick = () => { SRS.review(it.id, b.grade); i++; renderCard(); };
          a.appendChild(btn);
        });
      };
    };
    renderCard();
  };

  // ---------- BEGRIPPEN ----------
  const renderBegrippen = () => {
    subtitle.textContent = "Begrippen — overzicht per hoofdstuk";
    const byChap = {};
    for (const b of content.begrippen) (byChap[b.hoofdstuk] ||= []).push(b);

    let html = `<div class="card"><h2>Begrippenlijst</h2>
      <p class="muted">Snel opzoeken. Voor leren met spaced repetition: ga naar <b>Leren</b>.</p></div>`;
    for (const h of content.hoofdstukken) {
      const list = byChap[h.id] || [];
      if (!list.length) continue;
      html += `<div class="card"><h3>${esc(h.titel)} <span class="muted">(${list.length})</span></h3>
        <ul class="def-list">${list.map(b => `
          <li>
            ${b.afbeelding ? `<a class="thumb" href="${esc(b.afbeelding)}" target="_blank" rel="noopener">
              <img loading="lazy" src="${esc(b.afbeelding)}" alt="" /></a>` : ""}
            <span class="term">${esc(b.term)}</span>
            <span class="meta">${(b.tags || []).map(t => `#${esc(t)}`).join(" ")}</span>
            <div>${esc(b.definitie)}</div>
          </li>`).join("")}</ul></div>`;
    }
    view.innerHTML = html;
  };

  // ---------- OEFENEN ----------
  const renderOefenen = () => {
    subtitle.textContent = "Oefenvragen — kies hoofdstuk en type";

    const chapterOptions = [
      `<option value="*">Alle hoofdstukken</option>`,
      ...content.hoofdstukken.map(h => `<option value="${h.id}">${esc(h.titel)}</option>`)
    ].join("");

    view.innerHTML = `
      <div class="card">
        <h2>Oefenen</h2>
        <div class="row">
          <label>Hoofdstuk:
            <select id="chap">${chapterOptions}</select>
          </label>
          <label>Type:
            <select id="type">
              <option value="*">Alles</option>
              <option value="mc">Meerkeuze</option>
              <option value="open">Open</option>
              <option value="inzicht">Inzicht</option>
            </select>
          </label>
          <label>Moeilijkheid:
            <select id="diff">
              <option value="*">Alle</option>
              <option value="makkelijk">Makkelijk</option>
              <option value="gemiddeld">Gemiddeld</option>
              <option value="lastig">Lastig</option>
            </select>
          </label>
          <button class="primary" id="start">Start oefenen</button>
        </div>
      </div>
      <div id="quizHost"></div>
    `;

    document.getElementById("start").onclick = () => {
      const ch = document.getElementById("chap").value;
      const tp = document.getElementById("type").value;
      const df = document.getElementById("diff").value;
      const pool = content.vragen.filter(q =>
        (ch === "*" || q.hoofdstuk === ch) &&
        (tp === "*" || q.type === tp) &&
        (df === "*" || q.moeilijkheid === df)
      );
      if (!pool.length) { document.getElementById("quizHost").innerHTML =
        `<div class="card"><p>Geen vragen die hieraan voldoen.</p></div>`; return; }
      runQuiz(Quiz.shuffle(pool), document.getElementById("quizHost"), { mode: "oefenen" });
    };
  };

  const runQuiz = (questions, host, { mode }) => {
    let i = 0, correct = 0;
    const review = [];
    const next = () => {
      if (i >= questions.length) {
        const pct = Math.round((correct / questions.length) * 100);
        host.innerHTML = `<div class="card">
          <h2>Resultaat</h2>
          <p><b>${correct}</b> van <b>${questions.length}</b> goed (${pct}%).</p>
          <div class="progress"><span style="width:${pct}%"></span></div>
          <hr/>
          <h3>Overzicht</h3>
          <ul class="def-list">${review.map(r => `
            <li><span class="chip ${r.correct ? 'brand' : 'bad'}">${r.correct ? 'goed' : 'fout'}</span>
              <span class="meta">${esc(Data.chapterTitle(content, r.q.hoofdstuk))} · ${r.q.type}</span>
              <div>${esc(r.q.vraag)}</div></li>`).join("")}</ul>
          <div class="row" style="margin-top:12px">
            <button class="primary" id="again">Nog een ronde</button>
            <button class="ghost" id="home">Terug</button>
          </div></div>`;
        document.getElementById("again").onclick = () => runQuiz(Quiz.shuffle(questions), host, { mode });
        document.getElementById("home").onclick  = () => go("home");
        return;
      }
      const q = questions[i];
      Quiz.render(host, q, {
        idxInfo: `Vraag ${i + 1} / ${questions.length}`,
        onAnswered: (ok) => {
          if (ok) correct++;
          review.push({ q, correct: ok });
          i++;
          next();
        }
      });
    };
    next();
  };

  // ---------- VERBANDEN ----------
  const renderVerbanden = () => {
    subtitle.textContent = "Kruisverbanden — snap je het grote plaatje?";

    if (!content.verbanden.length) {
      view.innerHTML = `<div class="card"><p>Nog geen kruisverbanden ingevoerd.</p></div>`;
      return;
    }

    let html = `<div class="card"><h2>Kruisverbanden</h2>
      <p class="muted">Klik op een verband om de uitleg te bekijken. Daaronder kun je oefenen.</p></div>`;
    for (const v of content.verbanden) {
      const begripsTermen = (v.betreft || []).map(id => {
        const b = content.begrippen.find(x => x.id === id);
        return b ? b.term : id;
      });
      html += `<div class="card">
        <h3>${esc(v.titel)} <span class="chip">${esc(Data.chapterTitle(content, v.hoofdstuk))}</span></h3>
        <div class="chips" style="margin:6px 0">${begripsTermen.map(t => `<span class="chip brand">${esc(t)}</span>`).join("")}</div>
        ${v.afbeelding ? `<figure class="qimg"><a href="${esc(v.afbeelding)}" target="_blank" rel="noopener">
          <img loading="lazy" src="${esc(v.afbeelding)}" alt="" /></a></figure>` : ""}
        <details><summary>Toon uitleg</summary><p>${esc(v.uitleg)}</p></details>
      </div>`;
    }

    // Oefenronde: alle inzichtvragen (kruisverband-georiënteerd)
    const inzicht = content.vragen.filter(q => q.type === "inzicht");
    html += `<div class="card"><h3>Oefen inzichtvragen (${inzicht.length})</h3>
      <p class="muted">Deze vragen toetsen kruisverbanden en begrip op VWO-niveau.</p>
      <button class="primary" id="startV">Start</button></div>
      <div id="vHost"></div>`;
    view.innerHTML = html;
    document.getElementById("startV").onclick = () => {
      if (!inzicht.length) {
        document.getElementById("vHost").innerHTML = `<div class="card"><p>Geen inzichtvragen beschikbaar.</p></div>`;
        return;
      }
      runQuiz(Quiz.shuffle(inzicht), document.getElementById("vHost"), { mode: "verbanden" });
    };
  };

  // ---------- PROEFTOETS ----------
  const renderToetsConfig = () => {
    subtitle.textContent = "Proeftoets — realistische test";

    view.innerHTML = `
      <div class="card">
        <h2>Proeftoets samenstellen</h2>
        <p>De toets mixt meerkeuze, open en inzichtvragen uit alle hoofdstukken — net als een echt proefwerk.</p>
        <div class="row">
          <label>Aantal vragen:
            <select id="n">
              <option value="10">10</option>
              <option value="15" selected>15</option>
              <option value="20">20</option>
            </select>
          </label>
          <label>Tijdslimiet (min):
            <select id="t">
              <option value="0">geen</option>
              <option value="15">15</option>
              <option value="20" selected>20</option>
              <option value="30">30</option>
            </select>
          </label>
          <button class="primary" id="startToets">Start proeftoets</button>
        </div>
      </div>
      <div id="toetsHost"></div>
    `;

    document.getElementById("startToets").onclick = () => {
      const n = parseInt(document.getElementById("n").value, 10);
      const tmin = parseInt(document.getElementById("t").value, 10);
      const set = buildToets(n);
      runToets(set, tmin);
    };
  };

  // Stelt een gemixte set samen: ~40% MC, ~35% open, ~25% inzicht, verdeeld over hoofdstukken.
  const buildToets = (n) => {
    const mc      = Quiz.shuffle(content.vragen.filter(q => q.type === "mc"));
    const open    = Quiz.shuffle(content.vragen.filter(q => q.type === "open"));
    const inzicht = Quiz.shuffle(content.vragen.filter(q => q.type === "inzicht"));
    const want = {
      mc:      Math.round(n * 0.40),
      open:    Math.round(n * 0.35),
      inzicht: n - Math.round(n * 0.40) - Math.round(n * 0.35),
    };
    const take = (arr, k) => arr.slice(0, Math.min(k, arr.length));
    let pick = [...take(mc, want.mc), ...take(open, want.open), ...take(inzicht, want.inzicht)];

    // Aanvullen als er te weinig in een categorie zat
    if (pick.length < n) {
      const rest = Quiz.shuffle(content.vragen.filter(q => !pick.includes(q)));
      pick = pick.concat(rest.slice(0, n - pick.length));
    }
    return Quiz.shuffle(pick);
  };

  const runToets = (questions, minutes) => {
    let i = 0, correct = 0;
    const review = [];
    const host = document.getElementById("toetsHost");
    let endsAt = null, timerEl = null, timerHandle = null;

    if (minutes > 0) endsAt = Date.now() + minutes * 60 * 1000;

    const renderTimer = () => {
      if (!endsAt || !timerEl) return;
      const left = Math.max(0, endsAt - Date.now());
      const mm = Math.floor(left / 60000), ss = Math.floor((left % 60000) / 1000);
      timerEl.textContent = `${mm}:${String(ss).padStart(2, "0")}`;
      if (left <= 0) { clearInterval(timerHandle); finish(true); }
    };

    const finish = (timeUp = false) => {
      if (timerHandle) clearInterval(timerHandle);
      const pct = Math.round((correct / questions.length) * 100);
      const grade =
        pct >= 90 ? "🌟 Uitstekend" :
        pct >= 75 ? "👍 Goed" :
        pct >= 55 ? "🙂 Voldoende" :
        pct >= 35 ? "😬 Bijna" : "❗ Nog veel oefenen";

      host.innerHTML = `<div class="card">
        <h2>Proeftoets — resultaat</h2>
        ${timeUp ? `<p class="chip warn">⏰ Tijd voorbij</p>` : ""}
        <p style="font-size:1.2rem"><b>${correct}/${questions.length}</b> goed — ${pct}% — ${grade}</p>
        <div class="progress"><span style="width:${pct}%"></span></div>
        <hr/>
        <h3>Nakijken</h3>
        <ul class="def-list">${review.map((r, idx) => `
          <li>
            <span class="chip ${r.correct ? 'brand' : 'bad'}">${r.correct ? 'goed' : 'fout'}</span>
            <span class="meta">${idx + 1}. ${esc(Data.chapterTitle(content, r.q.hoofdstuk))} · ${r.q.type}</span>
            <div style="margin-top:4px"><b>${esc(r.q.vraag)}</b></div>
            <div class="muted" style="margin-top:4px">
              ${r.q.type === "mc"
                ? "Goede optie: " + esc(r.q.opties[r.q.antwoord_index])
                : "Modelantwoord: " + esc(r.q.antwoord)}
            </div>
          </li>`).join("")}
        </ul>
        <div class="row" style="margin-top:14px">
          <button class="primary" id="herkans">Nieuwe proeftoets</button>
          <button class="ghost"   id="home">Terug naar start</button>
        </div>
      </div>`;
      document.getElementById("herkans").onclick = () => renderToetsConfig();
      document.getElementById("home").onclick    = () => go("home");
    };

    const renderHeader = () => {
      const head = document.createElement("div");
      head.className = "row between";
      head.style.marginBottom = "10px";
      head.innerHTML = `
        <div class="row"><span class="chip brand">Proeftoets</span>
          <span class="muted">${i + 1} / ${questions.length}</span></div>
        <div class="row">${endsAt ? `<span class="chip warn">⏱️ <span id="timer">…</span></span>` : ""}
          <button class="ghost" id="stop">Stop & nakijken</button></div>`;
      return head;
    };

    const next = () => {
      if (i >= questions.length) return finish(false);
      host.innerHTML = "";
      host.appendChild(renderHeader());
      const qHost = document.createElement("div");
      host.appendChild(qHost);

      timerEl = document.getElementById("timer");
      if (endsAt) {
        renderTimer();
        timerHandle = setInterval(renderTimer, 500);
      }
      document.getElementById("stop").onclick = () => finish(false);

      const q = questions[i];
      Quiz.render(qHost, q, {
        idxInfo: null,
        onAnswered: (ok) => {
          if (timerHandle) clearInterval(timerHandle);
          if (ok) correct++;
          review.push({ q, correct: ok });
          i++;
          next();
        }
      });
    };
    next();
  };

  // ---------- BOEK (foto's bekijken) ----------
  const PAGE_FILES = [
    "101657948","101705255","101713805","101718373","101726780","101732336",
    "101740664","101745196","101752681",
    "101757207","101806392","101811140","101819863","101823729","101831251","101908856",
    "101920404","101924475","101935795","101942220","101950157","101954550","102001394","102006026","102013669","102018397",
    "102026478","102030802","102037810","102042676","102051386","102056072","102104432","102109211","102122953"
  ];
  const PAGE_SECTIONS = [
    { titel: "5.1 Het skelet",                idx: [0, 9] },
    { titel: "5.2 De bouw van botten",        idx: [9, 16] },
    { titel: "5.3 Beenverbindingen / gewrichten", idx: [16, 26] },
    { titel: "5.4 Spieren",                   idx: [26, 35] },
  ];
  const renderBoek = () => {
    subtitle.textContent = "Boekpagina's — alle foto's";
    let html = `<div class="card"><h2>Pagina's uit Stijn's boek</h2>
      <p class="muted">Klik op een foto voor de volledige pagina. Handig om iets na te zoeken bij het leren.</p></div>`;
    for (const s of PAGE_SECTIONS) {
      const slice = PAGE_FILES.slice(s.idx[0], s.idx[1]);
      html += `<div class="card"><h3>${esc(s.titel)} <span class="muted">(${slice.length} pagina's)</span></h3>
        <div class="pages-grid">${slice.map(id => `
          <a href="img/pages/PXL_20260524_${id}.jpg" target="_blank" rel="noopener" title="${id}">
            <img loading="lazy" src="img/pages/PXL_20260524_${id}.jpg" alt="pagina ${id}" />
          </a>`).join("")}</div></div>`;
    }
    view.innerHTML = html;
  };

  // ---------- bootstrap ----------
  go("home").catch(() => {});
})();
