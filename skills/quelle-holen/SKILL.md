---
name: quelle-holen
description: Lädt das von einer Clipping-Kampagne freigegebene Ausgangsmaterial (VOD, Stream, Podcastfolge, Drive-Datei) mit yt-dlp herunter, bevorzugt nur benötigte Abschnitte plus Untertitel. Benutzen, wenn ein Video für eine Kampagne geholt werden soll oder als zweiter Schritt von /clip-kampagnen:los.
---

# Quelle holen

## Voraussetzungen

`yt-dlp` und `ffmpeg` müssen im PATH sein. Prüf mit `yt-dlp --version` und `ffmpeg -version`.
Fehlt etwas, sag dem Nutzer, wie er es installiert (siehe README des Plugins):
Windows `winget install yt-dlp.yt-dlp` und `winget install Gyan.FFmpeg`, Mac `brew install yt-dlp ffmpeg`.

## Grundregeln

- Lade **nur** Material, das in `clips/<kurzname>/regeln.md` als erlaubte Quelle steht oder das der
  Nutzer ausdrücklich als freigegeben bestätigt. Sonst: nachfragen, nicht laden.
- Keine Logins, keine Cookies aus dem Browser, kein Umgehen von Paywalls oder DRM.
- Lade so wenig wie möglich: erst Untertitel bzw. Ton, ganze Videos nur wenn nötig.

## Ablauf

1. Lies `clips/<kurzname>/regeln.md` und frag nach dem konkreten Link, falls er dort fehlt.
2. Metadaten: `yt-dlp --dump-json --skip-download "<link>"` → Titel, Dauer, Kanal in
   `clips/<kurzname>/quelle.md` notieren.
3. Untertitel (schnell und klein):
   `yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "de.*,en.*" --convert-subs srt -o "clips/<kurzname>/quelle" "<link>"`
4. Gibt es keine Untertitel, nur den Ton laden:
   `yt-dlp -x --audio-format mp3 -o "clips/<kurzname>/ton.%(ext)s" "<link>"`
5. Das Video selbst wird erst in `clip-bauen` abschnittsweise geladen (`--download-sections`). Bei
   Dateien von Drive o. Ä., die keine Abschnitte können, einmal komplett laden:
   `yt-dlp -f "bv*[height<=1080]+ba/b" -o "clips/<kurzname>/quelle.%(ext)s" "<link>"`
6. Melde kurz, was jetzt im Ordner liegt, und mach mit `momente-finden` weiter.
