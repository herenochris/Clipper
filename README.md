# clip-kampagnen

Ein Claude-Code-Plugin auf Deutsch: Es sucht Clipping-Kampagnen auf
[contentrewards.com](https://contentrewards.com) und produziert dafür fertige Kurzvideos
(Hochformat 9:16, große Untertitel, Hook-Einblendung) plus Titel, Caption und Hashtags.

**Gepostet und eingereicht wird nichts automatisch.** Du bekommst fertige Dateien und postest sie selbst.
Kein Skill loggt sich irgendwo ein. Verdienst ist nicht garantiert.

## Installation (am PC)

1. **Claude Code** installieren
   - Windows (PowerShell): `irm https://claude.ai/install.ps1 | iex`
   - Mac/Linux: `curl -fsSL https://claude.ai/install.sh | bash`
2. **Werkzeuge** installieren
   - Windows: `winget install yt-dlp.yt-dlp` und `winget install Gyan.FFmpeg`
   - Mac: `brew install yt-dlp ffmpeg`
   - Python 3 (für die Untertitel-Hilfe): Windows `winget install Python.Python.3.12`, Mac ist meist schon da
   - Optional für Videos ohne Untertitel: `pip install openai-whisper`
   - Danach ein **neues** Terminal öffnen und prüfen: `yt-dlp --version`, `ffmpeg -version`
3. Einen Arbeitsordner anlegen, z. B. `Clips`, dort ein Terminal öffnen und `claude` starten.
4. In Claude Code:
   ```
   /plugin marketplace add herenochris/Clipper
   /plugin install clip-kampagnen@clip-kampagnen
   ```
   Danach Claude Code einmal neu starten.

## Benutzen

Alles auf einmal:
```
/clip-kampagnen:los
```
oder mit Thema: `/clip-kampagnen:los Podcast-Kampagnen auf Deutsch`

Claude fragt an drei Stellen nach: welche Kampagne, welche Momente, welches Layout.
Die fertigen Videos liegen danach in `clips/<kampagne>/NN-fertig.mp4`, die Texte in `NN-text.md`.

Du kannst die Schritte auch einzeln anstoßen, einfach in normalen Worten
("such mir Kampagnen", "mach aus Moment 3 einen Clip", "prüf den Clip").

## Die Skills

| Skill | Was er macht |
| --- | --- |
| `kampagnen-suche` | Kampagnen auf contentrewards.com finden, Regeln und erlaubte Quellen notieren |
| `quelle-holen` | Freigegebenes Ausgangsmaterial und Untertitel mit yt-dlp laden |
| `momente-finden` | Starke Stellen über Transkript und Lautstärke finden |
| `clip-bauen` | Schneiden, 9:16, Untertitel einbrennen, Hook einblenden (ffmpeg) |
| `text-paket` | Hook, Titel, Caption, Hashtags |
| `regel-check` | Ampel-Prüfung gegen Kampagnenregeln vor dem Posten |

## Wichtig

- **Nur erlaubtes Material clippen.** Das Plugin arbeitet nur mit Quellen, die eine Kampagne freigibt oder
  die du als freigegeben bestätigst. Fremde Inhalte ohne Erlaubnis zu posten kann Urheberrechte verletzen.
- contentrewards.com zeigt manche Kampagnen nur nach Login. Dann fragt Claude dich nach dem Link oder dem
  Regeltext, den du aus deinem Browser einfügst.
- Lies vor jedem Befehl kurz mit, bevor du in Claude Code zustimmst.

## Lizenz

MIT
