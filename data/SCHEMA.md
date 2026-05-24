# content.json — schema

De hele leerstof staat in één bestand: `data/content.json`.
De webapp leest dit bij het laden in. Pas dit bestand aan om nieuwe stof toe te voegen.

## Topstructuur

```json
{
  "vak": "Biologie",
  "niveau": "VWO 1",
  "proefwerk": "T3 week 26",
  "hoofdstukken": [ { ... } ],
  "begrippen":    [ { ... } ],
  "feiten":       [ { ... } ],
  "verbanden":    [ { ... } ],
  "vragen":       [ { ... } ]
}
```

## hoofdstukken

```json
{ "id": "h5", "titel": "Cellen", "bron": "raw/h05_p82_cellen.jpg" }
```

## begrippen (definities; gebruikt door flashcards + MC-distractors)

```json
{
  "id": "b-cel",
  "hoofdstuk": "h5",
  "term": "Cel",
  "definitie": "De kleinste levende bouwsteen van een organisme.",
  "tags": ["bouw", "basis"]
}
```

## feiten (losse, leerbare uitspraken)

```json
{
  "id": "f-fotosynthese-formule",
  "hoofdstuk": "h6",
  "feit": "Bij fotosynthese maakt een plant glucose en zuurstof uit koolstofdioxide en water, met licht als energiebron.",
  "tags": ["fotosynthese"]
}
```

## verbanden (kruisverbanden tussen begrippen/feiten)

```json
{
  "id": "v-foto-ademhaling",
  "hoofdstuk": "h6",
  "titel": "Fotosynthese vs. verbranding",
  "uitleg": "Fotosynthese en verbranding zijn elkaars omgekeerde processen: de stoffen die bij het ene proces ontstaan, worden bij het andere verbruikt.",
  "betreft": ["b-fotosynthese", "b-verbranding"]
}
```

## vragen

Drie types: `mc` (meerkeuze), `open` (vrij invullen), `inzicht` (kruisverband / toepassing, vrij invullen met modelantwoord).

```json
{
  "id": "q-001",
  "hoofdstuk": "h5",
  "type": "mc",
  "moeilijkheid": "makkelijk",
  "vraag": "Welk onderdeel van de cel bevat het DNA?",
  "opties": ["Celmembraan", "Cytoplasma", "Celkern", "Mitochondrium"],
  "antwoord_index": 2,
  "uitleg": "Het DNA ligt opgeslagen in de celkern."
}
```

```json
{
  "id": "q-002",
  "hoofdstuk": "h6",
  "type": "open",
  "moeilijkheid": "gemiddeld",
  "vraag": "Schrijf het woordreceptaarschema van fotosynthese op.",
  "antwoord": "koolstofdioxide + water --(licht)--> glucose + zuurstof",
  "kernwoorden": ["koolstofdioxide", "water", "licht", "glucose", "zuurstof"]
}
```

```json
{
  "id": "q-003",
  "hoofdstuk": "h6",
  "type": "inzicht",
  "moeilijkheid": "lastig",
  "vraag": "Leg uit waarom planten in het donker geen netto zuurstof afgeven, terwijl ze dat overdag wel doen.",
  "antwoord": "In het donker stopt de fotosynthese, maar de verbranding (ademhaling) gaat door. Daardoor verbruiken planten 's nachts zuurstof in plaats van afgeven. Overdag is de fotosynthese groter dan de verbranding, waardoor er netto zuurstof vrijkomt.",
  "kernwoorden": ["fotosynthese stopt", "verbranding gaat door", "netto", "licht"]
}
```

### Velden bij `open` / `inzicht`

- `antwoord`: modelantwoord (wordt getoond na zelfbeoordeling).
- `kernwoorden`: lijst van termen die in het antwoord van de leerling moeten voorkomen. De app markeert welke gevonden zijn en geeft een suggestiescore, maar de leerling beoordeelt zelf of het antwoord goed/halverwege/fout was.

### Moeilijkheid

`"makkelijk" | "gemiddeld" | "lastig"`. De Proeftoets-modus put uit alle moeilijkheden, met meer lastige vragen bij Inzicht.

## Tips voor goede VWO-1 vragen

- Stel vragen die **begrip** testen, niet alleen reproductie ("Waarom...", "Wat zou er gebeuren als...", "Vergelijk... met...").
- Maak bij MC de afleiders plausibel — gebruik andere begrippen uit hetzelfde hoofdstuk.
- Verwijs in `inzicht`-vragen naar minstens twee begrippen uit verschillende hoofdstukken voor kruisverband.
