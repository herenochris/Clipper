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

1. **Alle Kampagnen einsammeln.** Lies mit WebFetch `https://contentrewards.com` und die Übersichts- bzw.
   Discover-Seite der Kampagnen. Geh **alle** Seiten der Übersicht durch (Seitenzahlen, "Mehr laden",
   `?page=2` usw.) und alle Kategorien bzw. Filter, bis keine neuen Kampagnen mehr kommen. Ergänze mit
   WebSearch, z. B. `site:contentrewards.com clipping campaign` oder `contentrewards <Thema> campaign`,
   wenn der Nutzer ein Thema nennt (Streamer, Spiel, Podcast, Marke). Führe eine Liste aller gefundenen
   Kampagnen-Links ohne Doppelte.
2. **Jede Kampagne einzeln öffnen.** Öffne jeden Link aus Schritt 1 mit WebFetch und lies die Regeln. Nicht
   nach der Übersicht allein bewerten, dort fehlen meist erlaubte Quellen und Verbote. Bei sehr vielen
   Kampagnen (über 40): sag dem Nutzer die Zahl und arbeite sie trotzdem vollständig ab, in Blöcken.
3. **Wenn Seiten nur mit Login gehen** oder leer zurückkommen (die Seite lädt vieles per JavaScript):
   sag das ehrlich und bitte den Nutzer, im Browser eingeloggt die Kampagnen zu öffnen und dir die
   **Links** oder den **Regeltext** hier einzufügen. Arbeite dann mit diesem Text weiter. Behaupte nie,
   alle Kampagnen geprüft zu haben, wenn du nur einen Teil lesen konntest.
4. **Pro Kampagne festhalten:**
   - Name, Link, Datum des Abrufs
   - Satz pro 1.000 Aufrufe und Budget bzw. Restbudget
   - **Erlaubte Quellen** (Kanäle, VODs, Ordner/Drive-Links, die die Kampagne vorgibt)
   - Plattformen (TikTok, YouTube Shorts, Instagram Reels, X ...)
   - Pflichtangaben: Hashtags, Erwähnungen, Link in Bio, Wasserzeichen, Sprache
   - Verbote (z. B. keine Reuploads ohne Bearbeitung, keine KI-Stimmen, kein Clickbait)
   - Länge, Format, Mindestaufrufe, Einreichfrist
5. **Alle bewerten, die besten 5 vorschlagen.** Sortiere **alle** Kampagnen nach Machbarkeit für den
   Nutzer: Quelle klar und erlaubt > Satz pro 1.000 Aufrufe > Restbudget. Kampagnen ohne Restbudget, mit
   abgelaufener Frist oder mit unklarer Quelle kommen ans Ende. Beginne die Antwort mit
   "X Kampagnen gefunden, Y geprüft" (bei X ≠ Y den Grund nennen) und zeig dann die **besten 5** als
   Tabelle: Rang, Name, Satz, Restbudget, Quelle, Plattformen, warum sie oben ist.
6. **Speichern:** Schreib **alle** geprüften Kampagnen mit Rang nach `clips/kampagnen.md` im aktuellen
   Ordner, nicht nur die besten 5. Bestehende Einträge aktualisieren statt doppelt anlegen. Für die
   ausgewählte Kampagne lege `clips/<kurzname>/regeln.md` mit den Regeln aus Schritt 4 an.
   `<kurzname>`: klein, ohne Leerzeichen, z. B. `streamer-xy`.
7. Frag den Nutzer, welche Kampagne er machen will. Erst dann geht es mit `quelle-holen` weiter.
