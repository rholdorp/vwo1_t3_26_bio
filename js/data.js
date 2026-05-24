// Laadt en valideert content.json.
const Data = (() => {
  let cache = null;

  const load = async () => {
    if (cache) return cache;
    const r = await fetch("data/content.json", { cache: "no-store" });
    if (!r.ok) throw new Error(`content.json niet gevonden (${r.status})`);
    const j = await r.json();
    validate(j);
    cache = j;
    return j;
  };

  const validate = (j) => {
    const required = ["hoofdstukken", "begrippen", "feiten", "verbanden", "vragen"];
    for (const k of required) {
      if (!Array.isArray(j[k])) throw new Error(`content.json mist veld "${k}" (lijst).`);
    }
    const hids = new Set(j.hoofdstukken.map(h => h.id));
    const bids = new Set(j.begrippen.map(b => b.id));
    for (const q of j.vragen) {
      if (q.hoofdstuk && !hids.has(q.hoofdstuk)) {
        throw new Error(`Vraag ${q.id} verwijst naar onbekend hoofdstuk "${q.hoofdstuk}".`);
      }
      if (q.type === "mc") {
        if (!Array.isArray(q.opties) || q.opties.length < 2) throw new Error(`MC ${q.id}: minstens 2 opties.`);
        if (typeof q.antwoord_index !== "number" || q.antwoord_index < 0 || q.antwoord_index >= q.opties.length)
          throw new Error(`MC ${q.id}: antwoord_index ongeldig.`);
      } else if (q.type === "open" || q.type === "inzicht") {
        if (typeof q.antwoord !== "string") throw new Error(`Open vraag ${q.id}: antwoord ontbreekt.`);
      } else {
        throw new Error(`Vraag ${q.id}: onbekend type "${q.type}".`);
      }
    }
    for (const v of j.verbanden) {
      for (const ref of (v.betreft || [])) {
        if (!bids.has(ref)) throw new Error(`Verband ${v.id} verwijst naar onbekend begrip "${ref}".`);
      }
    }
  };

  const chapterTitle = (j, id) => (j.hoofdstukken.find(h => h.id === id) || {}).titel || id;

  return { load, chapterTitle };
})();
