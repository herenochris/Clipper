#!/usr/bin/env python3
"""Schneidet aus einer SRT-Datei den Bereich START bis ENDE aus und setzt ihn auf 0 zurück.

Nutzung: python3 srt_ausschnitt.py quelle.srt 00:12:30 00:13:05 ausschnitt.srt
Zeiten als HH:MM:SS, MM:SS oder Sekunden (auch mit Nachkommastellen).
Lange Untertitelzeilen werden in kurze Stücke (höchstens 4 Wörter) geteilt, wie bei Kurzvideos üblich.
"""
import re
import sys

ZEIT = re.compile(r"(\d+):(\d+):(\d+)[,.](\d+)\s*-->\s*(\d+):(\d+):(\d+)[,.](\d+)")


def sekunden(text):
    teile = [float(t) for t in text.replace(",", ".").split(":")]
    wert = 0.0
    for t in teile:
        wert = wert * 60 + t
    return wert


def srt_zeit(s):
    s = max(0.0, s)
    ms = int(round(s * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    sek, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{sek:02d},{ms:03d}"


def bloecke(inhalt):
    for block in re.split(r"\n\s*\n", inhalt.replace("\r", "")):
        zeilen = [z for z in block.strip().split("\n") if z.strip()]
        for i, zeile in enumerate(zeilen):
            m = ZEIT.search(zeile)
            if m:
                g = [int(x) for x in m.groups()]
                a = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
                b = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
                text = " ".join(re.sub(r"<[^>]+>", "", z) for z in zeilen[i + 1:]).strip()
                if text:
                    yield a, b, text
                break


def main():
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    quelle, start, ende, ziel = sys.argv[1], sekunden(sys.argv[2]), sekunden(sys.argv[3]), sys.argv[4]
    with open(quelle, encoding="utf-8", errors="replace") as f:
        inhalt = f.read()
    ausgabe, letzter_text, nr = [], None, 0
    for a, b, text in bloecke(inhalt):
        if b <= start or a >= ende:
            continue
        # Auto-Untertitel wiederholen oft die Vorzeile: Doppeltes entfernen
        if letzter_text and text.startswith(letzter_text):
            text = text[len(letzter_text):].strip()
        letzter_text = " ".join(text.split()) or letzter_text
        woerter = text.split()
        if not woerter:
            continue
        # Erst über die volle Dauer der Zeile verteilen, dann auf den Ausschnitt begrenzen,
        # damit Wörter vor START wegfallen statt nach vorne zu rutschen
        stuecke = [woerter[i:i + 4] for i in range(0, len(woerter), 4)]
        dauer = (b - a) / len(stuecke)
        for j, stueck in enumerate(stuecke):
            von, bis = a + j * dauer, a + (j + 1) * dauer
            if bis <= start or von >= ende:
                continue
            nr += 1
            von, bis = max(von, start) - start, min(bis, ende) - start
            ausgabe.append(f"{nr}\n{srt_zeit(von)} --> {srt_zeit(bis)}\n{' '.join(stueck)}\n")
    with open(ziel, "w", encoding="utf-8") as f:
        f.write("\n".join(ausgabe))
    print(f"{nr} Untertitel nach {ziel} geschrieben")


if __name__ == "__main__":
    main()
