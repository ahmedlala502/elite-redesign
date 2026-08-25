# -*- coding: utf-8 -*-
"""Turns the scraped case-study export into a generated data module.

Run when assets/gc-elite-com-*.xlsx changes:

    python import_case_studies.py

It writes case_studies.py, which the page generators import. The spreadsheet
holds no video URLs (224 asset links, none .mp4), so films come from VIDEOS
below — captured separately from the live site.
"""
import io, os, re, sys, glob

try:
    import openpyxl
except ImportError:
    sys.exit("openpyxl is required to re-import the spreadsheet: pip install openpyxl")

ROOT = os.path.dirname(os.path.abspath(__file__))
CDN = "https://grand-community.fra1.digitaloceanspaces.com/uploads-live/f_s3"

# The export writes brand handles; these are the names used on the site.
NAMES = {
    "beitelsabban": "Beit El Sabban",
    "panerai": "Panerai",
    "ritualscosmeticsgcc": "Rituals Cosmetics",
    "clap": "Clap",
    "ilbarettosa": "Il Baretto",
    "crazypizza.saudi": "Crazy Pizza",
    "beefbar": "Beefbar",
    "ruya": "Rüya",
    "stregishotels": "St. Regis Hotels",
    "thebackburner": "The Back Burner",
    "maserati": "Maserati",
    "Nawader aloud": "Nawader Aloud",
    "Swaikhat And Tanoor": "Swaikhat & Tanoor",
    "Jon&Vinny's": "Jon & Vinny's",
    "BLACK TAP": "Black Tap",
    "Roka": "ROKA KSA",
}

MARKETS = {
    "sa": "Saudi Arabia", "kw": "Kuwait", "ae": "United Arab Emirates",
    "qa": "Qatar", "bh": "Bahrain", "eg": "Egypt",
}

# Categories carried over from the client roster. Brands absent here have no
# category on record and are left blank rather than guessed.
CATEGORIES = {
    "A.O.K Kitchen": "Restaurant", "Agio": "Restaurant", "Beefbar": "Restaurant",
    "Beit El Sabban": "Restaurant", "Brute": "Restaurant", "Clap": "Restaurant",
    "Coya": "Restaurant", "Enigmaku": "Fashion", "Fred": "Fashion",
    "Iris": "Restaurant", "Jones the Grocer": "Cafe", "Kiko": "Beauty",
    "Lavenue": "Restaurant", "MYAZŪ": "Restaurant", "Maryool": "Restaurant",
    "Nawader Aloud": "Perfume", "Panerai": "Fashion", "ROBATA": "Restaurant",
    "ROKA KSA": "Restaurant", "Rituals Cosmetics": "Beauty", "Rüya": "Restaurant",
    "Signor Sassi": "Restaurant", "Swaikhat & Tanoor": "Restaurant",
    "Tashas Cafe": "Cafe", "The Back Burner": "Restaurant", "Urth Caffe": "Cafe",
}

# Films captured from the live case-studies page; the export has none.
VIDEOS = {
    "Enigmaku":           CDN + "/photos/case_studies/2026-03/1861094955247019.mp4",
    "Beit El Sabban":     CDN + "/photos/case_studies/2026-03/1861005282291885.mp4",
    "Tashas Cafe":        CDN + "/photos/case_studies/2026-03/1861001850605665.mp4",
    "Kiko":               CDN + "/photos/case_studies/2026-03/1861000132801022.mp4",
    "Rituals Cosmetics":  CDN + "/photos/case_studies/2026-03/1860999803298860.mp4",
    "tabl.to":            CDN + "/photos/case_studies/2026-03/1860994169424703.mp4",
    "Million Riyal Menu": CDN + "/photos/case_studies/2026-03/1860920513399519.mp4",
    "Jones the Grocer":   CDN + "/photos/case_studies/2025-05/1832466427021874.mp4",
}

# Stills for the two campaigns that have artwork but no film.
STILLS = {
    "Fred":    CDN + "/photos/case_studies/2026-03/1861000674652848.jpg",
    "Panerai": CDN + "/photos/case_studies/2026-03/1861000621413694.jpg",
}


