# -*- coding: utf-8 -*-
"""Builds the remaining pages (case-studies, sponsors, contacts, about) + Arabic twins."""
import os, io
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUT = os.path.dirname(os.path.abspath(__file__))

from build_shell import head, nav, footer
import build_stories

def page(file, title, desc, body, ar=False):
    name = file[3:] if file.startswith("ar/") else file
    html = head(title, desc, name, ar) + nav(name, ar) + body + footer(ar)
    path = os.path.join(OUT, file)
    with io.open(path, "w", encoding="utf-8") as f: f.write(html)
    print("wrote", file, len(html))

# ── content data shared by EN and AR ──
STORIES = [
 ("Mr.Chow","United Arab Emirates","60M","+569","",1),("A.O.K Kitchen","Saudi Arabia","40M","+309","Restaurant",2),
 ("Enigmaku","Kuwait","24.9M","+186","Fashion",3),("tabl.to","Saudi Arabia","19.7M","+360","",4),
 ("Tashas Cafe","Saudi Arabia","17.9M","+87","Cafe",1),("Iris","Saudi Arabia","17M","+125","Restaurant",2),
 ("Clap","Saudi Arabia","17M","+120","Restaurant",3),("Brute","Saudi Arabia","15M","+93","Restaurant",4),
 ("Lavenue","Saudi Arabia","15M","+89","Restaurant",1),("Beit El Sabban","Saudi Arabia","13.9M","+58","Restaurant",2),
 ("Urth Caffe","Saudi Arabia","12M","+134","Cafe",3),("Jones the Grocer","Saudi Arabia","12M","+118","Cafe",4),
 ("Maryool","Kuwait","9M","+11","Restaurant",1),("Swaikhat & Tanoor","Kuwait","7M","+10","Restaurant",2),
 ("Signor Sassi","Saudi Arabia","5M","+7","Restaurant",3),("MYAZŪ","Saudi Arabia","5M","+6","Restaurant",4),
 ("ROBATA","Saudi Arabia","5M","+5","Restaurant",1),("Agio","Saudi Arabia","4M","+3","Restaurant",2),
 ("Coya","Saudi Arabia","3M","+3","Restaurant",3),("Kiko","Saudi Arabia","2.1M","+1","Beauty",4),
 ("Million Riyal Menu","Saudi Arabia","571.5K","+8","",1),("Panerai","Saudi Arabia","536.1K","+1","Fashion",2),
 ("Fred","Saudi Arabia","206.2K","+1","Fashion",3),("Rituals Cosmetics","Saudi Arabia","98.5K","+2","Beauty",4),
]

CLIENTS = [
 ("odachi","Restaurant"),("Nawader Aloud","Perfume"),("Crocs","Fashion"),("BHPC KSA","Fashion"),
 ("Urth Caffe","Cafe"),("Morini Riyadh","Restaurant"),("Rüya","Restaurant"),("Beefbar","Restaurant"),
 ("ROKA KSA","Restaurant"),("The Beauty Secrets","Beauty"),("Swaikhat & Tanoor","Restaurant"),("The Back Burner","Restaurant"),
 ("Maryool","Restaurant"),("Coya","Restaurant"),("A.O.K Kitchen","Restaurant"),("elct.sa","Fashion"),
 ("Opt Coffee KW","Cafe"),("ROBATA","Restaurant"),("Signor Sassi","Restaurant"),("San Carlo","Restaurant"),
 ("MYAZŪ","Restaurant"),("Agio","Restaurant"),("Beit El Sabban","Restaurant"),("Vero Moda","Fashion"),
 ("Enigmaku","Fashion"),("Clap","Restaurant"),("Jones the Grocer","Cafe"),("Iris","Restaurant"),
 ("Brute","Restaurant"),("Bagatelle","Restaurant"),("Sumosan","Restaurant"),("MNKY HSE","Restaurant"),
 ("Tashas Cafe","Cafe"),("Solitaire","Fashion"),("Panerai","Fashion"),("Fred","Fashion"),
 ("Kiko","Beauty"),("Maje","Fashion"),("Ted Baker","Fashion"),("TAG Heuer","Fashion"),
 ("Nicoli",""),("Skechers",""),("Dani by Daniel K",""),("Rituals Cosmetics",""),
 ("Rowleys",""),("Saiddal",""),("Keycafe",""),("DayDayGame",""),
 ("Jadeel",""),("Crêpes des Alpes",""),("Flamingo Room",""),("Splash Spectrum",""),
 ("MAREEZ",""),("Pizza Bar",""),("tabl.to",""),("Brunch & Cake",""),
 ("Hamra Tower",""),("Zuma",""),("Mr.Chow",""),("KAYZŌ",""),
 ("Il Baretto",""),("Crazy Pizza",""),("St. Regis Hotels",""),("Gia",""),
 ("Black Tap",""),("Sobhy Kaber",""),("Jon & Vinny's",""),("Million Riyal Menu",""),
 ("ISISPHARMA",""),("Lina's & Dina's",""),("ShieldMe",""),("Maserati",""),
 ("Tom Tom Coffee",""),("Mana",""),("Lavenue","Restaurant"),
]

