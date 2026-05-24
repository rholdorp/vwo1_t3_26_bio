// Lichte spaced-repetition (geïnspireerd op SM-2).
// State per item: { ef, interval, reps, due (ms), lastGrade }
// Grade: 0 = fout, 1 = lastig, 2 = goed, 3 = makkelijk.
const SRS = (() => {
  const KEY = "srs";
  const DAY = 86400000;

  const load = () => Storage.get(KEY, {});
  const save = (s) => Storage.set(KEY, s);

  const init = () => ({ ef: 2.5, interval: 0, reps: 0, due: Date.now(), lastGrade: null });

  const review = (id, grade) => {
    const state = load();
    const s = state[id] || init();
    if (grade === 0) {
      s.reps = 0;
      s.interval = 0;
      s.due = Date.now() + 5 * 60 * 1000; // 5 min later opnieuw
    } else {
      s.reps += 1;
      if (s.reps === 1) s.interval = 1;
      else if (s.reps === 2) s.interval = 2;
      else s.interval = Math.round(s.interval * s.ef);
      const q = [0, 3, 4, 5][grade];
      s.ef = Math.max(1.3, s.ef + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)));
      s.due = Date.now() + s.interval * DAY;
    }
    s.lastGrade = grade;
    state[id] = s;
    save(state);
    return s;
  };

  const dueItems = (allIds) => {
    const state = load();
    const now = Date.now();
    const seen = [], unseen = [];
    for (const id of allIds) {
      const s = state[id];
      if (!s) unseen.push(id);
      else if (s.due <= now) seen.push({ id, due: s.due });
    }
    seen.sort((a, b) => a.due - b.due);
    return [...unseen, ...seen.map(x => x.id)];
  };

  const stats = (allIds) => {
    const state = load();
    let learned = 0, dueNow = 0, neverSeen = 0;
    const now = Date.now();
    for (const id of allIds) {
      const s = state[id];
      if (!s) { neverSeen++; continue; }
      if (s.due <= now) dueNow++;
      if (s.reps >= 2 && s.lastGrade >= 2) learned++;
    }
    return { total: allIds.length, learned, dueNow, neverSeen };
  };

  return { review, dueItems, stats, _load: load };
})();
