---
name: regel-check
description: Prüft einen fertigen Clip samt Text vor dem Posten gegen die Regeln der Kampagne und die Plattform (Format, Länge, Pflicht-Hashtags, Quelle erlaubt, keine verbotenen Inhalte) und gibt eine Ampel. Benutzen, wenn der Nutzer fragt, ob ein Clip passt, ob er ihn posten oder einreichen kann, oder als letzter Schritt von /clip-kampagnen:los.
---

# Regel-Check

Prüfe jeden fertigen Clip `clips/<kurzname>/NN-fertig.mp4` mit `NN-text.md` gegen `regeln.md`.

## Prüfpunkte

1. **Technik** mit
   `ffprobe -v error -show_entries format=duration:stream=codec_type,width,height -of json NN-fertig.mp4`:
   1080x1920, Dauer innerhalb der Vorgabe, Tonspur vorhanden.
2. **Quelle erlaubt:** Der Link in `quelle.md` steht in den erlaubten Quellen von `regeln.md`.
3. **Pflichtangaben** aus `regeln.md` sind in `NN-text.md` (Hashtags, Erwähnungen, Hinweise).
4. **Verbote:** nichts von dem, was die Kampagne ausschließt (z. B. Werbung für Dritte, KI-Stimme,
   unbearbeiteter Reupload, falsche Behauptungen im Hook).
5. **Plattform-Basics:** keine erkennbar fremde Musik, die nicht im Original war; kein Inhalt, der gegen
   Community-Richtlinien verstößt (Gewalt real, Hetze, Nacktheit).
6. **Ehrlichkeit:** Hook und Titel passen zum Inhalt.

## Ausgabe

Eine Tabelle pro Clip mit 🟢 / 🟡 / 🔴 je Prüfpunkt und einer Gesamtampel. Bei 🔴 sag konkret, was zu
ändern ist, und biete an, es zu reparieren. Ergänze die Spalte "Status" in `clips/<kurzname>/uebersicht.md`
(`bereit` / `nacharbeiten`).

Zum Schluss erinnere den Nutzer: **Posten und Einreichen macht er selbst**, über seine Konten und die
Kampagnenseite. Verdienst ist nicht garantiert; Kampagnen können Clips ablehnen.
