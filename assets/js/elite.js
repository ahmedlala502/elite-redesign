(function(){
  'use strict';

  var root = document.documentElement;
  var lang = (root.getAttribute('lang') || 'en').slice(0,2);
  var isAr = lang === 'ar';

  /* ---------- i18n ---------- */
  var STRINGS = {
    en: {
      openMenu:'Open menu', closeMenu:'Close menu',
      play:'Play', pause:'Pause',
      themeLight:'Switch to light theme', themeDark:'Switch to dark theme',
      sent:'Sent',
      results:function(n,total){ return n === total ? (total + ' shown') : (n + ' of ' + total + ' shown'); },
      none:'No results'
    },
    ar: {
      openMenu:'فتح القائمة', closeMenu:'إغلاق القائمة',
      play:'تشغيل', pause:'إيقاف',
      themeLight:'التبديل إلى المظهر الفاتح', themeDark:'التبديل إلى المظهر الداكن',
      sent:'تم الإرسال',
      results:function(n,total){ return n === total ? ('عرض ' + total) : ('عرض ' + n + ' من ' + total); },
      none:'لا توجد نتائج'
    }
  };
  var t = function(k){ var s = STRINGS[lang] || STRINGS.en; return s[k] !== undefined ? s[k] : (STRINGS.en[k] !== undefined ? STRINGS.en[k] : k); };

  var each = function(list, fn){ Array.prototype.forEach.call(list, fn); };
  var $  = function(sel, ctx){ return (ctx||document).querySelector(sel); };
  var $$ = function(sel, ctx){ return Array.prototype.slice.call((ctx||document).querySelectorAll(sel)); };
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- Theme ---------- */
  var themeBtn = document.getElementById('theme');
  var themeMeta = $('meta[name="theme-color"]');
  var systemDark = matchMedia('(prefers-color-scheme: dark)');

  var effectiveTheme = function(){
    var set = root.getAttribute('data-theme');
    return set === 'dark' || set === 'light' ? set : (systemDark.matches ? 'dark' : 'light');
  };
  var syncTheme = function(){
    var mode = effectiveTheme();
    // Keep the browser chrome in step with the page background.
    if(themeMeta) themeMeta.setAttribute('content', mode === 'dark' ? '#0B0B0C' : '#F7F5F3');
    if(themeBtn) themeBtn.setAttribute('aria-label', mode === 'dark' ? t('themeLight') : t('themeDark'));
  };
  try{ var saved = localStorage.getItem('elite-theme'); if(saved) root.setAttribute('data-theme', saved); }catch(e){}
  syncTheme();
  if(systemDark.addEventListener) systemDark.addEventListener('change', syncTheme);
  if(themeBtn) themeBtn.addEventListener('click', function(){
    var next = effectiveTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try{ localStorage.setItem('elite-theme', next); }catch(e){}
    syncTheme();
  });

  /* ---------- Mobile drawer ---------- */
  var burger = document.getElementById('burger'), mnav = document.getElementById('mnav');
  if(burger && mnav){
    var setMenu = function(open, returnFocus){
      mnav.setAttribute('data-open', String(open));
      burger.setAttribute('aria-expanded', String(open));
      burger.setAttribute('aria-label', open ? t('closeMenu') : t('openMenu'));
      document.body.classList.toggle('is-menu-open', open);
      if(!open && returnFocus) burger.focus();
    };
    setMenu(false);
    burger.addEventListener('click', function(){ setMenu(mnav.getAttribute('data-open') !== 'true'); });
    each(mnav.querySelectorAll('a'), function(a){ a.addEventListener('click', function(){ setMenu(false); }); });
    addEventListener('keydown', function(e){
      if(e.key !== 'Escape' || mnav.getAttribute('data-open') !== 'true') return;
      setMenu(false, true);
    });
    // Close the drawer when the viewport grows past the mobile breakpoint.
    var wide = matchMedia('(min-width: 861px)');
    if(wide.addEventListener) wide.addEventListener('change', function(e){ if(e.matches) setMenu(false); });
  }

  /* ---------- Nav stuck state ---------- */
  var nav = document.getElementById('nav');
  if(nav){
    var onScroll = function(){ nav.setAttribute('data-stuck', String(scrollY > 8)); };
    addEventListener('scroll', onScroll, {passive:true}); onScroll();
  }

  /* ---------- Reveal + meter fills ---------- */
  var setW = function(f){ f.style.width = f.getAttribute('data-w') + '%'; };
  if(reduce || !('IntersectionObserver' in window)){
    each(document.querySelectorAll('.reveal'), function(el){ el.classList.add('in'); });
    $$('.meter-fill').forEach(setW);
  } else {
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(!e.isIntersecting) return;
        e.target.classList.add('in');
        each(e.target.querySelectorAll('.meter-fill'), function(f, i){
          setTimeout(function(){ setW(f); }, 120 * i);
        });
        io.unobserve(e.target);
      });
    }, {threshold:.18, rootMargin:'0px 0px -8% 0px'});
    each(document.querySelectorAll('.reveal'), function(el){ io.observe(el); });
  }

  /* ---------- Count-up stats ---------- */
  var format = function(v, suffix){
    // Suffix stays attached for the whole run so the number never changes width mid-animation.
    return (suffix ? v + suffix : String(v));
  };
  var counters = $$('[data-count]');
  if(counters.length){
    counters.forEach(function(el){
      var target = parseFloat(el.getAttribute('data-count'));
      var suffix = el.getAttribute('data-suffix') || '';
      if(isNaN(target)) return;
      if(reduce || !('IntersectionObserver' in window)){ el.textContent = format(target, suffix); return; }
      el.textContent = format(0, suffix);
      var cio = new IntersectionObserver(function(entries){
        entries.forEach(function(e){
          if(!e.isIntersecting) return;
          var dur = 1400, t0 = performance.now();
          (function step(now){
            var p = Math.min((now - t0) / dur, 1);
            var eased = 1 - Math.pow(1 - p, 3);
            el.textContent = format(Math.round(target * eased), suffix);
            if(p < 1) requestAnimationFrame(step);
            else el.textContent = format(target, suffix);
          })(t0);
          cio.unobserve(el);
        });
      }, {threshold:.5});
      cio.observe(el);
    });
  }

  /* ---------- Marquee pause toggle ---------- */
  each(document.querySelectorAll('[data-marquee-toggle]'), function(button){
    var region = button.closest('.trust');
    if(!region) return;
    // Reduced motion means the track is already still — start in the paused state.
    if(reduce){
      region.classList.add('is-paused');
      button.setAttribute('aria-pressed', 'true');
      button.textContent = t('play');
    }
    button.addEventListener('click', function(){
      var paused = region.classList.toggle('is-paused');
      // Under reduced motion the CSS holds the track still, so Play has to say
      // so explicitly — otherwise the button looks live and does nothing.
      region.classList.toggle('is-playing', reduce && !paused);
      button.setAttribute('aria-pressed', String(paused));
      button.textContent = paused ? t('play') : t('pause');
    });
  });

  /* ---------- Tabs (segmented) ---------- */
  each(document.querySelectorAll('.segmented[role="tablist"]'), function(tablist){
    var tabs = $$('[role="tab"]', tablist);
    var select = function(tab){
      var panel = document.getElementById(tab.getAttribute('aria-controls'));
      tabs.forEach(function(x){
        x.setAttribute('aria-selected', String(x === tab));
        x.setAttribute('tabindex', x === tab ? '0' : '-1');
      });
      each(tablist.parentNode.querySelectorAll('[role="tabpanel"]'), function(p){ p.hidden = p !== panel; });
    };
    tabs.forEach(function(tab, i){
      tab.addEventListener('click', function(){ select(tab); });
      tab.addEventListener('keydown', function(e){
        var forward = isAr ? 'ArrowLeft' : 'ArrowRight';
        var back = isAr ? 'ArrowRight' : 'ArrowLeft';
        var next = e.key === forward ? i + 1 : e.key === back ? i - 1 : e.key === 'Home' ? 0 : e.key === 'End' ? tabs.length - 1 : -1;
        if(next < 0 && e.key !== 'Home') return;
        e.preventDefault();
        var target = tabs[(next + tabs.length) % tabs.length];
        select(target); target.focus();
      });
    });
  });

  /* ---------- Accordion ---------- */
  var accSeq = 0;
  each(document.querySelectorAll('.acc'), function(acc){
    var single = acc.hasAttribute('data-single');
    var items = $$('.acc__item', acc);
    items.forEach(function(item){
      var trigger = $('.acc__trigger', item), panel = $('.acc__panel', item);
      if(!trigger || !panel) return;
      var inner = panel.firstElementChild;
      var id = 'acc-panel-' + (++accSeq);
      panel.id = panel.id || id;
      if(!trigger.id) trigger.id = panel.id + '-trigger';
      // aria-expanded belongs on the control, not on its container.
      panel.setAttribute('role', 'region');
      panel.setAttribute('aria-labelledby', trigger.id);
      trigger.setAttribute('aria-controls', panel.id);
      trigger.setAttribute('aria-expanded', 'false');
      item.setAttribute('data-open', 'false');
      item.removeAttribute('aria-expanded');

      var close = function(it){
        var tr = $('.acc__trigger', it), pn = $('.acc__panel', it);
        if(!tr || !pn) return;
        tr.setAttribute('aria-expanded', 'false');
        it.setAttribute('data-open', 'false');
        pn.style.maxHeight = '0px';
      };
      trigger.addEventListener('click', function(){
        var open = trigger.getAttribute('aria-expanded') === 'true';
        if(single && !open) items.forEach(close);
        if(open){ close(item); return; }
        trigger.setAttribute('aria-expanded', 'true');
        item.setAttribute('data-open', 'true');
        panel.style.maxHeight = (inner ? inner.scrollHeight + 48 : 400) + 'px';
      });
    });
    // Keep an open panel correctly sized when text reflows.
    addEventListener('resize', function(){
      items.forEach(function(item){
        if(item.getAttribute('data-open') !== 'true') return;
        var panel = $('.acc__panel', item), inner = panel && panel.firstElementChild;
        if(panel) panel.style.maxHeight = (inner ? inner.scrollHeight + 48 : 400) + 'px';
      });
    });
  });

  /* ---------- Collection: category filter + search, one source of truth ----------
     A list can be driven by a chip group, a search box, or both. Both inputs are
     applied together so narrowing by category no longer wipes the query (and the
     other way round), and a single result count drives the empty states. */
  var collections = [];
  var registerCollection = function(list){
    var existing = null;
    collections.forEach(function(c){ if(c.list === list) existing = c; });
    if(existing) return existing;
    var c = {
      list: list,
      items: Array.prototype.slice.call(list.children),
      category: 'all',
      query: '',
      group: null,
      filterEmpty: null,
      searchEmpty: null,
      status: null
    };
    collections.push(c);
    return c;
  };

  var normalise = function(s){
    s = (s || '').toLowerCase();
    // Fold accents so "Urth Caffe" matches "Urth Caffé", and Arabic diacritics/alef forms.
    if(String.prototype.normalize) s = s.normalize('NFD').replace(/[̀-ًͯ-ْ]/g, '');
    return s.replace(/[آأإ]/g, 'ا').replace(/ى/g, 'ي').replace(/ة/g, 'ه').trim();
  };

  var applyCollection = function(c){
    var q = normalise(c.query);
    var shown = 0;
    c.items.forEach(function(el){
      var cat = el.getAttribute('data-cat') || '';
      // An empty data-cat means "uncategorised" — it belongs to "all" only.
      var catOk = c.category === 'all' || cat === c.category;
      var name = normalise(el.getAttribute('data-name') || el.textContent);
      var qOk = !q || name.indexOf(q) !== -1;
      var match = catOk && qOk;
      el.hidden = !match;
      if(match) shown++;
    });
    var none = shown === 0;
    // Searching gets the search copy; a bare category with no matches gets the category copy.
    if(c.searchEmpty) c.searchEmpty.hidden = !(none && q);
    if(c.filterEmpty) c.filterEmpty.hidden = !(none && !q);
    if(c.status) c.status.textContent = none ? t('none') : t('results')(shown, c.items.length);
    return shown;
  };

  each(document.querySelectorAll('[data-filter-group]'), function(group){
    var list = $(group.getAttribute('data-filter-target'));
    if(!list) return;
    var c = registerCollection(list);
    c.group = group;
    c.filterEmpty = $(group.getAttribute('data-filter-empty') || '#__none');
    var buttons = $$('[data-value]', group);
    buttons.forEach(function(b){
      // Live per-category counts, so a chip never promises results it cannot deliver.
      var value = b.getAttribute('data-value');
      var slot = $('.count', b);
      var n = value === 'all' ? c.items.length : c.items.filter(function(el){ return (el.getAttribute('data-cat') || '') === value; }).length;
      if(slot) slot.textContent = n;
      else if(value !== 'all'){
        var span = document.createElement('span');
        span.className = 'count'; span.textContent = n;
        b.appendChild(document.createTextNode(' ')); b.appendChild(span);
      }
      if(n === 0 && value !== 'all') b.disabled = true;
      b.addEventListener('click', function(){
        buttons.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); });
        c.category = value;
        applyCollection(c);
      });
    });
  });

  each(document.querySelectorAll('[data-search]'), function(input){
    var list = $(input.getAttribute('data-search'));
    if(!list) return;
    var c = registerCollection(list);
    c.searchEmpty = $('[data-search-empty]', list.parentNode) || $('[data-search-empty]');
    var timer;
    input.addEventListener('input', function(){
      clearTimeout(timer);
      timer = setTimeout(function(){ c.query = input.value; applyCollection(c); }, 120);
    });
  });

  collections.forEach(function(c){
    // A polite live region so filtering is announced, not just seen.
    var status = document.createElement('p');
    status.className = 'sr'; status.setAttribute('role', 'status'); status.setAttribute('aria-live', 'polite');
    c.list.parentNode.insertBefore(status, c.list);
    c.status = status;
    applyCollection(c);
    c.status.textContent = '';
  });



  /* ---------- Campaign films ----------
     Videos are muted, loop and carry preload="none", so a page of 39 cards
     costs nothing until something actually plays. Only one plays at a time. */
  var playing = null;

  var toggleFor = function(v){
    var card = v.closest('.dcard') || v.closest('.reel__row') || v.parentNode;
    return card && $('[data-video-toggle]', card);
  };

  var markButton = function(v, on){
    var btn = toggleFor(v);
    if(!btn) return;
    btn.setAttribute('aria-pressed', String(on));
    var lbl = $('.dcard__cta-label', btn);
    var text = btn.getAttribute(on ? 'data-label-pause' : 'data-label-play');
    if(lbl && text) lbl.textContent = text;
  };

  var stopVideo = function(v){
    if(!v) return;
    v.pause();
    markButton(v, false);
    if(playing === v) playing = null;
  };

  var startVideo = function(v){
    if(!v || playing === v) return;
    stopVideo(playing);
    var p = v.play();
    // A rejected play (autoplay policy, missing file) must not leave a stuck state.
    if(p && p.catch) p.catch(function(){ stopVideo(v); });
    playing = v;
    markButton(v, true);
  };

  each(document.querySelectorAll('[data-video-toggle]'), function(btn){
    var card = btn.closest('.dcard') || btn.closest('.reel__row') || btn.parentNode;
    var video = card && $('video', card);
    if(!video) return;

    btn.addEventListener('click', function(e){
      e.preventDefault(); e.stopPropagation();
      if(video.paused) startVideo(video); else stopVideo(video);
    });

    // Hover preview on precise pointers only — never on touch, never on
    // reduced motion, and never inside the carousel (which drives its own).
    // Hover preview on precise pointers only, and only on the grid cards —
    // the reel rows are large enough that the badge is the right control.
    if(!reduce && card.classList.contains('dcard') &&
       matchMedia('(hover:hover) and (pointer:fine)').matches){
      card.addEventListener('mouseenter', function(){ startVideo(video); });
      card.addEventListener('mouseleave', function(){ stopVideo(video); video.currentTime = 0; });
    }
  });

  // A video scrolled out of view has no business still running.
  if('IntersectionObserver' in window){
    var vio = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(!e.isIntersecting) stopVideo(e.target); });
    }, {threshold:0});
    each(document.querySelectorAll('video.story__video'), function(v){ vio.observe(v); });
  }
  document.addEventListener('visibilitychange', function(){ if(document.hidden) stopVideo(playing); });

  /* ---------- Form validation ---------- */
  var emailRe = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
  each(document.querySelectorAll('[data-validate]'), function(form){
    var validateField = function(field){
      var wrap = field.closest('.field');
      var value = field.value.trim();
      var bad = !value || (field.type === 'email' && !emailRe.test(value));
      if(wrap) wrap.classList.toggle('is-invalid', bad);
      field.setAttribute('aria-invalid', String(bad));
      var err = wrap && $('.field__error', wrap);
      if(err){
        if(!err.id) err.id = (field.id || 'field') + '-error';
        if(bad) field.setAttribute('aria-describedby', err.id);
        else field.removeAttribute('aria-describedby');
      }
      return !bad;
    };
    each(form.querySelectorAll('[required]'), function(field){
      // Re-check on blur, then live once a field has already been marked bad.
      field.addEventListener('blur', function(){ validateField(field); });
      field.addEventListener('input', function(){
        var wrap = field.closest('.field');
        if(wrap && wrap.classList.contains('is-invalid')) validateField(field);
      });
    });
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var ok = true, first = null;
      each(form.querySelectorAll('[required]'), function(field){
        if(!validateField(field)){ ok = false; if(!first) first = field; }
      });
      if(!ok){ if(first) first.focus(); return; }
      var toast = document.getElementById('toast');
      if(toast){
        toast.textContent = form.getAttribute('data-success') || t('sent');
        toast.classList.add('is-show');
        setTimeout(function(){ toast.classList.remove('is-show'); }, 3200);
      }
      form.reset();
      each(form.querySelectorAll('.field'), function(f){ f.classList.remove('is-invalid'); });
    });
  });

  /* ---------- Dashboard demo ---------- */
  var demo = $('[data-dashboard-demo]');
  if(demo){
    var L = function(en, ar){ return isAr ? ar : en; };
    var stage = function(en, ar){ return L(en, ar); };
    var DATA = {
      launch: {
        branches:4, creators:128, campaignCount:7, coverage:346,
        period: L('01–30 Jun 2026','١ – ٣٠ يونيو ٢٠٢٦'), name: L('Summer launch · Riyadh','إطلاق الصيف · الرياض'),
        stages:{pending:24, confirmed:18, visited:12, delivered:9, 'post-creation':7, shared:5, covered:3},
        campaigns:[
          [L('Riyadh — Olaya','الرياض — العليا'), stage('Delivered','تم التسليم'), '98'],
          [L('Jeddah — Tahlia','جدة — التحلية'), stage('Shared','تم النشر'), '76'],
          [L('Dammam — Corniche','الدمام — الكورنيش'), stage('Confirmed','مؤكد'), '54'],
          [L('Mecca — Aziziyah','مكة — العزيزية'), stage('Pending','قيد الانتظار'), '41']
        ],
        bars:{story:201, post:82, video:63}
      },
      growth: {
        branches:6, creators:204, campaignCount:11, coverage:512,
        period: L('Q2 2026','الربع الثاني ٢٠٢٦'), name: L('Always-on growth · KSA','نمو مستمر · السعودية'),
        stages:{pending:31, confirmed:22, visited:16, delivered:13, 'post-creation':10, shared:8, covered:6},
        campaigns:[
          [L('Riyadh — Olaya','الرياض — العليا'), stage('Shared','تم النشر'), '112'],
          [L('Jeddah — Tahlia','جدة — التحلية'), stage('Delivered','تم التسليم'), '88'],
          [L('Dammam — Corniche','الدمام — الكورنيش'), stage('Visited','تمت الزيارة'), '64'],
          [L('Kuwait — Salhiya','الكويت — السالمية'), stage('Confirmed','مؤكد'), '49']
        ],
        bars:{story:298, post:142, video:72}
      },
      opening: {
        branches:2, creators:86, campaignCount:4, coverage:198,
        period: L('Sep 2026','سبتمبر ٢٠٢٦'), name: L('New location · Dubai','افتتاح جديد · دبي'),
        stages:{pending:14, confirmed:10, visited:7, delivered:5, 'post-creation':4, shared:3, covered:2},
        campaigns:[
          [L('Dubai — DIFC','دبي — مركز دبي المالي'), stage('Pending','قيد الانتظار'), '42'],
          [L('Dubai — Marina','دبي — المارينا'), stage('Confirmed','مؤكد'), '38'],
          [L('Abu Dhabi — Yas','أبوظبي — ياس'), stage('Visited','تمت الزيارة'), '31'],
          [L('Sharjah — Rolla','الشارقة — الرولة'), stage('Pending','قيد الانتظار'), '12']
        ],
        bars:{story:118, post:52, video:28}
      }
    };
    var pieces = function(n){ return isAr ? (n + ' عنصر') : (n + ' pieces'); };
    var render = function(view){
      var d = DATA[view]; if(!d) return;
      var set = function(sel, val){ var el = $(sel, demo); if(el) el.textContent = val; };
      set('[data-demo-campaign]', d.name);
      set('[data-demo-period]', d.period);
      var kpis = {branches:d.branches, creators:d.creators, campaigns:d.campaignCount, coverage:d.coverage};
      Object.keys(kpis).forEach(function(k){ var el = $('[data-demo-kpi="'+k+'"]'); if(el) el.textContent = kpis[k]; });
      Object.keys(d.stages).forEach(function(k){ var el = $('[data-demo-stage="'+k+'"]'); if(el) el.textContent = d.stages[k]; });
      var list = $('[data-demo-campaigns]');
      if(list){
        list.innerHTML = '';
        d.campaigns.forEach(function(r){
          var row = document.createElement('div'); row.className = 'demo-row';
          var name = document.createElement('span'); name.className = 'demo-row__name'; name.textContent = r[0];
          var st = document.createElement('span'); st.className = 'demo-row__stage'; st.textContent = r[1];
          var n = document.createElement('span'); n.className = 'demo-row__n'; n.textContent = r[2];
          row.appendChild(name); row.appendChild(st); row.appendChild(n);
          list.appendChild(row);
        });
      }
      var total = $('[data-demo-total]'); if(total) total.textContent = pieces(d.coverage);
      Object.keys(d.bars).forEach(function(k){
        var bar = $('[data-demo-bar="'+k+'"]'), pct = $('[data-demo-pct="'+k+'"]');
        if(bar) bar.style.width = Math.round(d.bars[k] / d.coverage * 100) + '%';
        if(pct) pct.textContent = d.bars[k];
      });
    };
    var views = $$('[data-demo-view]', demo);
    views.forEach(function(b){
      b.addEventListener('click', function(){
        views.forEach(function(x){ x.setAttribute('aria-pressed', String(x === b)); });
        render(b.getAttribute('data-demo-view'));
      });
    });
    var active = views.filter(function(b){ return b.getAttribute('aria-pressed') === 'true'; })[0] || views[0];
    render(active ? active.getAttribute('data-demo-view') : 'launch');
  }

  /* ---------- Lazy media: fade in once decoded ---------- */
  each(document.querySelectorAll('img[loading="lazy"]'), function(img){
    var done = function(){ img.classList.add('is-loaded'); };
    if(img.complete && img.naturalWidth) done();
    else img.addEventListener('load', done, {once:true});
    img.addEventListener('error', function(){ img.classList.add('is-broken'); }, {once:true});
  });

  /* ---------- Current year ---------- */
  each(document.querySelectorAll('[data-year]'), function(el){
    el.textContent = String(new Date().getFullYear());
  });
})();
