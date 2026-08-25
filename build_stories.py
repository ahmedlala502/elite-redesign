# -*- coding: utf-8 -*-
"""Success-story copy and markup.

Every description is derived from the campaign record itself (category, market,
creator count, combined reach) — nothing is claimed that the data does not say.

Card layout follows the destination-card pattern: media filling the whole card,
a market-tinted gradient rising from the bottom edge, and the copy sitting on
top of it with a single action row.
"""
import case_studies

# ---------------------------------------------------------------- vocabulary

CATS_EN = {
    "Restaurant": "Restaurant campaign",
    "Cafe": "Café campaign",
    "Fashion": "Fashion & accessories campaign",
    "Beauty": "Beauty campaign",
    "Perfume": "Fragrance campaign",
    "": "Influencer campaign",
}
CATS_AR = {
    "Restaurant": "حملة مطاعم",
    "Cafe": "حملة مقاهٍ",
    "Fashion": "حملة أزياء وإكسسوارات",
    "Beauty": "حملة تجميل",
    "Perfume": "حملة عطور",
    "": "حملة عبر المؤثرين",
}
LABELS_EN = {"Restaurant": "Restaurant", "Cafe": "Café", "Fashion": "Fashion & accessories",
             "Beauty": "Beauty", "Perfume": "Perfume", "": ""}
LABELS_AR = {"Restaurant": "مطاعم", "Cafe": "مقاهٍ", "Fashion": "أزياء وإكسسوارات",
             "Beauty": "تجميل", "Perfume": "عطور", "": ""}

MARKETS_AR = {
    "Saudi Arabia": "السعودية", "Kuwait": "الكويت", "United Arab Emirates": "الإمارات",
    "Qatar": "قطر", "Bahrain": "البحرين", "Egypt": "مصر", "": "",
}
# "in the United Arab Emirates", not "in United Arab Emirates".
ARTICLE_EN = {"United Arab Emirates": "the United Arab Emirates"}

# One muted accent per market. All low-chroma and dark, so 39 cards still read
# as one family against the obsidian page rather than as a colour chart.
ACCENTS = {
    "sa": "150 30% 20%",
    "kw": "8 34% 26%",
    "ae": "200 30% 22%",
    "qa": "340 24% 24%",
    "bh": "25 34% 24%",
    "eg": "45 30% 22%",
    "": "35 30% 24%",
}


def ar_figure(v):
    """'60M' -> '60 مليون'. Latin magnitude letters do not belong in an Arabic
    figure; a reader of the Arabic tree should not have to know that K means
    thousand."""
    v = str(v).strip()
    for suffix, word in (("B", "مليار"), ("M", "مليون"), ("K", "ألف")):
        if v.upper().endswith(suffix):
            return "%s %s" % (v[:-1], word)
    return v


def figure(v, ar):
    return ar_figure(v) if ar else str(v)


def market(place, ar):
    return MARKETS_AR.get(place, place) if ar else place


def market_in(place, ar):
    """Market name as it reads inside a sentence."""
    if not place:
        return ""
    return MARKETS_AR.get(place, place) if ar else ARTICLE_EN.get(place, place)


# ---------------------------------------------------------------- copy

def ar_creators(n):
    """Arabic counted noun: dual for 2, plural of paucity for 3-10,
    singular for 11 and above."""
    if n == 1:
        return "صانع محتوى واحد"
    if n == 2:
        return "صانعَي محتوى"
    if 3 <= n <= 10:
        return "%d صنّاع محتوى" % n
    return "%d صانع محتوى" % n


def roster(n, ar):
    """Roster size is in the record, so it can be described. Campaign type is not."""
    if ar:
        who = ar_creators(n)
        if n == 1:
            return who
        if n >= 100:
            return "شبكة من %s" % who
        if n < 20:
            return "مجموعة مركّزة من %s" % who
        return who
    if n == 1:
        return "a single creator"
    if n >= 100:
        return "a network of %d creators" % n
    if n < 20:
        return "a focused group of %d creators" % n
    return "%d creators" % n


def describe(rec, ar=False):
    """One sentence per campaign, stating only what the record holds.

    The category is carried by the card's chip and the market by its flag, so
    the sentence covers roster and reach and does not repeat either."""
    n = int(str(rec["influencers"]).lstrip("+") or 0)
    place = market_in(rec["market"], ar)
    if ar:
        where = (" في %s" % place) if place else ""
        f = ar_figure(rec["followers"])
        reach = ("بوصول إلى %s متابع." % f) if n == 1 else ("بوصول تراكمي إلى %s متابع." % f)
        return "%s%s، %s" % (roster(n, True), where, reach)
    who = roster(n, False)
    who = who[0].upper() + who[1:]
    where = (" in %s" % place) if place else ""
    reach = ("reaching %s followers." % rec["followers"]) if n == 1 else ("reaching a combined %s followers." % rec["followers"])
    return "%s%s, %s" % (who, where, reach)


