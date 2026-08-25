# -*- coding: utf-8 -*-
"""Generates the Arabic index.html and dashboard.html (the two pages built by hand in EN)."""
import os, io
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

OUT = os.path.dirname(os.path.abspath(__file__))

from build_shell import head, nav, footer


def shell(title, desc, body, page_id, ar=True):
    """Arabic page shell — chrome comes from build_shell so it cannot drift."""
    name = page_id + ".html"
    return head(title, desc, name, ar=True) + nav(name, ar=True) + body + footer(ar=True)


def write(file, content):
    with io.open(os.path.join(OUT, file), "w", encoding="utf-8") as f: f.write(content)
    print("wrote", file, len(content))

# ── AR index ──
marquee = '<span class="logo-cell">Panerai</span><span class="logo-cell">TAG Heuer</span><span class="logo-cell">Crocs</span><span class="logo-cell">Beefbar</span><span class="logo-cell">Ted Baker</span><span class="logo-cell">Maje</span><span class="logo-cell">Coya</span><span class="logo-cell">Bagatelle</span><span class="logo-cell">Urth Caffé</span><span class="logo-cell">Morini</span><span class="logo-cell">Rüya</span><span class="logo-cell">Signor Sassi</span><span class="logo-cell">San Carlo</span><span class="logo-cell">Myazū</span><span class="logo-cell">Sumosan</span><span class="logo-cell">MNKY HSE</span><span class="logo-cell">Tashas</span><span class="logo-cell">Jones the Grocer</span><span class="logo-cell">Vero Moda</span><span class="logo-cell">Kiko</span><span class="logo-cell">Roka</span><span class="logo-cell">Clap</span><span class="logo-cell">Robata</span><span class="logo-cell">Fred</span><span class="logo-cell">Solitaire</span>'
index_body = f"""
<main id="main">
  <section class="hero">
    <div class="wrap hero-in">
      <p class="eyebrow hero-fade" style="animation-delay:.15s">التسويق عبر المؤثرين · أكثر من 52 دولة</p>
      <h1 class="mark hero-mark" aria-label="إيليت">
        <span style="animation-delay:.10s">E</span><span style="animation-delay:.17s">L</span><span style="animation-delay:.24s">I</span><span style="animation-delay:.31s">T</span><span class="flip" style="animation-delay:.38s">E</span>
      </h1>
      <p class="hero-tag hero-fade" style="animation-delay:.5s">إتقانٌ يُعيد تعريف التميّز</p>
      <p class="hero-lede hero-fade" style="animation-delay:.65s">نصلك بصنّاع محتوى يتابعهم عملاؤك فعلًا، وندير الحملة كاملة نيابةً عنك، ونُطلعك بدقة على ما حققته — بدعم مباشر على مدار الساعة.</p>
      <div class="hero-cta hero-fade" style="animation-delay:.8s">
        <a class="btn btn-gold" href="contacts.html">ابدأ حملتك <span class="arrow" aria-hidden="true">→</span></a>
        <a class="btn btn-ghost-dark" href="case-studies.html">شاهد قصص النجاح</a>
      </div>
    </div>
    <div class="rail hero-fade" style="animation-delay:.95s">
      <div class="wrap rail-in">
        <div class="rail-item"><span class="rail-n" data-count="52">52</span><span class="rail-l">دولة نصل إليها</span></div>
        <div class="rail-item"><span class="rail-n" data-count="50" data-suffix=" مليار">50 مليار</span><span class="rail-l">إجمالي المتابعين</span></div>
        <div class="rail-item"><span class="rail-n" data-count="85" data-suffix=" ألف">85 ألف</span><span class="rail-l">صانع محتوى</span></div>
        <div class="rail-item"><span class="rail-n" data-count="1500">1500</span><span class="rail-l">علامة تجارية</span></div>
      </div>
    </div>
  </section>

  <section class="trust" aria-labelledby="trust-h">
    <div class="wrap trust-head">
      <h2 class="eyebrow" id="trust-h">بعض العلامات التي نعمل معها</h2>
      <p class="trust-note">80 علامة فاخرة عبر 7 أسواق — ضيافة وأزياء وصناعة ساعات وتجميل.</p>
      <button class="chip-btn" type="button" data-marquee-toggle aria-pressed="false">إيقاف</button>
    </div>
    <div class="marquee" aria-hidden="true">
      <div class="marquee-track">{marquee}</div>
      <div class="marquee-track" aria-hidden="true">{marquee}</div>
    </div>
    <div class="wrap center mt-8"><a class="link-arrow" href="sponsors.html">شاهد جميع العملاء الـ75 <span class="arrow" aria-hidden="true">→</span></a></div>
  </section>

  <section class="sec" aria-labelledby="svc-h">
    <div class="wrap">
      <div class="sec-head reveal">
        <p class="eyebrow">كيف نعمل</p>
        <h2 class="sec-title" id="svc-h">أربع خطوات، من البداية إلى النتيجة.</h2>
        <p class="sec-sub">أنت تحدّد الهدف. ونحن نختار صنّاع المحتوى، ونتفق على الشروط، وندير المحتوى، ونرفع لك النتائج — ويتابع فريقك كل ذلك في مكان واحد.</p>
      </div>
      <div class="svc-grid">
        <article class="svc svc--media reveal"><div class="svc__visual"><span class="svc__badge">01</span><img src="../assets/img/services/influencer-discovery.jpeg" alt="صانع محتوى يصوّر مقطعاً قصيراً بهاتفه" width="1100" height="825" loading="lazy" decoding="async"></div><div class="svc-body"><span class="svc-idx">خطوة 01</span><h3 class="svc-title"><b>اكتشاف</b><span>المؤثرين</span></h3><p class="svc-copy">نختار من شبكتنا صنّاع محتوى جمهورهم هو نفسه الجمهور الذي تريد الوصول إليه.</p></div></article>
        <article class="svc svc--media reveal" style="transition-delay:.08s"><div class="svc__visual"><span class="svc__badge">02</span><img src="../assets/img/services/campaign-strategy.jpeg" alt="جلسة تخطيط حملة حول جدول مطبوع" width="1100" height="825" loading="lazy" decoding="async"></div><div class="svc-body"><span class="svc-idx">خطوة 02</span><h3 class="svc-title"><b>استراتيجية</b><span>الحملة</span></h3><p class="svc-copy">نتفق معك على الهدف والشروط والجدول الزمني قبل أن يَنشر أحد شيئًا.</p></div></article>
        <article class="svc svc--media reveal" style="transition-delay:.16s"><div class="svc__visual"><span class="svc__badge">03</span><img src="../assets/img/services/content-creation.jpeg" alt="تصوير محتوى جارٍ في الموقع" width="1100" height="825" loading="lazy" decoding="async"></div><div class="svc-body"><span class="svc-idx">خطوة 03</span><h3 class="svc-title"><b>صناعة</b><span>المحتوى</span></h3><p class="svc-copy">الموجز والموافقات والنشر في مكان واحد، فلا يضيع شيء بين المحادثات.</p></div></article>
        <article class="svc svc--media reveal" style="transition-delay:.24s"><div class="svc__visual"><span class="svc__badge">04</span><img src="../assets/img/services/performance-tracking.jpeg" alt="لوحة أداء معروضة على شاشة حاسوب" width="1100" height="825" loading="lazy" decoding="async"></div><div class="svc-body"><span class="svc-idx">خطوة 04</span><h3 class="svc-title"><b>تتبّع</b><span>الأداء</span></h3><p class="svc-copy">ترى كل منشور فور نشره، وتستلم تقريرًا واضحًا في النهاية.</p></div></article>
      </div>
    </div>
  </section>

  <section class="sec sec--sunken" aria-labelledby="proof-h">
    <div class="wrap">
      <div class="sec-head reveal">
        <p class="eyebrow">أين نحن الأقوى</p>
        <h2 class="sec-title" id="proof-h">حضورٌ عميق في الخليج، وخبرةٌ في الضيافة والعلامات الفاخرة.</h2>
        <p class="sec-sub">سجلّ عملائنا يوضّح بالضبط أين نعرف طريقنا.</p>
      </div>
      <div class="proof">
        <div class="reveal"><h3>العملاء حسب الفئة</h3>
          <div class="meters">
            <div class="meter-row"><div class="meter-top"><span class="meter-name">مطاعم</span><span class="meter-val">58.8%</span></div><div class="meter-bar"><i class="meter-fill" data-w="100"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">أزياء</span><span class="meter-val">10.3%</span></div><div class="meter-bar"><i class="meter-fill" data-w="17.5"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">مقاهٍ</span><span class="meter-val">10.3%</span></div><div class="meter-bar"><i class="meter-fill" data-w="17.5"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">عطور</span><span class="meter-val">4.4%</span></div><div class="meter-bar"><i class="meter-fill" data-w="7.5"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">تجميل</span><span class="meter-val">2.9%</span></div><div class="meter-bar"><i class="meter-fill" data-w="5"></i></div></div>
          </div>
        </div>
        <div class="reveal" style="transition-delay:.1s"><h3>العملاء حسب السوق</h3>
          <div class="meters">
            <div class="meter-row"><div class="meter-top"><span class="meter-name">السعودية</span><span class="meter-val">71.7%</span></div><div class="meter-bar"><i class="meter-fill" data-w="100"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">الكويت</span><span class="meter-val">15.2%</span></div><div class="meter-bar"><i class="meter-fill" data-w="21.2"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">الإمارات</span><span class="meter-val">4.4%</span></div><div class="meter-bar"><i class="meter-fill" data-w="6.1"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">قطر</span><span class="meter-val">4.4%</span></div><div class="meter-bar"><i class="meter-fill" data-w="6.1"></i></div></div>
            <div class="meter-row"><div class="meter-top"><span class="meter-name">البحرين</span><span class="meter-val">2.2%</span></div><div class="meter-bar"><i class="meter-fill" data-w="3"></i></div></div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="sec" aria-labelledby="why-h">
    <div class="wrap">
      <div class="sec-head reveal"><p class="eyebrow">لماذا إيليت</p><h2 class="sec-title" id="why-h">عشر سنوات من العلاقات، تحت تصرّفك غدًا.</h2></div>
      <div class="why reveal">
        <div class="why-item"><h3>عقد من التميّز</h3><p>أكثر من عشر سنوات في إدارة حملات المؤثرين لعلامات فاخرة — الطريقة مجرّبة ومعروفة.</p></div>
        <div class="why-item"><h3>انتشار عالمي</h3><p>حضورنا في أكثر من 52 دولة يصل بعلامتك إلى الجمهور المناسب أينما كان.</p></div>
        <div class="why-item"><h3>شراكات مميّزة</h3><p>علاقات حصرية مع صنّاع المحتوى ومع العلامات الفاخرة تفتح لك أبوابًا لا يصل إليها غيرك.</p></div>
        <div class="why-item"><h3>نتائج قابلة للقياس</h3><p>نتتبّع كل حملة من أولها إلى آخرها، فترى النموّ بعينك لا في وعودٍ تُقال لك.</p></div>
        <div class="why-item"><h3>جودة استثنائية</h3><p>من فكرة الحملة إلى تنفيذها، نلتزم بأعلى معايير الجودة والاحترافية.</p></div>
      </div>
    </div>
  </section>

  <section class="cta">
    <div class="wrap cta-in">
      <p class="eyebrow">تواصل معنا</p>
      <h2 class="cta-title">أخبرنا بما تريد إطلاقه.</h2>
      <p class="cta-lede">سنعود إليك بصنّاع المحتوى والخطة والأرقام. عادةً خلال يومين.</p>
      <div class="row" style="justify-content:center">
        <a class="btn btn-gold" href="contacts.html">ابدأ حملتك <span class="arrow" aria-hidden="true">→</span></a>
        <a class="btn btn-ghost-dark" href="about.html">عن إيليت</a>
      </div>
    </div>
  </section>
</main>"""

