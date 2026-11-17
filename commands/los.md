---
description: Komplett-Durchlauf - Kampagne finden, Quelle holen, Momente finden, Clips bauen, Texte schreiben, Regeln prüfen
argument-hint: "[Thema oder Kampagnen-Link, optional]"
---

Führe den kompletten Clip-Ablauf dieses Plugins aus. Eingabe des Nutzers: $ARGUMENTS

Nutze nacheinander diese Skills des Plugins `clip-kampagnen`:

1. `kampagnen-suche` – mit dem Thema bzw. Link oben, falls angegeben. **Warte**, bis der Nutzer eine
   Kampagne gewählt hat.
2. `quelle-holen` – nur erlaubtes Material der gewählten Kampagne.
3. `momente-finden` – **warte**, bis der Nutzer die Momente ausgewählt hat (oder "alle" sagt).
4. `clip-bauen` – für jeden gewählten Moment.
5. `text-paket` – für jeden Clip.
6. `regel-check` – für jeden Clip.

Zum Schluss: kurze Übersicht in `clips/<kurzname>/uebersicht.md` (Nr, Datei, Dauer, Hook, Status) und
im Chat, wo die fertigen Dateien liegen. Nichts posten, nichts einreichen, nirgends einloggen.
