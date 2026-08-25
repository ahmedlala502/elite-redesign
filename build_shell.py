# -*- coding: utf-8 -*-
"""Shared page chrome — head, nav and footer.

Both generators (build_pages.py and build_ar_extra.py) pull the chrome from here
so the nav, footer and meta block cannot drift apart between the English and
Arabic trees the way they had.
"""

SITE = "https://eelite.vercel.app"  # used for canonical + hreflang + og:url

# (file, English label, Arabic label)
NAV_PAGES = [
    ("index.html",        "Home",            "الرئيسية"),
    ("dashboard.html",    "Dashboard",       "مساحة العمل"),
    ("case-studies.html", "Success Stories", "قصص النجاح"),
    ("sponsors.html",     "Our Clients",     "عملاؤنا"),
    ("about.html",        "About",           "من نحن"),
    ("contacts.html",     "Contact",         "تواصل معنا"),
]

FONTS_LATIN = ("https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300;400;500;700"
               "&family=Red+Hat+Text:wght@400;500&family=Montserrat:wght@500;600&display=swap")
# Arabic pages need a real Arabic face; Tahoma was only ever a fallback.
FONTS_ARABIC = ("https://fonts.googleapis.com/css2?family=Red+Hat+Display:wght@300;400;500;700"
                "&family=Montserrat:wght@500;600"
                "&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap")


def _rel(page, ar):
    """Link from inside the current tree to a page in the same language."""
    return page


def head(title, desc, page, ar=False, og_desc=None):
    """<head> + skip link + opening body tag."""
    base = "../" if ar else ""
    css = base + "assets/css/elite.css"
    rtl = '\n<link rel="stylesheet" href="%sassets/css/elite-rtl.css">' % base if ar else ""
    lang, dirn = ("ar", "rtl") if ar else ("en", "ltr")
    fonts = FONTS_ARABIC if ar else FONTS_LATIN
    en_url = "%s/%s" % (SITE, page)
    ar_url = "%s/ar/%s" % (SITE, page)
    canonical = ar_url if ar else en_url
    page_id = page.replace(".html", "")
    return f"""<!DOCTYPE html>
<html lang="{lang}" dir="{dirn}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0B0C">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="ar" href="{ar_url}">
<link rel="alternate" hreflang="x-default" href="{en_url}">
<link rel="icon" href="{base}assets/img/elite-logo.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Elite">
<meta property="og:locale" content="{'ar_SA' if ar else 'en_US'}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{og_desc or desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{SITE}/assets/img/elite-logo.svg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="{fonts}" rel="stylesheet">
<link rel="stylesheet" href="{css}">{rtl}
<script>(function(){{try{{var t=localStorage.getItem('elite-theme');if(t)document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();</script>
</head>
<body data-page="{page_id}">
<a class="skip" href="#main">{'تخطَّ إلى المحتوى' if ar else 'Skip to content'}</a>
"""


def nav(page, ar=False):
    """Sticky header. `page` is the bare filename, e.g. 'about.html'."""
    i = 2 if ar else 1
    links = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (row[0], ' aria-current="page"' if row[0] == page else "", row[i])
        for row in NAV_PAGES
    )
    # Language toggle points at the twin page in the other tree.
    toggle = ("../%s" % page) if ar else ("ar/%s" % page)
    lang_label, lang_aria = ("EN", "التبديل إلى الإنجليزية") if ar else ("AR", "Switch language to Arabic")
    home = "index.html"
    home_aria = "إيليت — الصفحة الرئيسية" if ar else "Elite — home"
    nav_aria = "التنقّل الرئيسي" if ar else "Primary"
    mnav_aria = "التنقّل الرئيسي، الجوال" if ar else "Primary, mobile"
    theme_aria = "تغيير المظهر" if ar else "Switch theme"
    menu_aria = "فتح القائمة" if ar else "Open menu"
    return f"""<header class="nav" id="nav">
  <div class="wrap nav-in">
    <a class="mark nav-mark" href="{home}" aria-label="{home_aria}">ELIT<span class="flip">E</span></a>
    <nav aria-label="{nav_aria}">
      <ul class="nav-links">{links}</ul>
    </nav>
    <div class="nav-tools">
      <a class="chip-btn" href="{toggle}" hreflang="{'en' if ar else 'ar'}" lang="{'en' if ar else 'ar'}" aria-label="{lang_aria}">{lang_label}</a>
      <button class="chip-btn" id="theme" type="button" aria-label="{theme_aria}"><span aria-hidden="true">◐</span></button>
      <button class="chip-btn nav-burger" id="burger" type="button" aria-expanded="false" aria-controls="mnav" aria-label="{menu_aria}"><span class="burger-bars" aria-hidden="true"></span></button>
    </div>
  </div>
  <nav class="mnav" id="mnav" data-open="false" aria-label="{mnav_aria}"><ul class="wrap">{links}</ul></nav>
</header>
"""


