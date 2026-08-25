# -*- coding: utf-8 -*-
"""Real campaign media per success story, from the Elite platform CDN.

Each record carries the campaign video (or still), its screenshots, the brand
logo, and the creators who actually ran it. Stories with no record here fall
back to the generated CSS artwork.

The scraped avatar URLs repeat their path prefix many times over
(f_s3/2026-04/.../f_s3/2026-01/...). The CDN serves both forms; only the last
segment is kept here.
"""

CDN = "https://grand-community.fra1.digitaloceanspaces.com/uploads-live/f_s3"


def _cs(date, name):
    return "%s/photos/case_studies/%s/%s" % (CDN, date, name)


def _brand(date, name):
    return "%s/photos/brands/%s/%s" % (CDN, date, name)


def _av(date, country, name):
    return "%s/%s/photos/influencers/%s/instagram/%s" % (CDN, date, country, name)


# name -> media record. `video` is an mp4; `still` is used when the campaign has
# no video. `shots` are stills from the campaign, used as video posters.
MEDIA = {
    "Enigmaku": {
        "country": "kw",
        "video": _cs("2026-03", "1861094955247019.mp4"),
        "shots": [_cs("2026-03", n) for n in
                  ["1861094958627998.png", "1861094959488837.png",
                   "1861094960989853.png", "1861094962669770.png"]],
        "logo": _brand("2025-04", "1829293951041501.jfif"),
        "avatars": [_av("2024-11", "kw", "get2fit_1816870244110578.jpg"),
                    _av("2024-11", "kw", "alabeautysalon_1806448583973800.jpg"),
                    _av("2024-11", "kw", "dr.desho_1809806883454696.jpg")],
        "more": 17,
    },
    "Beit El Sabban": {
        "country": "sa",
        "video": _cs("2026-03", "1861005282291885.mp4"),
        "shots": [_cs("2026-03", n) for n in
                  ["1861005285833577.png", "1861005286693766.png",
                   "1861005287657865.png", "1861005288314998.png"]],
        "logo": _brand("2025-04", "1829841142556666.jpg"),
        "avatars": [_av("2024-11", "sa", "nermin_mohsen_1816926583595378.jpg"),
                    _av("2025-02", "sa", "mazenabdallahhh_1823674608706764.jpg"),
                    _av("2024-11", "sa", "alaaofficial__1816922786898832.jpg")],
        "more": 17,
    },
    "Tashas Cafe": {
        "country": "sa",
        "video": _cs("2026-03", "1861001850605665.mp4"),
        "shots": [_cs("2026-03", n) for n in
                  ["1861001854215021.png", "1861001855027616.png",
                   "1861001856101836.png", "1861001857416124.png"]],
        "logo": _brand("2026-01", "1853457970803878.png"),
        "avatars": [_av("2024-11", "sa", "monashe22_1816697144029761.jpg"),
                    _av("2024-11", "sa", "waadshaat1_18250133.jpeg"),
                    _av("2025-05", "sa", "hindboumchamar_1832777762972062.jpg")],
        "more": 17,
    },
    "Fred": {
        "country": "sa",
        "still": _cs("2026-03", "1861000674652848.jpg"),
        "shots": [],
        "logo": _brand("2025-11", "1849298812811393.jpeg"),
        "avatars": [_av("2024-11", "sa", "ayadiabb_1816931249643717.jpg")],
        "more": 0,
    },
    "Panerai": {
        "country": "sa",
        "still": _cs("2026-03", "1861000621413694.jpg"),
        "shots": [],
        "logo": _brand("2025-11", "1849298418738385.jpeg"),
        "avatars": [_av("2024-12", "sa", "alyahya23_1819170728399347.jpg")],
        "more": 0,
    },
    "Kiko": {
        "country": "sa",
        "video": _cs("2026-03", "1861000132801022.mp4"),
        "shots": [],
        "logo": _brand("2025-11", "1849298978115382.png"),
        "avatars": [_av("2024-12", "eg", "mennathabet_makeupartist_42891819.jpeg")],
        "more": 0,
    },
    "Rituals Cosmetics": {
        "country": "sa",
        "video": _cs("2026-03", "1860999803298860.mp4"),
        "shots": [_cs("2026-03", "1860999806249719.png")],
        "logo": _brand("2025-11", "1849302888070172.jpg"),
        "avatars": [_av("2024-11", "sa", "maram_alnahla_1816738298182379.jpg"),
                    _av("2024-11", "sa", "tulip8i8_1816785505562072.jpg")],
        "more": 0,
    },
    "tabl.to": {
        "country": "sa",
        "video": _cs("2026-03", "1860994169424703.mp4"),
        "shots": [_cs("2026-03", "1860994175649128.png"),
                  _cs("2026-03", "1860994178423578.png")],
        "logo": _brand("2026-01", "1855635817194466.jpg"),
        "avatars": [_av("2024-11", "sa", "drrmohh_25111303.jpeg"),
                    _av("2024-12", "sa", "samerdosary_55294768.jpeg"),
                    _av("2024-11", "sa", "chef_turki_1_1816931350551599.jpg")],
        "more": 17,
    },
    "Million Riyal Menu": {
        "country": "sa",
        "video": _cs("2026-03", "1860920513399519.mp4"),
        "shots": [],
        "logo": _brand("2026-02", "1856726442503833.png"),
        "avatars": [_av("2025-07", "sa", "ahmadhmadeh03_1838804488414246.jpg"),
                    _av("2025-07", "sa", "u7l7_1838090066685013.jpg"),
                    _av("2024-11", "sa", "rashdb_1815931968747625.jpg")],
        "more": 4,
    },
    "Jones the Grocer": {
        "country": "sa",
        "video": _cs("2025-05", "1832466427021874.mp4"),
        "shots": [_cs("2025-05", n) for n in
                  ["1832466429846960.png", "1832466430888165.png",
                   "1832466431523462.png"]],
        "logo": _brand("2025-05", "1832465679080023.jpg"),
        "avatars": [_av("2024-11", "sa", "salehalobidy_1816926462274153.jpg"),
                    _av("2024-12", "sa", "layla_iskandar_92900503.jpeg"),
                    _av("2024-11", "sa", "lolita2050_1816929123988181.jpg")],
        "more": 17,
    },
}


def get(name):
    return MEDIA.get(name)


def all_urls():
    """Every URL in the table, for the link checker."""
    urls = []
    for rec in MEDIA.values():
        for key in ("video", "still", "logo"):
            if rec.get(key):
                urls.append(rec[key])
        urls.extend(rec.get("shots", []))
        urls.extend(rec.get("avatars", []))
    return urls
