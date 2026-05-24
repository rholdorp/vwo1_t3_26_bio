// Eenvoudige wrapper rond localStorage met JSON-(de)serialisatie en namespacing.
const Storage = (() => {
  const NS = "biotrainer.v1.";
  const get = (key, fallback) => {
    try { const v = localStorage.getItem(NS + key); return v == null ? fallback : JSON.parse(v); }
    catch { return fallback; }
  };
  const set = (key, value) => {
    try { localStorage.setItem(NS + key, JSON.stringify(value)); } catch {}
  };
  const remove = (key) => { try { localStorage.removeItem(NS + key); } catch {} };
  const clearAll = () => {
    try {
      const toRemove = [];
      for (let i = 0; i < localStorage.length; i++) {
        const k = localStorage.key(i);
        if (k && k.startsWith(NS)) toRemove.push(k);
      }
      toRemove.forEach(k => localStorage.removeItem(k));
    } catch {}
  };
  return { get, set, remove, clearAll };
})();