WHY = [
 ("Decade of excellence","With over 10 years of experience in the industry, Elite brings a wealth of knowledge and expertise to every campaign we undertake."),
 ("Global reach","Our presence in over 52 countries enables us to connect brands with influencers and audiences on a global scale, ensuring maximum reach and impact."),
 ("Elite partnerships","We pride ourselves on our exclusive partnerships with high-end brands and elite influencers, ensuring that our clients have access to the best talent and opportunities worldwide."),
 ("Measurable results","We're committed to delivering measurable results that drive real business growth and ROI for our clients, no matter where they are in the world."),
 ("Exceptional quality","From campaign conception to execution, we maintain the highest standards of quality and professionalism in everything we do."),
]

# ── EN pages ──
def cases_body():
    cards = build_stories.cards()
    feature = build_stories.reel()
    chips = build_stories.chips()
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">SUCCESS IN ACTION</p><h1>Stories From Our Clients</h1>
    <p class="lede">Real campaigns, real creators, real numbers. Filter by category to find work close to yours.</p>
  </div></section>{feature}
  <section class="sec sec--tight"><div class="wrap">
    <div class="search-row reveal">
      <input class="search-input" id="story-search" type="search" placeholder="Search stories…" data-search="#story-list" aria-label="Search success stories">
      <div class="chips" data-filter-group data-filter-target="#story-list" data-filter-empty="#story-empty">{chips}</div>
    </div>
    <div class="dcard-grid mt-8" id="story-list">{cards}</div>
    <div class="state mt-8" id="story-empty" hidden>
      <h3>No stories in this category yet</h3><p>Try another filter, or tell us what you're looking for and we'll share relevant work directly.</p>
    </div>
    <div class="state mt-8" data-search-empty hidden>
      <h3>Nothing matched that search</h3><p>Check the spelling, or clear the search to see every story.</p>
    </div>
    <div class="center mt-12 reveal"><a class="btn btn-ghost" href="contacts.html">Get a campaign like these <span class="arrow" aria-hidden="true">→</span></a></div>
  </div></section>
  <section class="sec sec--sunken"><div class="wrap">
    <div class="sec-head sec-head--center reveal"><p class="eyebrow">Questions</p><h2 class="sec-title">How a campaign runs.</h2></div>
    <div class="acc mt-8" data-single>
      <div class="acc__item" data-open="false">
        <button class="acc__trigger" type="button">How do you pick the creators?<span class="acc__icon" aria-hidden="true"></span></button>
        <div class="acc__panel"><div class="acc__panel-in">We shortlist from our network based on genuine audience overlap with your brand — market, category, age profile and engagement quality — not follower count alone.</div></div>
      </div>
      <div class="acc__item" data-open="false">
        <button class="acc__trigger" type="button">How long does a campaign take?<span class="acc__icon" aria-hidden="true"></span></button>
        <div class="acc__panel"><div class="acc__panel-in">It depends on scope and market, but most campaigns move from brief to first published content within a few weeks. We'll give you a schedule before anything is signed.</div></div>
      </div>
      <div class="acc__item" data-open="false">
        <button class="acc__trigger" type="button">What do you report back?<span class="acc__icon" aria-hidden="true"></span></button>
        <div class="acc__panel"><div class="acc__panel-in">Coverage by creator and format — stories, posts and video — plus reach and campaign-level performance, all visible live in the Elite dashboard.</div></div>
      </div>
      <div class="acc__item" data-open="false">
        <button class="acc__trigger" type="button">Which markets do you cover?<span class="acc__icon" aria-hidden="true"></span></button>
        <div class="acc__panel"><div class="acc__panel-in">Elite has a presence in more than 52 countries, with the deepest creator networks across Saudi Arabia, Kuwait, the UAE, Qatar and Bahrain.</div></div>
      </div>
    </div>
  </div></section>
