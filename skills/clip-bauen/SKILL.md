---
name: clip-bauen
description: Baut aus einem ausgewählten Moment ein fertiges Hochkant-Kurzvideo (9:16, 1080x1920) mit großen eingebrannten Untertiteln und optionalem Hook-Text, bereit zum Posten auf TikTok, Shorts oder Reels. Benutzen, wenn der Nutzer einen Clip schneiden, hochkant machen oder untertiteln will oder als vierter Schritt von /clip-kampagnen:los.
---

# Clip bauen

Im selben Ordner wie diese Datei liegt das Hilfsskript `srt_ausschnitt.py`. Nutze dessen vollen Pfad.
Unter Windows heißt Python oft `py` statt `python3`.

## Grundregeln

- Überschreib nie fertige Dateien: ffmpeg immer mit `-n`.
- Halte dich an `clips/<kurzname>/regeln.md` (Länge, Wasserzeichen, Pflicht-Einblendungen).
- Die Clips müssen erkennbar **bearbeitet** sein (Schnitt, Format, Untertitel, Hook). Viele Kampagnen
  lehnen reine Reuploads ab.

## Ablauf für jeden Moment Nr N (Start S, Ende E aus `momente.md`)

1. **Abschnitt holen** (nur wenn nicht schon eine lokale `quelle.*` existiert):
   `yt-dlp --download-sections "*S-E" --force-keyframes-at-cuts -f "bv*[height<=1080]+ba/b" --merge-output-format mp4 -o "clips/<kurzname>/NN-roh.%(ext)s" "<link>"`
   Bei lokaler Quelle stattdessen:
   `ffmpeg -n -ss S -to E -i clips/<kurzname>/quelle.mp4 -c:v libx264 -c:a aac clips/<kurzname>/NN-roh.mp4`
2. **Untertitel zuschneiden:**
   `python3 <skillordner>/srt_ausschnitt.py clips/<kurzname>/quelle.de.srt S E clips/<kurzname>/NN.srt`
   (Englische Quelle → `quelle.en.srt`. Kein Transkript vorhanden → mit Whisper direkt aus `NN-roh.mp4`
   erzeugen: `whisper clips/<kurzname>/NN-roh.mp4 --output_format srt --output_dir clips/<kurzname>` und
   die Datei in `NN.srt` umbenennen.)
3. **Layout wählen** – frag den Nutzer einmal pro Kampagne, falls unklar. Standard ist A.
   - **A – Unscharfer Hintergrund** (passt fast immer): Video mittig, oben und unten unscharf gefüllt.
   - **B – Vollbild-Ausschnitt**: Mitte des Bildes auf 9:16 zugeschnitten (gut bei einer Person im Bild).
4. **Rendern** (in den Ordner `clips/<kurzname>` wechseln, damit der Untertitelpfad einfach bleibt):

   Layout A:
   ```
   ffmpeg -n -i NN-roh.mp4 -filter_complex "[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,boxblur=20:2[bg];[0:v]scale=1080:-2[fg];[bg][fg]overlay=(W-w)/2:(H-h)/2,subtitles=NN.srt:force_style='FontName=Arial,FontSize=16,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV=70'[v]" -map "[v]" -map "0:a?" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart NN-fertig.mp4
   ```
   Layout B:
   ```
   ffmpeg -n -i NN-roh.mp4 -vf "scale=-2:1920,crop=1080:1920,subtitles=NN.srt:force_style='FontName=Arial,FontSize=16,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=3,Shadow=0,Alignment=2,MarginV=70'" -c:v libx264 -preset medium -crf 20 -pix_fmt yuv420p -c:a aac -b:a 160k -movflags +faststart NN-fertig.mp4
   ```
   **Hook-Text** (aus `text-paket`) für die ersten 3 Sekunden oben einblenden: an die Filterkette
   `,drawtext=text='HOOK':fontcolor=white:fontsize=64:box=1:boxcolor=black@0.6:boxborderw=20:x=(w-text_w)/2:y=220:enable='lt(t,3)'`
   anhängen. Doppelpunkte und Apostrophe im Hook vorher entfernen. Unter Windows ggf.
   `fontfile='C\:/Windows/Fonts/arialbd.ttf'` ergänzen.
5. **Kontrolle:** `ffprobe -v error -show_entries format=duration:stream=width,height -of csv=p=0 NN-fertig.mp4`
   muss 1080x1920 und die erwartete Dauer zeigen. Mach ein Standbild bei Sekunde 2
   (`ffmpeg -n -ss 2 -i NN-fertig.mp4 -frames:v 1 NN-vorschau.png`) und schau es dir an: Untertitel
   lesbar, nichts Wichtiges abgeschnitten? Sonst Layout wechseln.
6. Danach `text-paket` und `regel-check`.
