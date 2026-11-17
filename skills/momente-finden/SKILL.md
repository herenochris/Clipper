---
name: momente-finden
description: Findet die stärksten, clipwürdigen Momente in einem langen Video (Stream, VOD, Podcast) anhand von Transkript und Lautstärkespitzen und schlägt Start/Ende für Kurzclips vor. Benutzen, wenn der Nutzer gute Stellen, Highlights oder Clip-Ideen aus einem Video will oder als dritter Schritt von /clip-kampagnen:los.
---

# Momente finden

## Ablauf

1. **Transkript besorgen** (in dieser Reihenfolge):
   - `clips/<kurzname>/quelle.*.srt` aus `quelle-holen`
   - sonst mit Whisper, falls installiert: `whisper clips/<kurzname>/ton.mp3 --language de --output_format srt --output_dir clips/<kurzname>`
     (bzw. `faster-whisper`). Ist nichts installiert, sag es und frag den Nutzer nach Zeitstempeln.
2. **Lautstärkespitzen** als Hinweis (Lachen, Schreie, Jubel):
   `ffmpeg -i clips/<kurzname>/ton.mp3 -af ebur128=framelog=verbose -f null - 2>&1 | grep "M:"`
   Nutze die lautesten Bereiche nur als Zusatzsignal, nicht als einzigen Grund.
3. **Momente auswählen.** Gute Clip-Momente haben: einen klaren Anfang ohne Vorwissen, eine Pointe,
   Überraschung, starke Emotion, eine steile These oder eine nützliche Info. 15 bis 60 Sekunden
   (oder was `regeln.md` vorgibt). Lieber 2 Sekunden vor dem Höhepunkt einsteigen als 20.
4. **Liste schreiben:** nach `clips/<kurzname>/momente.md`, höchstens 8 Vorschläge, beste zuerst:

   | Nr | Start | Ende | Dauer | Worum es geht | Warum es zieht | Zitat (wörtlich aus Transkript) |

   Zitate nur wörtlich aus dem Transkript, nichts dazu erfinden.
5. Frag den Nutzer, welche Nummern gebaut werden sollen ("alle" ist okay). Dann `clip-bauen`.