</main>"""

def sponsors_body():
    cells = "".join(f'<span class="logo-cell-grid" data-cat="{c}" data-name="{n}">{n}</span>' for n,c in CLIENTS)
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">OUR CLIENTS</p><h1>Seventy-five brands. Seven markets.</h1>
    <p class="lede">Seventy-five brands across seven countries and twelve categories choose Elite to reach their audience.</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="kpi-grid reveal">
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">Featured clients</span><span class="kpi__icon">◈</span></div><span class="kpi__value" data-count="75">75</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">Countries</span><span class="kpi__icon">◉</span></div><span class="kpi__value" data-count="7">7</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">Categories</span><span class="kpi__icon">▦</span></div><span class="kpi__value" data-count="12">12</span></div>
    </div>
    <div class="proof mt-8">
      <div class="card reveal"><h3 class="h4">Clients by category</h3>
        <div class="meters mt-6">
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Restaurant</span><span class="meter-val">58.82%</span></div><div class="meter-bar"><i class="meter-fill" data-w="100"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Fashion</span><span class="meter-val">10.29%</span></div><div class="meter-bar"><i class="meter-fill" data-w="17.5"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Café</span><span class="meter-val">10.29%</span></div><div class="meter-bar"><i class="meter-fill" data-w="17.5"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Perfume</span><span class="meter-val">4.41%</span></div><div class="meter-bar"><i class="meter-fill" data-w="7.5"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Cosmetics / Beauty</span><span class="meter-val">2.94%</span></div><div class="meter-bar"><i class="meter-fill" data-w="5"></i></div></div>
        </div>
      </div>
      <div class="card reveal" style="transition-delay:.1s"><h3 class="h4">Clients by region</h3>
        <div class="meters mt-6">
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Saudi Arabia</span><span class="meter-val">71.74%</span></div><div class="meter-bar"><i class="meter-fill" data-w="100"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Kuwait</span><span class="meter-val">15.22%</span></div><div class="meter-bar"><i class="meter-fill" data-w="21.2"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">United Arab Emirates</span><span class="meter-val">4.35%</span></div><div class="meter-bar"><i class="meter-fill" data-w="6.1"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Qatar</span><span class="meter-val">4.35%</span></div><div class="meter-bar"><i class="meter-fill" data-w="6.1"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">Bahrain</span><span class="meter-val">2.17%</span></div><div class="meter-bar"><i class="meter-fill" data-w="3"></i></div></div>
        </div>
      </div>
    </div>
  </div></section>
  <section class="sec sec--sunken"><div class="wrap">
    <div class="search-row reveal">
      <div class="sec-head" style="margin:0"><p class="eyebrow">The roster</p><h2 class="sec-title mt-4">Brands we work with.</h2></div>
      <input class="search-input" id="client-search" type="search" placeholder="Search clients…" data-search="#client-list" aria-label="Search clients">
    </div>
    <div class="chips mt-8 reveal" data-filter-group data-filter-target="#client-list" data-filter-empty="#client-empty">
      <button class="chip-toggle" type="button" data-value="all" aria-pressed="true">All <span class="count">{len(CLIENTS)}</span></button>
      <button class="chip-toggle" type="button" data-value="Restaurant" aria-pressed="false">Restaurant</button>
      <button class="chip-toggle" type="button" data-value="Cafe" aria-pressed="false">Café</button>
      <button class="chip-toggle" type="button" data-value="Fashion" aria-pressed="false">Fashion</button>
      <button class="chip-toggle" type="button" data-value="Beauty" aria-pressed="false">Cosmetics / Beauty</button>
      <button class="chip-toggle" type="button" data-value="Perfume" aria-pressed="false">Perfume</button>
    </div>
    <div class="logo-grid mt-8 reveal" id="client-list">{cells}</div>
    <div class="state mt-8" id="client-empty" hidden><h3>No clients in this category yet</h3><p>Pick another category to keep browsing.</p></div>
    <div class="state mt-8" data-search-empty hidden><h3>No match for that name</h3><p>Clear the search to see the full roster.</p></div>
    <p class="center subtle mt-10">Showing all {len(CLIENTS)} clients</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="cta"><div class="wrap cta-in"><h2 class="cta-title">Your brand belongs here.</h2><p class="cta-lede">Join seventy-five brands running influencer campaigns with Elite across the Gulf and beyond.</p><a class="btn btn-gold" href="contacts.html">Become a client <span class="arrow" aria-hidden="true">→</span></a></div></div>
  </div></section>
</main>"""

def contacts_body():
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">CONTACT US</p><h1>Tell us what you want to launch.</h1>
    <p class="lede">Stay connected with us! Whether you have a question, suggestion, or just want to say hello, we're here to help. Don't hesitate to reach out — we'd love to hear from you.</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="split split--form">
      <div class="card reveal">
        <div class="segmented" role="tablist" aria-label="I am a">
          <button role="tab" id="tab-inf" aria-controls="panel-inf" aria-selected="true" type="button">Influencer</button>
          <button role="tab" id="tab-brand" aria-controls="panel-brand" aria-selected="false" tabindex="-1" type="button">Brand</button>
        </div>
        <div id="panel-inf" role="tabpanel" aria-labelledby="tab-inf">
          <p class="muted mt-6">Join the Elite network and work with the region's premium brands.</p>
          <form class="form-grid mt-6" data-validate data-success="Thanks — an Elite partner manager will be in touch.">
            <div class="field"><label class="field__label" for="i-name">Name <span class="req">*</span></label><input class="input" id="i-name" name="name" required placeholder="Your full name"><span class="field__error">Please enter your name.</span></div>
            <div class="field"><label class="field__label" for="i-country">Country</label><select class="select" id="i-country" name="country"><option value="">Select country</option><option>Saudi Arabia</option><option>Kuwait</option><option>United Arab Emirates</option><option>Qatar</option><option>Bahrain</option><option>Egypt</option><option>Other</option></select></div>
            <div class="field"><label class="field__label" for="i-email">Email <span class="req">*</span></label><input class="input" id="i-email" name="email" type="email" required placeholder="you@example.com"><span class="field__error">Enter a valid email address, like name@company.com.</span></div>
            <div class="field"><label class="field__label" for="i-phone">Phone number</label><input class="input" id="i-phone" name="phone" type="tel" placeholder="+966 …"></div>
            <div class="field--full"><label class="check"><input type="checkbox" name="whatsapp" checked><span>WhatsApp is active on this number</span></label></div>
            <div class="field field--full"><label class="field__label" for="i-msg">Message</label><textarea class="textarea" id="i-msg" name="message" placeholder="Tell us about your audience and the brands you'd like to work with."></textarea></div>
            <div class="field--full"><button class="btn btn-gold btn-block" type="submit">Send message</button></div>
          </form>
        </div>
        <div id="panel-brand" role="tabpanel" aria-labelledby="tab-brand" hidden>
          <p class="muted mt-6">Tell us the goal and we'll come back with creators, a plan and a budget.</p>
          <form class="form-grid mt-6" data-validate data-success="Thanks — we'll reply with a campaign outline shortly.">
            <div class="field"><label class="field__label" for="b-name">Name <span class="req">*</span></label><input class="input" id="b-name" name="name" required placeholder="Your full name"><span class="field__error">Please enter your name.</span></div>
            <div class="field"><label class="field__label" for="b-brand">Brand <span class="req">*</span></label><input class="input" id="b-brand" name="brand" required placeholder="Brand name"><span class="field__error">Please enter your brand.</span></div>
            <div class="field"><label class="field__label" for="b-email">Email <span class="req">*</span></label><input class="input" id="b-email" name="email" type="email" required placeholder="you@company.com"><span class="field__error">Enter a valid email address, like name@company.com.</span></div>
            <div class="field"><label class="field__label" for="b-country">Country</label><select class="select" id="b-country" name="country"><option value="">Select country</option><option>Saudi Arabia</option><option>Kuwait</option><option>United Arab Emirates</option><option>Qatar</option><option>Bahrain</option><option>Egypt</option><option>Other</option></select></div>
            <div class="field"><label class="field__label" for="b-phone">Phone number</label><input class="input" id="b-phone" name="phone" type="tel" placeholder="+966 …"></div>
            <div class="field"><label class="field__label" for="b-cat">Category</label><select class="select" id="b-cat" name="category"><option value="">Select category</option><option>Restaurant</option><option>Café</option><option>Fashion</option><option>Cosmetics / Beauty</option><option>Perfume</option><option>Hotel</option><option>Other</option></select></div>
            <div class="field--full"><label class="check"><input type="checkbox" name="whatsapp" checked><span>WhatsApp is active on this number</span></label></div>
            <div class="field field--full"><label class="field__label" for="b-msg">Message</label><textarea class="textarea" id="b-msg" name="message" placeholder="What are you launching, and what does success look like?"></textarea></div>
            <div class="field--full"><button class="btn btn-gold btn-block" type="submit">Send message</button></div>
          </form>
        </div>
      </div>
      <aside class="stack reveal" style="transition-delay:.1s">
        <div class="card card--sunken"><h3 class="h4">What happens next</h3>
          <ol class="stack mt-6">
            <li class="muted"><b class="gold">1 —</b> We read your brief and check creator fit.</li>
            <li class="muted"><b class="gold">2 —</b> You get a shortlist, a plan and a budget.</li>
            <li class="muted"><b class="gold">3 —</b> We run the campaign and report live.</li>
          </ol>
        </div>
        <div class="card card--sunken"><h3 class="h4">Where we work</h3><p class="muted mt-4">Saudi Arabia · Kuwait · United Arab Emirates · Qatar · Bahrain — and 52+ countries worldwide.</p></div>
        <div class="card card--sunken"><h3 class="h4">24/7 live support</h3><p class="muted mt-4">Campaigns don't keep office hours. Neither do we.</p></div>
      </aside>
    </div>
  </div></section>
