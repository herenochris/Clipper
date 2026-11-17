---
name: text-paket
description: Schreibt für einen fertigen Kurzclip den Hook (Texteinblendung in den ersten Sekunden), Titel, Caption und Hashtags passend zu Plattform und Kampagnenregeln. Benutzen, wenn der Nutzer Hook, Titel, Beschreibung, Caption oder Hashtags für einen Clip will oder als fünfter Schritt von /clip-kampagnen:los.
---

# Text-Paket

## Grundregeln

- Kein Clickbait, der dem Clip nicht entspricht. Kein erfundenes Zitat. Keine falschen Zahlen.
- Pflicht-Hashtags, Erwähnungen und Hinweise aus `clips/<kurzname>/regeln.md` kommen immer rein.
- Sprache wie im Clip, außer die Kampagne verlangt etwas anderes.

## Ablauf pro Clip NN

1. Lies `momente.md` (Worum es geht, Zitat), `NN.srt` und `regeln.md`.
2. Schreib:
   - **3 Hooks**, je höchstens 7 Wörter, für die Einblendung in Sekunde 0 bis 3. Ohne Doppelpunkt und
     Apostroph (ffmpeg-tauglich). Markiere deinen Favoriten.
   - **Titel** für YouTube Shorts (höchstens 70 Zeichen).
   - **Caption** für TikTok/Instagram: 1 bis 2 Sätze + Pflichtangaben.
   - **Hashtags**: Pflicht-Hashtags + 3 bis 5 passende, keine irreführenden Trend-Hashtags.
3. Speichere alles in `clips/<kurzname>/NN-text.md`.
4. Hat `clip-bauen` noch keinen Hook eingebrannt, biete an, den Clip mit dem Favoriten neu zu rendern.