def stat_line(rec, ar=False):
    """The one-line figure summary that sits under the brand name."""
    n = str(rec["influencers"]).lstrip("+")
    if ar:
        return "%s متابع · %s صانع محتوى" % (ar_figure(rec["followers"]), n)
    return "%s followers · %s creators" % (rec["followers"], n)


# ---------------------------------------------------------------- media

def _handle(url):
    """Instagram handle out of an avatar filename."""
    return url.rsplit("/", 1)[-1].rsplit("_", 1)[0]


def crew(rec, ar=False):
    """Avatar stack of the creators who actually ran the campaign."""
    if not rec.get("avatars"):
        return ""
    pics = "".join(
        '<img class="crew__face" src="%s" alt="@%s" width="32" height="32" loading="lazy" decoding="async">'
        % (u, _handle(u)) for u in rec["avatars"][:3]
    )
    more = ('<span class="crew__more">+%d</span>' % rec["more"]) if rec.get("more") else ""
    return '<div class="crew"><div class="crew__faces">%s%s</div></div>' % (pics, more)


def media(rec, art, ar=False):
    """Campaign film, campaign still, a campaign shot, or generated artwork."""
    name = rec["name"]
    L = lambda e, a: a if ar else e

    if rec.get("video"):
        poster = (' poster="%s"' % rec["shots"][0]) if rec.get("shots") else ""
        return ('<video class="story__video" muted loop playsinline preload="none"%s aria-label="%s">'
                '<source src="%s" type="video/mp4"></video>'
                % (poster, L("%s campaign film" % name, "فيلم حملة %s" % name), rec["video"]))

    src = rec.get("still") or (rec["shots"][0] if rec.get("shots") else None)
    if src:
        return ('<img class="story__still" src="%s" alt="%s" loading="lazy" decoding="async">'
                % (src, L("%s campaign still" % name, "لقطة من حملة %s" % name)))

    return '<div class="art art--%s"></div>' % art


# ---------------------------------------------------------------- markup

def card(rec, art, ar=False):
    """Destination-style card: media edge to edge, copy over a tinted gradient."""
    L = lambda e, a: a if ar else e
    name = rec["name"]
    accent = ACCENTS.get(rec["code"], ACCENTS[""])
    label = (LABELS_AR if ar else LABELS_EN)[rec["category"]]
    chip = ('<span class="dcard__chip">%s</span>' % label) if label else ""
    code = (rec["code"] or "").upper()
    # An ISO code in a pill, not an emoji flag — flag glyphs do not render on Windows.
    flag = ('<span class="dcard__flag">%s</span>' % code) if code else ""
    logo = ('<img class="dcard__logo" src="%s" alt="" loading="lazy" decoding="async">' % rec["logo"]) if rec.get("logo") else ""

    # Films get the centred glass player over the media; the action row stays
    # a conversion CTA on every card, so the two are never confused.
    player = ('<button class="dcard__play" type="button" data-video-toggle aria-pressed="false" '
              'aria-label="%s">'
              '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
              '<path class="ico-play" d="M8 5.5v13l11-6.5z"/>'
              '<path class="ico-pause" d="M7 5h3.2v14H7zM13.8 5H17v14h-3.2z"/></svg></button>'
              % L("Play the %s film" % name, "تشغيل فيلم %s" % name)) if rec.get("video") else ""

    action = ('<a class="dcard__cta" href="contacts.html">'
              '<span class="dcard__cta-label">%s</span>'
              '<svg class="dcard__cta-ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
              'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
              '<path d="M5 12h13M12 5l7 7-7 7"/></svg></a>'
              % L("Start a campaign", "ابدأ حملة"))

    return f"""
      <article class="dcard reveal" data-cat="{rec['category']}" data-name="{name}" style="--card-accent:{accent}">
        <div class="dcard__media">{media(rec, art, ar)}</div>
        <div class="dcard__veil" aria-hidden="true"></div>
        {player}
        {logo}
        <div class="dcard__content">
          {chip}
          <h3 class="dcard__title">{name}{flag}</h3>
          <p class="dcard__stats">{stat_line(rec, ar)}</p>
          <p class="dcard__desc">{describe(rec, ar)}</p>
          <div class="dcard__foot">{crew(rec, ar)}{action}</div>
        </div>
      </article>"""