</main>"""

def about_body():
    cards = "".join(f'<div class="why-item"><h3>{t}</h3><p>{c}</p></div>' for t,c in WHY)
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">ABOUT US</p><h1>Ten years putting brands in the right feeds.</h1>
    <p class="lede">Your premier destination for cutting-edge influencer marketing solutions.</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="split">
      <div class="split__media split__media--logo reveal"><img src="assets/img/elite-logo.svg" alt="Elite — Niche Mastery Redefined" width="572" height="232" loading="lazy" decoding="async"></div>
      <div class="reveal" style="transition-delay:.1s">
        <p class="eyebrow">Who we are</p>
        <h2 class="sec-title mt-4">A decade of influence, in more than 52 countries.</h2>
        <p class="lede mt-6">Welcome to Elite. With over a decade of experience in the industry and a global presence spanning more than 52 countries, Elite has established itself as a trusted leader in the world of influencer marketing. Our extensive experience and international reach empower us to deliver unparalleled results for brands seeking to maximize their impact on a global scale.</p>
        <div class="stat-grid mt-8">
          <div class="stat"><span class="stat__value" data-count="10">10</span><span class="stat__label">Years</span></div>
          <div class="stat"><span class="stat__value" data-count="52">52</span><span class="stat__label">Countries</span></div>
          <div class="stat"><span class="stat__value" data-count="50" data-suffix="B">50B</span><span class="stat__label">Follower reach</span></div>
          <div class="stat"><span class="stat__value" data-count="85" data-suffix="K">85K</span><span class="stat__label">Creators</span></div>
          <div class="stat"><span class="stat__value" data-count="1500">1500</span><span class="stat__label">Brands served</span></div>
        </div>
      </div>
    </div>
  </div></section>
  <section class="sec sec--sunken"><div class="wrap">
    <div class="proof">
      <div class="reveal"><p class="eyebrow">Our mission</p><h2 class="sec-title mt-4">Simple, yet powerful.</h2><p class="lede mt-6">To empower brands with tailored influencer marketing strategies that amplify their message and drive tangible results. We are committed to leveraging our decade-long expertise and global network to create impactful campaigns that resonate with audiences around the world.</p></div>
      <div class="reveal" style="transition-delay:.1s"><p class="eyebrow">What sets us apart</p><h2 class="sec-title mt-4">Exceptional strategies.</h2><p class="lede mt-6">At Elite, we understand that exceptional results require exceptional strategies. That's why we've spent over 10 years cultivating relationships with elite influencers and high-end brands, ensuring that our clients have access to the best talent and opportunities across the globe — bespoke campaigns that transcend borders and resonate with diverse audiences.</p></div>
    </div>
  </div></section>
  <section class="sec"><div class="wrap">
    <div class="sec-head sec-head--center reveal"><p class="eyebrow">Why choose Elite</p><h2 class="sec-title">Five reasons brands stay.</h2></div>
    <div class="why reveal mt-8">{cards}</div>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="cta"><div class="wrap cta-in"><p class="eyebrow">Get in touch</p><h2 class="cta-title">Let's talk about your next campaign.</h2><p class="cta-lede">Ready to elevate your brand with the power of influencer marketing on a global scale? Get in touch today to learn more about our services and how we can help you achieve your marketing goals.</p><a class="btn btn-gold" href="contacts.html">Contact us <span class="arrow" aria-hidden="true">→</span></a></div></div>
  </div></section>
</main>"""

