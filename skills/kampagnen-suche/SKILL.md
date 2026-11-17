---
name: kampagnen-suche
description: Sucht laufende Clipping-Kampagnen auf contentrewards.com (Content Rewards, früher Whop Content Rewards) und hält ihre Regeln fest. Benutzen, wenn der Nutzer nach Kampagnen, Clipping-Jobs, "wo kann ich Clips einreichen", Auszahlung pro 1.000 Aufrufe oder einer bestimmten Kampagne fragt, oder als erster Schritt von /clip-kampagnen:los.
---

# Kampagnen-Suche

Finde Clipping-Kampagnen, für die der Nutzer Kurzvideos machen darf, und schreib ihre Regeln so auf,
dass die anderen Skills damit arbeiten können.

## Grundregeln

- Erfinde nichts. Jede Zahl (Satz pro 1.000 Aufrufe, Budget, Mindestaufrufe) stammt von einer Seite, die du
  gerade gelesen hast, mit Link und Datum. Fehlt eine Angabe, schreib "unbekannt".
- Du loggst dich nirgends ein, trittst keiner Kampagne bei und reichst nichts ein. Das macht der Nutzer.
- Eine Kampagne ist nur brauchbar, wenn klar ist, **welches Ausgangsmaterial** geclippt werden darf. Ohne
  diese Angabe: als "Quelle unklar" markieren und keine Clips dafür produzieren.

## Ablauf

1. **Suchen.** Lies mit WebFetch `https://contentrewards.com` und die Übersichts- bzw. Discover-Seite der
   Kampagnen. Ergänze mit WebSearch, z. B. `site:contentrewards.com clipping campaign` oder
   `contentrewards <Thema> campaign`, wenn der Nutzer ein Thema nennt (Streamer, Spiel, Podcast, Marke).
2. **Wenn Seiten nur mit Login gehen** oder leer zurückkommen (die Seite lädt vieles per JavaScript):
   sag das ehrlich und bitte den Nutzer, im Browser eingeloggt die Kampagnen zu öffnen und dir den
   **Link** oder den **Regeltext** der Kampagne hier einzufügen. Arbeite dann mit diesem Text weiter.
3. **Pro Kampagne festhalten:**
   - Name, Link, Datum des Abrufs
   - Satz pro 1.000 Aufrufe und Budget bzw. Restbudget
   - **Erlaubte Quellen** (Kanäle, VODs, Ordner/Drive-Links, die die Kampagne vorgibt)
   - Plattformen (TikTok, YouTube Shorts, Instagram Reels, X ...)
   - Pflichtangaben: Hashtags, Erwähnungen, Link in Bio, Wasserzeichen, Sprache
   - Verbote (z. B. keine Reuploads ohne Bearbeitung, keine KI-Stimmen, kein Clickbait)
   - Länge, Format, Mindestaufrufe, Einreichfrist
4. **Bewerten:** Sortiere nach Machbarkeit für den Nutzer: Quelle klar und erlaubt > Satz > Restbudget.
   Zeig höchstens fünf Kampagnen als kurze Tabelle.
5. **Speichern:** Schreib alles nach `clips/kampagnen.md` im aktuellen Ordner. Bestehende Einträge
   aktualisieren statt doppelt anlegen. Für die ausgewählte Kampagne lege `clips/<kurzname>/regeln.md`
   mit den Regeln aus Schritt 3 an. `<kurzname>`: klein, ohne Leerzeichen, z. B. `streamer-xy`.
6. Frag den Nutzer, welche Kampagne er machen will. Erst dann geht es mit `quelle-holen` weiter.