def cards(ar=False):
    """Every campaign on record, biggest reach first."""
    return "".join(card(rec, (i % 6) + 1, ar)
                   for i, rec in enumerate(case_studies.WITH_MEDIA))


def chips(ar=False):
    """Category filters, built from the categories actually present in the data."""
    L = lambda e, a: a if ar else e
    present = []
    for rec in case_studies.WITH_MEDIA:
        if rec["category"] and rec["category"] not in present:
            present.append(rec["category"])
    order = ["Restaurant", "Cafe", "Fashion", "Beauty", "Perfume"]
    present.sort(key=lambda c: order.index(c) if c in order else 99)
    out = ['<button class="chip-toggle" type="button" data-value="all" aria-pressed="true">%s</button>'
           % L("All", "الكل")]
    for c in present:
        out.append('<button class="chip-toggle" type="button" data-value="%s" aria-pressed="false">%s</button>'
                   % (c, (LABELS_AR if ar else LABELS_EN)[c]))
    return "".join(out)


def reel(ar=False):
    """Featured films as full-width alternating rows: media on one side, the
    campaign's identity and figures on the other, flipping each row."""
    L = lambda e, a: a if ar else e
    filmed = [r for r in case_studies.WITH_MEDIA if r.get("video")]

    rows = []
    for i, rec in enumerate(filmed):
        name = rec["name"]
        label = (LABELS_AR if ar else LABELS_EN)[rec["category"]]
        role_bits = [b for b in (market(rec["market"], ar), label) if b]
        role = (" · " if ar else " // ").join(role_bits)
        creators = str(rec["influencers"]).lstrip("+")
        # The reference badge showed a runtime; the figures we actually hold are
        # reach and roster, so the badge carries those instead of a made-up one.
        badge = L("%s REACH // %s CREATORS" % (rec["followers"], creators),
                  "‏وصول %s · %s صانع محتوى" % (ar_figure(rec["followers"]), creators))
        logo = ('<span class="reel__logo"><img src="%s" alt="" loading="lazy" decoding="async"></span>'
                % rec["logo"]) if rec.get("logo") else ""
        poster = (' poster="%s"' % rec["shots"][0]) if rec.get("shots") else ""

        rows.append(f"""
        <article class="reel__row" data-flip="{'true' if i % 2 else 'false'}">
          <div class="reel__media">
            <div class="reel__hatch" aria-hidden="true"></div>
            <video class="story__video" muted loop playsinline preload="none"{poster} aria-label="{L('%s campaign film' % name, 'فيلم حملة %s' % name)}"><source src="{rec['video']}" type="video/mp4"></video>
            <button class="reel__play" type="button" data-video-toggle aria-pressed="false"
                    data-label-play="{L('Play the film','تشغيل الفيلم')}" data-label-pause="{L('Pause the film','إيقاف الفيلم')}"
                    aria-label="{L('Play the %s film' % name, 'تشغيل فيلم %s' % name)}">
              <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path class="ico-play" d="M8 5.5v13l11-6.5z"/><path class="ico-pause" d="M7 5h3.2v14H7zM13.8 5H17v14h-3.2z"/></svg>
            </button>
            <span class="reel__badge">{badge}</span>
          </div>
          <div class="reel__side">
            <div class="reel__ident">
              <div class="reel__hatch" aria-hidden="true"></div>
              {logo}
              <div class="reel__who">
                <h3 class="reel__name">{name}</h3>
                <p class="reel__role">{role}</p>
              </div>
            </div>
            <div class="reel__body">
              <p class="reel__quote">{describe(rec, ar)}</p>
              <div class="reel__figs">
                <div><b>{figure(rec['followers'], ar)}</b><span>{L('Followers','المتابعون')}</span></div>
                <div><b>{rec['influencers']}</b><span>{L('Creators','صنّاع المحتوى')}</span></div>
              </div>
              {crew(rec, ar)}
            </div>
          </div>
        </article>""")

    return f"""
  <section class="sec sec--sunken reel-sec" aria-labelledby="reel-h">
    <div class="wrap">
      <div class="reel-head reveal">
        <h2 class="reel-kicker" id="reel-h">&laquo; {L('Featured work','أعمال مختارة')} &raquo;</h2>
      </div>
      <div class="reel">{''.join(rows)}
      </div>
    </div>
  </section>"""