page("case-studies.html","Success Stories — Elite","Success in action: influencer campaigns Elite has run for premium brands, with reach and creator counts.",cases_body())
page("sponsors.html","Our Clients — Elite","Seventy-five brands across seven countries and twelve categories partner with Elite for influencer marketing.",sponsors_body())
page("contacts.html","Contact Us — Elite","Talk to Elite about an influencer campaign, or join the network as a creator. 24/7 live support.",contacts_body())
page("about.html","About Us — Elite","Over a decade of influencer marketing across more than 52 countries. Elite's mission, approach and reasons brands stay.",about_body())

# ── AR pages (same structure, translated copy) ──
def cases_body_ar():
    cards = build_stories.cards(ar=True)
    feature = build_stories.reel(ar=True)
    chips = build_stories.chips(ar=True)
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">نجاحٌ في الواقع</p><h1>قصص عملائنا</h1>
    <p class="lede">حملات حقيقية، صنّاع محتوى حقيقيون، وأرقام حقيقية. صفِّ حسب الفئة لتجد عملاً قريباً من مجالك.</p>
  </div></section>{feature}
  <section class="sec sec--tight"><div class="wrap">
    <div class="search-row reveal">
      <input class="search-input" id="story-search" type="search" placeholder="ابحث في القصص…" data-search="#story-list" aria-label="ابحث في قصص النجاح">
      <div class="chips" data-filter-group data-filter-target="#story-list" data-filter-empty="#story-empty">{chips}</div>
    </div>
    <div class="dcard-grid mt-8" id="story-list">{cards}</div>
    <div class="state mt-8" id="story-empty" hidden><h3>لا توجد قصص في هذه الفئة بعد</h3><p>جرّب فلتراً آخر، أو أخبرنا بما تبحث عنه وسنشاركك عملاً ذا صلة مباشرة.</p></div>
    <div class="state mt-8" data-search-empty hidden><h3>لا نتائج مطابقة</h3><p>تحقّق من الإملاء، أو امسح البحث لرؤية كل القصص.</p></div>
    <div class="center mt-12 reveal"><a class="btn btn-ghost" href="contacts.html">احصل على حملة كهذه <span class="arrow" aria-hidden="true">→</span></a></div>
  </div></section>
  <section class="sec sec--sunken"><div class="wrap">
    <div class="sec-head sec-head--center reveal"><p class="eyebrow">أسئلة</p><h2 class="sec-title">كيف تجري الحملة.</h2></div>
    <div class="acc mt-8" data-single>
      <div class="acc__item" data-open="false"><button class="acc__trigger" type="button">كيف تختارون صنّاع المحتوى؟<span class="acc__icon" aria-hidden="true"></span></button><div class="acc__panel"><div class="acc__panel-in">نرشّح من شبكتنا بناءً على تداخل حقيقي بين جمهور المؤثر وعلامتك — السوق، الفئة، الشريحة العمرية وجودة التفاعل — لا عدد المتابعين وحده.</div></div></div>
      <div class="acc__item" data-open="false"><button class="acc__trigger" type="button">كم تستغرق الحملة؟<span class="acc__icon" aria-hidden="true"></span></button><div class="acc__panel"><div class="acc__panel-in">يعتمد على النطاق والسوق، لكن معظم الحملات تنتقل من الموجز إلى أول محتوى منشور خلال أسابيع معدودة. سنزوّدك بجدول زمني قبل أي توقيع.</div></div></div>
      <div class="acc__item" data-open="false"><button class="acc__trigger" type="button">ماذا تقدّمون من تقارير؟<span class="acc__icon" aria-hidden="true"></span></button><div class="acc__panel"><div class="acc__panel-in">تغطية حسب المؤثر والصيغة — ستوريز، منشورات وفيديو — إضافة إلى الوصول والأداء على مستوى الحملة، كلّها مرئية مباشرة في مساحة عمل إيليت.</div></div></div>
      <div class="acc__item" data-open="false"><button class="acc__trigger" type="button">ما الأسواق التي تغطّونها؟<span class="acc__icon" aria-hidden="true"></span></button><div class="acc__panel"><div class="acc__panel-in">حضور إيليت في أكثر من 52 دولة، مع أعمق شبكات صنّاع المحتوى عبر السعودية والكويت والإمارات وقطر والبحرين.</div></div></div>
    </div>
  </div></section>