write("ar/index.html", shell("إيليت — إتقانٌ يُعيد تعريف التميّز","تربط إيليت العلامات التجارية الفاخرة بصنّاع محتوى موثوقين في أكثر من 52 دولة، ثم تخطط للحملة وتديرها وتقيس نتائجها في مساحة عمل واحدة.",index_body,"index"))

# ── AR dashboard ──
dash_body = f"""
<main id="main">
  <section class="pagehead"><div class="wrap pagehead-in">
    <p class="tag">مساحة العمل</p><h1>مساحة عمل واحدة لكل حملة</h1>
    <p class="lede">الفروع، صنّاع المحتوى، مراحل الحملة والتغطية — تمنحك منصة إيليت نظرة شاملة على كل أنشطة التسويق عبر المؤثرين.</p>
    <div class="row">
      <a class="btn btn-gold" href="https://gc-elite.com/dashboard">سجّل الدخول <span class="arrow" aria-hidden="true">→</span></a>
      <a class="btn btn-ghost-dark" href="contacts.html">اطلب عرضاً توضيحياً</a>
    </div>
  </div></section>

  <section class="sec sec--tight"><div class="wrap">
    <div class="demo-card reveal" data-dashboard-demo>
      <div class="demo-card__head">
        <div><span class="eyebrow">معاينة تفاعلية</span><p class="subtle" style="margin-top:6px">بيانات حملة توضيحية — بدّل العرض لاستكشاف مساحة العمل.</p></div>
        <div class="segmented" role="group" aria-label="اختر حملة معاينة">
          <button type="button" data-demo-view="launch" aria-pressed="true">إطلاق صيفي</button>
          <button type="button" data-demo-view="growth" aria-pressed="false">نموّ مستمر</button>
          <button type="button" data-demo-view="opening" aria-pressed="false">موقع جديد</button>
        </div>
      </div>
      <div class="row" style="justify-content:space-between">
        <span class="demo-row__stage" data-demo-campaign>إطلاق صيفي · الرياض</span>
        <span class="demo-row__stage" data-demo-period>01–30 يونيو 2026</span>
      </div>
    </div>
    <div class="kpi-grid mt-8 reveal">
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">الفروع</span></div><span class="kpi__value" data-demo-kpi="branches" data-count="4">4</span><span class="kpi__delta">تقارير لكل موقع</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">المؤثرون المفضّلون</span></div><span class="kpi__value" data-demo-kpi="creators" data-count="128">128</span><span class="kpi__delta">شبكتك المحفوظة</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">الحملات</span></div><span class="kpi__value" data-demo-kpi="campaigns" data-count="7">7</span><span class="kpi__delta">مباشرة ومجدولة</span></div>
      <div class="kpi"><div class="kpi__top"><span class="kpi__label">التغطية</span></div><span class="kpi__value" data-demo-kpi="coverage" data-count="346">346</span><span class="kpi__delta">ستوريز · منشورات · فيديو</span></div>
    </div>
  </div></section>

  <section class="sec sec--sunken"><div class="wrap">
    <div class="sec-head reveal"><p class="eyebrow">نظرة على المؤثرين</p><h2 class="sec-title">كل صانع محتوى، كل مرحلة.</h2><p class="sec-sub">تابع كل مؤثر من أول تواصل إلى التغطية المنشورة، دون ملاحقة أحد للحصول على تحديث.</p></div>
    <div class="kpi-grid reveal" aria-label="مراحل الحملة">
      <div class="kpi"><span class="kpi__label">قيد الانتظار</span><span class="kpi__value" data-demo-stage="pending">0</span></div>
      <div class="kpi"><span class="kpi__label">مؤكَّد</span><span class="kpi__value" data-demo-stage="confirmed">0</span></div>
      <div class="kpi"><span class="kpi__label">تمت الزيارة</span><span class="kpi__value" data-demo-stage="visited">0</span></div>
      <div class="kpi"><span class="kpi__label">تم التسليم</span><span class="kpi__value" data-demo-stage="delivered">0</span></div>
      <div class="kpi"><span class="kpi__label">قيد الإنتاج</span><span class="kpi__value" data-demo-stage="post-creation">0</span></div>
      <div class="kpi"><span class="kpi__label">تمت المشاركة</span><span class="kpi__value" data-demo-stage="shared">0</span></div>
      <div class="kpi"><span class="kpi__label">تمت التغطية</span><span class="kpi__value" data-demo-stage="covered">0</span></div>
    </div>
    <div class="proof mt-12">
      <div class="card reveal"><div class="row" style="justify-content:space-between"><div><span class="eyebrow">مساحة مباشرة</span><h3 class="h4 mt-4">الحملات الأخيرة</h3></div><a class="link-arrow" href="contacts.html">عرض الكل <span class="arrow" aria-hidden="true">→</span></a></div><div class="demo-list mt-6" data-demo-campaigns></div></div>
      <div class="card reveal" style="transition-delay:.1s"><div class="row" style="justify-content:space-between"><h3 class="h4">تفاصيل التغطية</h3><span class="kpi__delta" data-demo-total>346 عنصراً</span></div>
        <div class="meters mt-6">
          <div class="meter-row"><div class="meter-top"><span class="meter-name">ستوري</span><span class="meter-val" data-demo-pct="story">201</span></div><div class="meter-bar"><i class="meter-fill" data-demo-bar="story" data-w="58"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">منشور</span><span class="meter-val" data-demo-pct="post">82</span></div><div class="meter-bar"><i class="meter-fill" data-demo-bar="post" data-w="24"></i></div></div>
          <div class="meter-row"><div class="meter-top"><span class="meter-name">فيديو</span><span class="meter-val" data-demo-pct="video">63</span></div><div class="meter-bar"><i class="meter-fill" data-demo-bar="video" data-w="18"></i></div></div>
        </div>
      </div>
    </div>
  </div></section>

  <section class="sec"><div class="wrap">
    <div class="sec-head sec-head--center reveal"><p class="eyebrow">داخل المنصة</p><h2 class="sec-title">مبنية لمن يديرون الحملات.</h2></div>
    <div class="kpi-grid mt-12">
      <article class="card card--hover reveal"><h3 class="card__title">المؤثرون والمفضّلة</h3><p class="muted">تصفّح الشبكة، احفظ المفضّلة وابنِ قوائم مختصرة يراها فريقك كله.</p></article>
      <article class="card card--hover reveal" style="transition-delay:.08s"><h3 class="card__title">الفروع</h3><p class="muted">أدِر علامات متعددة المواقع مع تغطية وتسجيلات دخول لكل فرع.</p></article>
      <article class="card card--hover reveal" style="transition-delay:.16s"><h3 class="card__title">الماسح الضوئي</h3><p class="muted">تحقّق من تسجيل صنّاع المحتوى في الموقع بمسح سريع — بلا أوراق.</p></article>
      <article class="card card--hover reveal" style="transition-delay:.24s"><h3 class="card__title">الحملات</h3><p class="muted">اكتب الموجز، ووافق على المحتوى، وتابع كل مرحلة من الحملة في خط زمني واحد.</p></article>
      <article class="card card--hover reveal" style="transition-delay:.32s"><h3 class="card__title">التقارير</h3><p class="muted">تغطية حسب الصيغة والمؤثر، جاهزة للمشاركة مع أصحاب المصلحة.</p></article>
      <article class="card card--hover reveal" style="transition-delay:.4s"><h3 class="card__title">دعم على مدار الساعة</h3><p class="muted">فريق مباشر وراء المنصة متى احتاجت حملةٌ إلى يد.</p></article>
    </div>
  </div></section>

  <section class="cta"><div class="wrap cta-in"><h2 class="cta-title">شاهدها بحملتك أنت.</h2><p class="cta-lede">سجّل الدخول إلى مساحة عملك، أو اطلب جولة ببيانات علامتك.</p><div class="row" style="justify-content:center"><a class="btn btn-gold" href="https://gc-elite.com/dashboard">تسجيل الدخول <span class="arrow" aria-hidden="true">→</span></a><a class="btn btn-ghost-dark" href="contacts.html">اطلب عرضاً</a></div></div></section>
</main>"""

write("ar/dashboard.html", shell("مساحة العمل — إيليت","مساحة عمل واحدة للفروع وصنّاع المحتوى ومراحل الحملة وتقارير التغطية.",dash_body,"dashboard"))

print("DONE")