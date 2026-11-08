# A0–A1 Curriculum Map (draft v1)

Draft for review by a German teacher before use. Built to match the telc Deutsch A1 topics (Lesen, Hören, Schreiben, Sprechen) and the existing app content in `content.js`.

**Language of instruction:** German first, with a one-tap English hint on every instruction and grammar explanation.

**Lesson template (every lesson):** Lernziel (objective) · Wortschatz (8–10 words with article and plural) · Grammatik (1 point) · Hören · Üben (3–5 exercises) · Sprechen or Schreiben · Mini-Test (5 questions) · 12–15 minutes.

| # | Module | Lessons | Grammar focus | Exam skill |
|---|--------|---------|---------------|------------|
| 0 | Start | 0.1 Alphabet & Aussprache · 0.2 Begrüßen & Verabschieden · 0.3 Zahlen 0–100 | Satzmelodie, Buchstabieren | Hören: Zahlen verstehen |
| 1 | Sich vorstellen | 1.1 Name, Herkunft, Wohnort · 1.2 Alter, Beruf, Sprachen · 1.3 Formular ausfüllen | sein, heißen, kommen, wohnen; Verb auf Position 2 | Schreiben Teil 1 (Formular); Sprechen Teil 1 |
| 2 | Familie & Freunde | 2.1 Familienmitglieder · 2.2 Personen beschreiben · 2.3 Über die Familie sprechen | haben; mein/dein/sein/ihr; Plural | Hören: kurze Gespräche |
| 3 | Zeit & Tagesablauf | 3.1 Uhrzeit · 3.2 Wochentage, Monate, Datum · 3.3 Mein Tag | um/am/im; trennbare Verben | Lesen: Zeitangaben, Pläne |
| 4 | Essen & Trinken | 4.1 Lebensmittel · 4.2 Im Restaurant · 4.3 Was isst du gern? | der/die/das; ein/eine; Akkusativ; möchten; kein/nicht | Sprechen Teil 2 (Fragen & Antworten) |
| 5 | Einkaufen | 5.1 Im Supermarkt (Mengen) · 5.2 Kleidung & Preise · 5.3 Geschäfte & Öffnungszeiten | Zahlen & Preise; W-Fragen (Wie viel?) | Lesen: Schilder, Anzeigen |
| 6 | Wohnen | 6.1 Zimmer & Möbel · 6.2 Wohnungssuche · 6.3 Nachbarn & Hausregeln | Präpositionen in/auf/neben (Ort); Imperativ | Lesen: Anzeigen; Sprechen Teil 3 (Bitten) |
| 7 | Unterwegs | 7.1 Wegbeschreibung · 7.2 Bus & Bahn · 7.3 Reisen & Hotel | links/rechts/geradeaus; nach/aus/zu; Modalverb können | Hören: Durchsagen |
| 8 | Gesundheit | 8.1 Körper · 8.2 Beim Arzt · 8.3 Termin vereinbaren | müssen; Imperativ (Sie-Form) | Hören: Telefonansagen; Sprechen Teil 3 |
| 9 | Arbeit & Lernen | 9.1 Berufe & Arbeitsalltag · 9.2 Im Kurs · 9.3 E-Mails & Nachrichten | Konnektoren und/aber/oder/denn | Schreiben Teil 2 (kurze Nachricht) |
| 10 | Freizeit & Planen | 10.1 Hobbys · 10.2 Verabredungen & Einladungen · 10.3 Wetter & Wochenende | wollen/können; Perfekt (Grundlagen) | Schreiben Teil 2; Lesen: Einladungen |
| 11 | Dienstleistungen | 11.1 Post & Paket · 11.2 Bank & Formulare · 11.3 Telefon & Notizen | Höfliche Bitten (Können Sie …?) | Lesen/Hören: Alltagstexte |
| 12 | Prüfungstraining | 12.1 Lesen-Strategien · 12.2 Hören-Strategien · 12.3 Schreiben-Muster · 12.4 Sprechen-Training · 12.5 Probeprüfung | Wiederholung aller Strukturen | Alle vier Teile, mit Zeit |

## Notes for building
- ~39 lessons total. Per lesson: about 10 words (390 words), 1 grammar point, 1 listening, 1 reading, 1 production task.
- Reuse existing content: the 17 grammar lessons and 8 everyday themes in `content.js` map onto modules 1–11. Missing modules: 0 (pronunciation), 2.2 (adjectives), 3.2 (dates), 6.3 (location prepositions) need new grammar entries.
- Add per-lesson fields to the content format: `module`, `objective`, `minutes`, `completion` (score needed to unlock the next lesson).
- Every lesson needs native-speaker review before release. Mark unreviewed lessons as draft in the data.
- Official format and scoring for telc A1 must be checked against telc's own materials, not assumed from this table.