</main>"""

def sponsors_body_ar():
    cells = "".join(f'<span class="logo-cell-grid" data-cat="{c}" data-name="{n}">{n}</span>' for n,c in CLIENTS)
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">عملاؤنا</p><h1>75 علامة تجارية. 7 أسواق.</h1>
    <p class="lede">75 علامة تجارية في 7 دول و12 فئة اختارت إيليت للوصول إلى جمهورها.</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="kpi-grid reveal">
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">عملاء مميّزون</span><span class="kpi__icon">◈</span></div><span class="kpi__value" data-count="75">75</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">الدول</span><span class="kpi__icon">◉</span></div><span class="kpi__value" data-count="7">7</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">الفئات</span><span class="kpi__icon">▦</span></div><span class="kpi__value" data-count="12">12</span></div>
    </div>
    <div class="proof mt-8">
      <div class="card reveal"><h3 class="h4">العملاء حسب الفئة</h3>
        <div class="meters mt-6">
          <div class="meter-row"><div class="meter-top"><span class="meter-name">مطاعم</span><span class="meter-val">58.82%</span></div><div class="meter-bar"><i class="meter-fill" data-w="100"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">أزياء</span><span class="meter-val">10.29%</span></div><div class="meter-bar"><i class="meter-fill" data-w="17.5"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">مقاهٍ</span><span class="meter-val">10.29%</span></div><div class="meter-bar"><i class="meter-fill" data-w="17.5"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">عطور</span><span class="meter-val">4.41%</span></div><div class="meter-bar"><i class="meter-fill" data-w="7.5"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">تجميل</span><span class="meter-val">2.94%</span></div><div class="meter-bar"><i class="meter-fill" data-w="5"></i></div></div>
        </div>
      </div>
      <div class="card reveal" style="transition-delay:.1s"><h3 class="h4">العملاء حسب المنطقة</h3>
        <div class="meters mt-6">
          <div class="meter-row"><div class="meter-top"><span class="meter-name">السعودية</span><span class="meter-val">71.74%</span></div><div class="meter-bar"><i class="meter-fill" data-w="100"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">الكويت</span><span class="meter-val">15.22%</span></div><div class="meter-bar"><i class="meter-fill" data-w="21.2"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">الإمارات</span><span class="meter-val">4.35%</span></div><div class="meter-bar"><i class="meter-fill" data-w="6.1"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">قطر</span><span class="meter-val">4.35%</span></div><div class="meter-bar"><i class="meter-fill" data-w="6.1"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">البحرين</span><span class="meter-val">2.17%</span></div><div class="meter-bar"><i class="meter-fill" data-w="3"></i></div></div>
        </div>
      </div>
    </div>
  </div></section>
  <section class="sec sec--sunken"><div class="wrap">
    <div class="search-row reveal">
      <div class="sec-head" style="margin:0"><p class="eyebrow">القائمة</p><h2 class="sec-title mt-4">العلامات التي نعمل معها.</h2></div>
      <input class="search-input" id="client-search" type="search" placeholder="ابحث في العملاء…" data-search="#client-list" aria-label="ابحث في العملاء">
    </div>
    <div class="chips mt-8 reveal" data-filter-group data-filter-target="#client-list" data-filter-empty="#client-empty">
      <button class="chip-toggle" type="button" data-value="all" aria-pressed="true">الكل <span class="count">{len(CLIENTS)}</span></button>
      <button class="chip-toggle" type="button" data-value="Restaurant" aria-pressed="false">مطاعم</button>
      <button class="chip-toggle" type="button" data-value="Cafe" aria-pressed="false">مقاهٍ</button>
      <button class="chip-toggle" type="button" data-value="Fashion" aria-pressed="false">أزياء</button>
      <button class="chip-toggle" type="button" data-value="Beauty" aria-pressed="false">تجميل</button>
      <button class="chip-toggle" type="button" data-value="Perfume" aria-pressed="false">عطور</button>
    </div>
    <div class="logo-grid mt-8 reveal" id="client-list">{cells}</div>
    <div class="state mt-8" id="client-empty" hidden><h3>لا عملاء في هذه الفئة بعد</h3><p>اختر فئة أخرى لمواصلة التصفّح.</p></div>
    <div class="state mt-8" data-search-empty hidden><h3>لا تطابق للاسم</h3><p>امسح البحث لرؤية القائمة كاملة.</p></div>
    <p class="center subtle mt-10">عرض جميع العملاء الـ{len(CLIENTS)}</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="cta"><div class="wrap cta-in"><h2 class="cta-title">علامتك تنتمي إلى هنا.</h2><p class="cta-lede">انضم إلى 75 علامة تجارية تدير حملات المؤثرين مع إيليت في الخليج وخارجه.</p><a class="btn btn-gold" href="contacts.html">كن عميلاً <span class="arrow" aria-hidden="true">→</span></a></div></div>
  </div></section>
</main>"""

