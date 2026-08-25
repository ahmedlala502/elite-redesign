# -*- coding: utf-8 -*-
"""Re-applies the shared chrome to the two hand-written English pages.

index.html and dashboard.html hold hand-authored bodies, so they are not built
by build_pages.py. This script swaps their head/nav/footer for the ones in
build_shell.py, keeping every page's chrome identical. Run it after changing
build_shell.py:

    python sync_chrome.py
"""
import io, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_shell import head, nav, footer

ROOT = os.path.dirname(os.path.abspath(__file__))

PAGES = [
    ("index.html", "Elite — Niche Mastery Redefined",
     "Elite is the #1 influencer marketing platform: creator discovery, campaign strategy, "
     "content creation and performance tracking across 52+ countries."),
    ("dashboard.html", "Dashboard — Elite",
     "One workspace for branches, creators, campaign stages and coverage reporting."),
]

for name, title, desc in PAGES:
    path = os.path.join(ROOT, name)
    s = io.open(path, encoding="utf-8").read()
    # The body is everything between the main landmark and the footer.
    body = s[s.index('<main id="main">'):s.index('<footer class="foot">')]
    out = head(title, desc, name) + nav(name) + "\n" + body + footer() + "\n"
    io.open(path, "w", encoding="utf-8").write(out)
    print("synced", name, len(out))
print("DONE")
