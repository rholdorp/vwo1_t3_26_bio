# Content toevoegen vanuit een foto

Stappen om een boekpagina om te zetten naar leerstof voor de app:

1. **Foto in `raw/`** zetten, met duidelijke naam (zie `raw/README.md`).
2. **Begrippen** uit de pagina overnemen → vul `begrippen` in `data/content.json`. Eén begrip = één definitie. Hou ze kort en in eigen woorden.
3. **Feiten** die geen begrip zijn maar wel uit het hoofd moeten (bv. "Een insect heeft 6 poten") → vul `feiten`.
4. **Kruisverbanden**: als twee onderwerpen samenhangen (vaak tussen hoofdstukken), voeg een `verband` toe met een korte uitleg. Dit is dé manier waarop VWO-vragen lastig worden gemaakt, dus niet overslaan.
5. **Vragen**: maak per onderwerp:
   - 2–4 makkelijke MC-vragen (reproductie).
   - 2–3 gemiddelde open vragen.
   - 1–2 lastige inzichtvragen (kruisverband, "leg uit", "wat als").

## Sneltips

- Hergebruik `id`s nooit. Een schema: `b-` begrip, `f-` feit, `v-` verband, `q-` vraag, dan kort onderwerp.
- Eén hoofdstuk = één `id`, bv. `h5`. Verwijs hier consequent naar in `hoofdstuk`-velden.
- Bij MC: zorg dat exact één optie helemaal klopt. Andere opties moeten *plausibel maar fout* zijn (vaak verwarringen die in het boek genoemd worden).
- Bij open vragen: `kernwoorden` zijn de termen die ABSOLUUT in een goed antwoord horen. De app gebruikt ze als hint na het invullen.

## Validatie

Na bewerken: open `index.html` in de browser. De app toont bovenaan een foutmelding als `content.json` ongeldig JSON is of als een vraag verwijst naar een onbekend hoofdstuk.