def contacts_body_ar():
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">تواصل معنا</p><h1>أخبرنا بما تريد إطلاقه.</h1>
    <p class="lede">سؤال، أو فكرة حملة، أو رغبة في الانضمام إلى الشبكة — اكتب لنا، ويصلك ردّ من شخص حقيقي.</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="split split--form">
      <div class="card reveal">
        <div class="segmented" role="tablist" aria-label="أنا صانع محتوى أو علامة تجارية">
          <button role="tab" id="tab-inf" aria-controls="panel-inf" aria-selected="true" type="button">صانع محتوى</button>
          <button role="tab" id="tab-brand" aria-controls="panel-brand" aria-selected="false" tabindex="-1" type="button">علامة تجارية</button>
        </div>
        <div id="panel-inf" role="tabpanel" aria-labelledby="tab-inf">
          <p class="muted mt-6">انضم إلى شبكة إيليت واعمل مع أرقى العلامات في المنطقة.</p>
          <form class="form-grid mt-6" data-validate data-success="شكراً — سيتواصل معك مدير شراكات إيليت.">
            <div class="field"><label class="field__label" for="i-name">الاسم <span class="req">*</span></label><input class="input" id="i-name" name="name" required placeholder="اسمك الكامل"><span class="field__error">يرجى إدخال اسمك.</span></div>
            <div class="field"><label class="field__label" for="i-country">الدولة</label><select class="select" id="i-country" name="country"><option value="">اختر الدولة</option><option>السعودية</option><option>الكويت</option><option>الإمارات</option><option>قطر</option><option>البحرين</option><option>مصر</option><option>أخرى</option></select></div>
            <div class="field"><label class="field__label" for="i-email">البريد <span class="req">*</span></label><input class="input" id="i-email" name="email" type="email" required placeholder="you@example.com"><span class="field__error">أدخل بريدًا إلكترونيًا صحيحًا، مثل <bdi>name@company.com</bdi></span></div>
            <div class="field"><label class="field__label" for="i-phone">الهاتف</label><input class="input" id="i-phone" name="phone" type="tel" placeholder="+966 …"></div>
            <div class="field--full"><label class="check"><input type="checkbox" name="whatsapp" checked><span>واتساب فعّال على هذا الرقم</span></label></div>
            <div class="field field--full"><label class="field__label" for="i-msg">رسالة</label><textarea class="textarea" id="i-msg" name="message" placeholder="أخبرنا عن جمهورك والعلامات التي تود العمل معها."></textarea></div>
            <div class="field--full"><button class="btn btn-gold btn-block" type="submit">إرسال</button></div>
          </form>
        </div>
        <div id="panel-brand" role="tabpanel" aria-labelledby="tab-brand" hidden>
          <p class="muted mt-6">أخبرنا بالهدف وسنعود بصنّاع محتوى وخطة وميزانية.</p>
          <form class="form-grid mt-6" data-validate data-success="شكراً — سنرد بمخطط حملة قريباً.">
            <div class="field"><label class="field__label" for="b-name">الاسم <span class="req">*</span></label><input class="input" id="b-name" name="name" required placeholder="اسمك الكامل"><span class="field__error">يرجى إدخال اسمك.</span></div>
            <div class="field"><label class="field__label" for="b-brand">العلامة <span class="req">*</span></label><input class="input" id="b-brand" name="brand" required placeholder="اسم العلامة"><span class="field__error">يرجى إدخال علامتك.</span></div>
            <div class="field"><label class="field__label" for="b-email">البريد <span class="req">*</span></label><input class="input" id="b-email" name="email" type="email" required placeholder="you@company.com"><span class="field__error">أدخل بريدًا إلكترونيًا صحيحًا، مثل <bdi>name@company.com</bdi></span></div>
            <div class="field"><label class="field__label" for="b-country">الدولة</label><select class="select" id="b-country" name="country"><option value="">اختر الدولة</option><option>السعودية</option><option>الكويت</option><option>الإمارات</option><option>قطر</option><option>البحرين</option><option>مصر</option><option>أخرى</option></select></div>
            <div class="field"><label class="field__label" for="b-phone">الهاتف</label><input class="input" id="b-phone" name="phone" type="tel" placeholder="+966 …"></div>
            <div class="field"><label class="field__label" for="b-cat">الفئة</label><select class="select" id="b-cat" name="category"><option value="">اختر الفئة</option><option>مطاعم</option><option>مقاهٍ</option><option>أزياء</option><option>تجميل</option><option>عطور</option><option>فندقة</option><option>أخرى</option></select></div>
            <div class="field--full"><label class="check"><input type="checkbox" name="whatsapp" checked><span>واتساب فعّال على هذا الرقم</span></label></div>
            <div class="field field--full"><label class="field__label" for="b-msg">رسالة</label><textarea class="textarea" id="b-msg" name="message" placeholder="ماذا تطلق، وما الشكل الذي يبدو عليه النجاح؟"></textarea></div>
            <div class="field--full"><button class="btn btn-gold btn-block" type="submit">إرسال</button></div>
          </form>
        </div>
      </div>
      <aside class="stack reveal" style="transition-delay:.1s">
        <div class="card card--sunken"><h3 class="h4">ما الخطوات التالية</h3>
          <ol class="stack mt-6">
            <li class="muted"><b class="gold">1 —</b> نقرأ موجزك ونتحقق من ملاءمة المؤثر.</li>
            <li class="muted"><b class="gold">2 —</b> تحصل على قائمة مختصرة وخطة وميزانية.</li>
            <li class="muted"><b class="gold">3 —</b> ندير الحملة ونقدّم التقارير مباشرة.</li>
          </ol>
        </div>
        <div class="card card--sunken"><h3 class="h4">أين نعمل</h3><p class="muted mt-4">السعودية · الكويت · الإمارات · قطر · البحرين — وأكثر من 52 دولة حول العالم.</p></div>
        <div class="card card--sunken"><h3 class="h4">دعم مباشر على مدار الساعة</h3><p class="muted mt-4">الحملات لا تتوقّف عند نهاية الدوام، ولا نحن.</p></div>
      </aside>
    </div>
  </div></section>