def shorten(url):
    """Avatar paths repeat their prefix up to twenty times; keep the last one."""
    if not url:
        return url
    idx = url.rfind("/f_s3/")
    return CDN + url[idx + 5:] if idx != -1 else url


def sort_key(followers):
    """'24.9M' -> a number, so the grid can lead with the biggest campaigns."""
    m = re.match(r"([\d.]+)\s*([KMB]?)", str(followers or "0"))
    if not m:
        return 0.0
    return float(m.group(1)) * {"": 1, "K": 1e3, "M": 1e6, "B": 1e9}[m.group(2)]


def main():
    books = sorted(glob.glob(os.path.join(ROOT, "assets", "gc-elite-com-*.xlsx")))
    if not books:
        sys.exit("no assets/gc-elite-com-*.xlsx found")
    path = books[-1]
    ws = openpyxl.load_workbook(path, data_only=True)["Sheet1"]

    records = []
    for row in ws.iter_rows(min_row=2, values_only=True):
        raw_name, followers, influencers, country, more = row[3], row[4], row[5], row[6], row[7]
        if not raw_name:
            continue
        name = NAMES.get(str(raw_name).strip(), str(raw_name).strip())
        code = str(country or "").strip().rstrip(",").lower()
        images = [u for u in row[11:19] if u]

        shots = [u for u in images if "/case_studies/" in u]
        logo = next((u for u in images if "/brands/" in u), None)
        avatars = [shorten(u) for u in images if "/influencers/" in u]

        records.append({
            "name": name,
            "market": MARKETS.get(code, ""),
            "code": code,
            "followers": str(followers or "").strip(),
            "influencers": str(influencers or "").strip(),
            "more": int(str(more).strip().lstrip("+")) if more and str(more).strip().lstrip("+").isdigit() else 0,
            "category": CATEGORIES.get(name, ""),
            "video": VIDEOS.get(name),
            "still": STILLS.get(name),
            "shots": shots,
            "logo": logo,
            "avatars": avatars,
        })

    records.sort(key=lambda r: sort_key(r["followers"]), reverse=True)

    out = [
        "# -*- coding: utf-8 -*-",
        '"""GENERATED by import_case_studies.py — do not edit by hand.',
        "",
        "Source: assets/%s" % os.path.basename(path),
        'Films and the two stills are injected by the importer; the export has none."""',
        "",
        "CASE_STUDIES = [",
    ]
    for r in records:
        out.append("    {")
        for key in ("name", "market", "code", "followers", "influencers", "category"):
            out.append("        %-14s %r," % ('"%s":' % key, r[key]))
        out.append("        %-14s %d," % ('"more":', r["more"]))
        for key in ("video", "still", "logo"):
            out.append("        %-14s %r," % ('"%s":' % key, r[key]))
        for key in ("shots", "avatars"):
            out.append("        %-14s [" % ('"%s":' % key))
            for u in r[key]:
                out.append("            %r," % u)
            out.append("        ],")
        out.append("    },")
    out.append("]")
    out.append("")
    out.append("BY_NAME = {r['name']: r for r in CASE_STUDIES}")
    out.append("")
    out.append("# Campaigns with a real frame on file. The rest would only render")
    out.append("# generated artwork, so the case-studies grid leaves them out.")
    out.append("WITH_MEDIA = [r for r in CASE_STUDIES if r['video'] or r['still'] or r['shots']]")
    out.append("")

    target = os.path.join(ROOT, "case_studies.py")
    io.open(target, "w", encoding="utf-8").write("\n".join(out))

    films = sum(1 for r in records if r["video"])
    stills = sum(1 for r in records if r["still"])
    cats = sum(1 for r in records if r["category"])
    print("read     %s" % os.path.basename(path))
    print("wrote    case_studies.py — %d campaigns" % len(records))
    print("         %d films, %d stills, %d with shots, %d categorised"
          % (films, stills, sum(1 for r in records if r["shots"]), cats))
    print("         %d without a category on record" % (len(records) - cats))
    blank = [r["name"] for r in records if not (r["video"] or r["still"] or r["shots"])]
    print("         %d with no frame on file (excluded from the grid): %s"
          % (len(blank), ", ".join(blank) or "none"))


if __name__ == "__main__":
    main()