def footer(ar=False):
    L = lambda e, a: a if ar else e
    base = "../" if ar else ""
    return f"""<footer class="foot">
  <div class="wrap foot-in">
    <div>
      <span class="mark foot-mark"><span class="mark-img"><img src="{base}assets/img/elite-logo.svg" alt="{L('Elite — Niche Mastery Redefined','إيليت — إتقانٌ يُعيد تعريف التميّز')}" width="572" height="232" loading="lazy" decoding="async"></span></span>
      <h4>{L('Overview','لمحة')}</h4>
      <p>{L('Elite is the #1 influencer marketing platform to help you achieve all your marketing goals — we launch and manage your campaigns with 24/7 live support.','إيليت هي منصة التسويق عبر المؤثرين التي تعتمد عليها العلامات التجارية الفاخرة للوصول إلى صنّاع المحتوى المناسبين، وإدارة الحملة، وإثبات نتائجها — بدعم مباشر على مدار الساعة.')}</p>
      <form class="sub" data-validate data-success="{L("You're subscribed. Welcome to Elite.",'تم الاشتراك. أهلًا بك في إيليت.')}">
        <label class="sr" for="nl-email">{L('Email address','البريد الإلكتروني')}</label>
        <input id="nl-email" type="email" name="email" placeholder="{L('Enter your email','أدخل بريدك الإلكتروني')}" autocomplete="email" required>
        <button type="submit" aria-label="{L('Subscribe to the newsletter','الاشتراك في النشرة البريدية')}">↗</button>
      </form>
    </div>
    <div><h4>{L('Explore','استكشف')}</h4><ul class="foot-list"><li><a href="dashboard.html">{L('Dashboard','مساحة العمل')}</a></li><li><a href="case-studies.html">{L('Success stories','قصص النجاح')}</a></li><li><a href="sponsors.html">{L('Our clients','عملاؤنا')}</a></li><li><a href="about.html">{L('About us','من نحن')}</a></li></ul></div>
    <div><h4>{L('Company','الشركة')}</h4><ul class="foot-list"><li><a href="contacts.html">{L('Contact us','تواصل معنا')}</a></li><li><a href="about.html">{L('About Elite','عن إيليت')}</a></li></ul></div>
    <div><h4>{L('Our social media','وسائل التواصل')}</h4><ul class="foot-list"><li><a href="https://instagram.com" target="_blank" rel="noopener">Instagram</a></li></ul></div>
  </div>
  <div class="wrap foot-bottom">
    <span>{L('Copyright © <span data-year>2026</span> Elite — all rights reserved','© <span data-year>2026</span> إيليت — جميع الحقوق محفوظة')}</span>
    <span>{L('Niche Mastery Redefined','إتقانٌ يُعيد تعريف التميّز')}</span>
  </div>
</footer>
<div class="toast" id="toast" role="status" aria-live="polite"></div>
<script src="{base}assets/js/elite.js" defer></script>
</body>
</html>"""