</main>"""

def about_body_ar():
    WHY_AR = [
      ("عقد من التميّز","أكثر من عشر سنوات في المجال: تدخل إيليت كل حملة بخبرة متراكمة ومعرفة بالسوق."),
      ("انتشار عالمي","حضورنا في أكثر من 52 دولة يصل بعلامتك إلى الجمهور المناسب أينما كان."),
      ("شراكات مميّزة","علاقات حصرية مع صنّاع المحتوى ومع العلامات الفاخرة تفتح لك أبوابًا لا يصل إليها غيرك."),
      ("نتائج قابلة للقياس","نتتبّع كل حملة من أولها إلى آخرها، فترى النموّ بعينك لا في وعودٍ تُقال لك."),
      ("جودة استثنائية","من فكرة الحملة إلى تنفيذها، نلتزم بأعلى معايير الجودة والاحترافية."),
    ]
    cards = "".join(f'<div class="why-item"><h3>{t}</h3><p>{c}</p></div>' for t,c in WHY_AR)
    return f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">من نحن</p><h1>عشر سنوات نضع العلامات أمام الجمهور الصحيح.</h1>
    <p class="lede">وجهتك الأولى لحلول التسويق عبر المؤثرين المتطورة.</p>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="split">
      <div class="split__media split__media--logo reveal"><img src="../assets/img/elite-logo.svg" alt="إيليت — إتقانٌ يُعيد تعريف التميّز" width="572" height="232" loading="lazy" decoding="async"></div>
      <div class="reveal" style="transition-delay:.1s">
        <p class="eyebrow">من نحن</p>
        <h2 class="sec-title mt-4">عقد من التأثير، في أكثر من 52 دولة.</h2>
        <p class="lede mt-6">أكثر من عشر سنوات في التسويق عبر المؤثرين، وحضور في أكثر من 52 دولة. هذا ما يتيح لنا أن نصل بعلامتك إلى الجمهور الصحيح في السوق الصحيح، ثم نُثبت لك ما حققته الحملة بالأرقام.</p>
        <div class="stat-grid mt-8">
          <div class="stat"><span class="stat__value" data-count="10">10</span><span class="stat__label">سنوات</span></div>
          <div class="stat"><span class="stat__value" data-count="52">52</span><span class="stat__label">دولة</span></div>
          <div class="stat"><span class="stat__value" data-count="50" data-suffix=" مليار">50 مليار</span><span class="stat__label">إجمالي المتابعين</span></div>
          <div class="stat"><span class="stat__value" data-count="85" data-suffix=" ألف">85 ألف</span><span class="stat__label">صانع محتوى</span></div>
          <div class="stat"><span class="stat__value" data-count="1500">1500</span><span class="stat__label">علامة تجارية</span></div>
        </div>
      </div>
    </div>
  </div></section>
  <section class="sec sec--sunken"><div class="wrap">
    <div class="proof">
      <div class="reveal"><p class="eyebrow">رسالتنا</p><h2 class="sec-title mt-4">بسيطة، لكنها قوية.</h2><p class="lede mt-6">أن نوصل رسالة كل علامة إلى من يهمّه سماعها فعلًا — بخطة مبنية على شبكتنا وخبرتنا، ونتائج تُقاس لا تُوصف.</p></div>
      <div class="reveal" style="transition-delay:.1s"><p class="eyebrow">ما يميّزنا</p><h2 class="sec-title mt-4">استراتيجيات استثنائية.</h2><p class="lede mt-6">أمضينا أكثر من عشر سنوات نبني علاقات مع صنّاع المحتوى ومع العلامات الفاخرة. تلك العلاقات هي ما يجعل حملتك تبدأ من قائمة أسماء جاهزة، لا من الصفر.</p></div>
    </div>
  </div></section>
  <section class="sec"><div class="wrap">
    <div class="sec-head sec-head--center reveal"><p class="eyebrow">لماذا إيليت</p><h2 class="sec-title">خمسة أسباب تبقى العلامات معنا.</h2></div>
    <div class="why reveal mt-8">{cards}</div>
  </div></section>
  <section class="sec sec--tight"><div class="wrap">
    <div class="cta"><div class="wrap cta-in"><p class="eyebrow">تواصل معنا</p><h2 class="cta-title">لنتحدّث عن حملتك القادمة.</h2><p class="cta-lede">أخبرنا بما تريد إطلاقه، وسنعود إليك بصنّاع المحتوى والخطة والأرقام. عادةً خلال يومين.</p><a class="btn btn-gold" href="contacts.html">تواصل معنا <span class="arrow" aria-hidden="true">→</span></a></div></div>
  </div></section>
</main>"""

page("ar/case-studies.html","قصص النجاح — إيليت","نجاحٌ في الواقع: حملات المؤثرين التي أطلقتها إيليت لعلامات راقية، مع أرقام الوصول وعدد صنّاع المحتوى.",cases_body_ar(),ar=True)
page("ar/sponsors.html","عملاؤنا — إيليت","خمس وسبعون علامة عبر سبع دول واثنتا عشرة فئة تتشارك مع إيليت في التسويق عبر المؤثرين.",sponsors_body_ar(),ar=True)
page("ar/contacts.html","تواصل معنا — إيليت","تحدّث إلى إيليت عن حملة مؤثرين، أو انضم إلى الشبكة كصانع محتوى. دعم مباشر على مدار الساعة.",contacts_body_ar(),ar=True)
page("ar/about.html","من نحن — إيليت","أكثر من عقد من التسويق عبر المؤثرين عبر أكثر من 52 دولة. رسالة إيليت ومنهجها وأسباب بقاء العلامات.",about_body_ar(),ar=True)

print("DONE")