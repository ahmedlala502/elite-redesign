# -*- coding: utf-8 -*-
"""Static audit: broken links, dead anchors, language leakage, a11y basics.

Run with:  python audit.py
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = [f for f in ["index.html", "dashboard.html", "case-studies.html", "sponsors.html", "about.html", "contacts.html"]]
ALL = [(p, False) for p in PAGES] + [(os.path.join("ar", p).replace("\\", "/"), True) for p in PAGES]

ARABIC = re.compile(r"[؀-ۿ]")
# Latin tokens that legitimately appear on an Arabic page: the wordmark, its
# tagline, and brand names — brands are never translated. The allowlist is
# harvested from the markup itself (data-name / logo cells) rather than by
# importing a generator, so the audit has no build side effects.
def _brand_words():
    words = set()
    for page, _ar in ALL:
        path = os.path.join(ROOT, page)
        if not os.path.exists(path):
            continue
        src = io.open(path, encoding="utf-8").read()
        names = re.findall(r'data-name="([^"]+)"', src)
        names += re.findall(r'class="logo-cell">([^<]+)<', src)
        names += re.findall(r'class="showcase__brand">([^<]+)<', src)
        for n in names:
            words.update(re.findall(r"[A-Za-z'’]+", n))
    return {w.lower() for w in words}


ALLOWED_LATIN = None  # filled after ALL is known

EXTRA_LATIN = {
    "elite", "elit", "instagram", "copyright",
}

ALLOWED_LATIN = _brand_words() | EXTRA_LATIN

problems = []


def note(page, kind, msg):
    problems.append((page, kind, msg))


for page, ar in ALL:
    path = os.path.join(ROOT, page)
    if not os.path.exists(path):
        note(page, "missing", "page does not exist")
        continue
    s = io.open(path, encoding="utf-8").read()
    base = os.path.dirname(path)

    # --- lang / dir ---
    m = re.search(r'<html lang="([^"]+)"(?: dir="([^"]+)")?', s)
    if not m:
        note(page, "lang", "no <html lang>")
    else:
        want_lang, want_dir = ("ar", "rtl") if ar else ("en", "ltr")
        if m.group(1) != want_lang:
            note(page, "lang", "lang=%s expected %s" % (m.group(1), want_lang))
        if m.group(2) != want_dir:
            note(page, "lang", "dir=%s expected %s" % (m.group(2), want_dir))

    # --- internal links resolve ---
    for href in re.findall(r'href="([^"]+)"', s):
        if href.startswith(("http", "mailto:", "tel:", "#", "data:")):
            continue
        target = os.path.normpath(os.path.join(base, href.split("#")[0]))
        if not os.path.exists(target):
            note(page, "link", "dead link -> %s" % href)

    # --- asset references resolve (src and video posters alike) ---
    for src in re.findall(r'src="([^"]+)"', s) + re.findall(r'poster="([^"]+)"', s):
        if src.startswith(("http", "data:")):
            continue
        # A leading slash is root-relative to the site, not to this page.
        target = os.path.join(ROOT, src.lstrip("/")) if src.startswith("/") else os.path.join(base, src)
        if not os.path.exists(os.path.normpath(target)):
            note(page, "asset", "missing asset -> %s" % src)

    # --- in-page anchors resolve ---
    ids = set(re.findall(r'id="([^"]+)"', s))
    for a in re.findall(r'href="#([^"]+)"', s):
        if a and a not in ids:
            note(page, "anchor", "dead anchor -> #%s" % a)

    # --- language toggle points at the twin page ---
    tog = re.search(r'<a class="chip-btn" href="([^"]+)" hreflang="([^"]+)"', s)
    name = os.path.basename(page)
    if not tog:
        note(page, "i18n", "no language toggle")
    else:
        want = ("../%s" % name) if ar else ("ar/%s" % name)
        if tog.group(1) != want:
            note(page, "i18n", "toggle -> %s expected %s" % (tog.group(1), want))
        if tog.group(2) != ("en" if ar else "ar"):
            note(page, "i18n", "toggle hreflang=%s" % tog.group(2))

    # --- language leakage ---
    text = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&[a-z]+;|&#\d+;", " ", text)
    # Email examples and URLs are Latin by nature; they are not untranslated copy.
    text = re.sub(r"\S+@\S+|https?://\S+", " ", text)
    if ar:
        for word in re.findall(r"[A-Za-z][A-Za-z'’]{3,}", text):
            if word.lower() not in ALLOWED_LATIN:
                note(page, "i18n", "untranslated English: %s" % word)
    else:
        if ARABIC.search(text):
            sample = ARABIC.search(text)
            note(page, "i18n", "Arabic text on English page near %r" % text[max(0, sample.start() - 20):sample.start() + 20])

    # --- accessibility basics ---
    for img in re.findall(r"<img\b[^>]*>", s):
        if "alt=" not in img:
            note(page, "a11y", "img without alt: %s" % img[:70])
    for btn in re.findall(r"<button\b[^>]*>\s*</button>", s):
        if "aria-label" not in btn:
            note(page, "a11y", "empty button without aria-label: %s" % btn[:70])
    if 'id="main"' not in s:
        note(page, "a11y", "no #main landmark for the skip link")
    if s.count("<h1") != 1:
        note(page, "a11y", "expected exactly one h1, found %d" % s.count("<h1"))


if problems:
    by_kind = {}
    for p, k, m in problems:
        by_kind.setdefault(k, []).append((p, m))
    for kind in sorted(by_kind):
        print("\n## %s (%d)" % (kind, len(by_kind[kind])))
        seen = set()
        for p, m in by_kind[kind]:
            key = (p, m)
            if key in seen:
                continue
            seen.add(key)
            print("  %-26s %s" % (p, m))
    print("\n%d problem(s)" % len(problems))
    sys.exit(1)
print("clean — no problems found")
