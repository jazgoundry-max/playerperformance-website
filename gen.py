#!/usr/bin/env python3
"""Builds the Player Performance website pages from one shared header/footer."""
import html, json, pathlib

import os
OUT = pathlib.Path(os.environ.get("SITE_OUT") or (pathlib.Path(__file__).parent / "_site"))
OUT.mkdir(parents=True, exist_ok=True)
SITE = "https://playerperformance.uk"
STYLE_V = "20261124e"
PORTAL = "https://pp-portal.azurewebsites.net"
SIGNIN = PORTAL + "/signin"
EMAIL = "inquiries@playerperformance.uk"
INSTA = "https://www.instagram.com/playerperformanceuk/"
FACEBOOK = "https://www.facebook.com/share/1E9Ee1qiNa/"
TIKTOK = "https://www.tiktok.com/@playerperformanceuk"
SOCIALS = [("Facebook", FACEBOOK, '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M13.5 21v-7.5h2.5l.4-3h-2.9V8.6c0-.9.3-1.5 1.5-1.5h1.5V4.4c-.3 0-1.2-.1-2.2-.1-2.2 0-3.8 1.4-3.8 3.9v2.3H8v3h2.5V21h3z"/></svg>'), ("Instagram", INSTA, '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>'), ("TikTok", TIKTOK, '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M16.6 3c.4 2.1 1.8 3.6 3.9 3.8v3a7 7 0 0 1-3.9-1.2v6.1A5.8 5.8 0 1 1 10.8 9v3.1a2.8 2.8 0 1 0 2.8 2.8V3h3z"/></svg>')]
SOCIAL_ICONS = "".join(f'<a href="{u}" target="_blank" rel="noopener" aria-label="Player Performance on {n}">{svg}</a>' for n, u, svg in SOCIALS)

NAV = [("index.html", "Home"), ("group-sessions.html", "Group sessions"), ("1-2-1.html", "1-2-1 coaching"),
       ("goalkeeping.html", "Goalkeeping"), ("camps.html", "Camps"), ("tournaments.html", "International"), ("mindset.html", "Mindset"), ("about.html", "About"), ("careers.html", "Careers"), ("reviews.html", "Reviews"), ("faqs.html", "FAQs"),
       ("contact.html", "Contact")]


def photo(label, note="Your photo here", wide=False, src=None, alt=None, pos="center"):
    if src:
        return f'<div class="photo has-img{" wide" if wide else ""}"><img src="{src}" alt="{html.escape(alt or label)}" loading="lazy" style="object-position:{pos}"></div>'
    return f'<div class="photo{" wide" if wide else ""}" aria-hidden="true"></div>'


def todo(text="Placeholder: tell Claude what this should say"):
    # Placeholder notes are for drafting only and never appear on the public site.
    return ""


def page(file, title, desc, body, extra_head=""):
    nav = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f == file else ""}>{n}</a>' for f, n in NAV)
    foot_links = "".join(f'<a href="{f}">{n}</a>' for f, n in NAV[1:4])
    doc = f"""<!DOCTYPE html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{SITE}/{"" if file == "index.html" else file}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Player Performance">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{SITE}/{"" if file == "index.html" else file}">
<meta property="og:image" content="{SITE}/hero-player.jpg">
<meta name="theme-color" content="#0B0B0D">{extra_head}
<link rel="icon" href="img/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="styles.css?v={STYLE_V}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="wrap"><span>Youth football development · Ages 4–16 · Sutton-in-Ashfield</span><span class="topbar-right"><span class="socials">{SOCIAL_ICONS}</span><a class="hide-sm" href="{SIGNIN}">Parent portal login</a></span></div></div>
<header class="header" id="top"><div class="wrap">
  <a class="logo" href="index.html" aria-label="Player Performance home"><img src="img/logo-white.png" alt="Player Performance"></a>
  <button class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
  <nav class="nav" id="site-nav" aria-label="Main">{nav}</nav>
  <div class="actions"><a class="btn btn-ghost btn-sm" href="{SIGNIN}">Portal login</a><a class="btn btn-pink btn-sm" href="group-sessions.html#timetable">Book a session</a></div>
</div></header>
<main id="main">
{body}
</main>
<footer class="footer"><div class="wrap">
  <div class="cols">
    <div><a class="logo" href="index.html"><img src="img/logo-white.png" alt="Player Performance"></a><p>Built for players who want more. Football development for 4 to 16 year olds at PP HQ, Sutton-in-Ashfield.</p></div>
    <div><h4>Coaching</h4>{foot_links}<a href="{PORTAL}/parent/spaces">Spare spaces this week</a></div>
    <div><h4>Parents</h4><a href="{SIGNIN}">Portal login</a><a href="reviews.html">Parent reviews</a><a href="faqs.html">FAQs</a><a href="contact.html">Contact us</a></div>
    <div><h4>Find us</h4><p>PP HQ, Units 2 &amp; 3, Springbank House,<br>2 Craster Street, Sutton-in-Ashfield NG17 5AG</p><a href="mailto:{EMAIL}">{EMAIL}</a><a href="{INSTA}">Instagram @playerperformanceuk</a></div>
  </div>
  <div class="legal"><span>© 2026 Player Performance</span><span><a href="contact.html" style="display:inline">Privacy</a> · <a href="contact.html" style="display:inline">Terms</a></span></div>
</div></footer>
<dialog class="lightbox" aria-label="Photo"><img alt=""><button type="button" class="lb-close" aria-label="Close">Close</button></dialog>
<script>
  (function () {{
    var h = document.querySelector('.header'), b = document.querySelector('.menu-btn');
    if (b) b.addEventListener('click', function () {{ var o = h.classList.toggle('open'); b.setAttribute('aria-expanded', o ? 'true' : 'false'); b.textContent = o ? 'Close' : 'Menu'; }});
    var f = document.querySelector('form[data-enquiry]');
    if (f) f.addEventListener('submit', function (e) {{
      e.preventDefault();
      var ok = f.querySelector('.notice.ok'), bad = f.querySelector('.notice.bad'), btn = f.querySelector('button[type=submit]');
      ok.style.display = 'none'; bad.style.display = 'none';
      if (!f.contact_name.value.trim() || (!f.contact_email.value.trim() && !f.contact_phone.value.trim())) {{ bad.textContent = 'Please add your name and an email address or phone number.'; bad.style.display = 'block'; return; }}
      var d = {{}}; ['contact_name','contact_email','contact_phone','message','experience','interest','group','company_website'].forEach(function (k) {{ if (f[k] && f[k].value.trim()) d[k] = f[k].value.trim(); }});
      var age = parseInt(f.child_age.value, 10); if (age >= 3 && age <= 18) d.child_age = age;
      if (f.waitlist.value) d.waitlist = true;
      btn.disabled = true; btn.textContent = 'Sending...';
      fetch('{PORTAL}/api/leads/enquiry', {{ method: 'POST', headers: {{ 'content-type': 'application/json' }}, body: JSON.stringify(d) }})
        .then(function (r) {{ if (!r.ok) throw new Error(r.status); ok.style.display = 'block'; f.reset(); }})
        .catch(function () {{ bad.textContent = "Sorry, that didn't send. Please try again, or email us at {EMAIL}."; bad.style.display = 'block'; }})
        .then(function () {{ btn.disabled = false; btn.textContent = 'Send message'; }});
    }});
    var tabs = document.querySelectorAll('.tt-tab');
    function showTab(k) {{ tabs.forEach(function (t) {{ var on = t.id === 'tab-' + k; t.setAttribute('aria-selected', on ? 'true' : 'false'); document.getElementById(t.getAttribute('aria-controls')).hidden = !on; }}); document.querySelectorAll('.price-panel').forEach(function (p) {{ p.hidden = p.dataset.for !== k; }}); }}
    tabs.forEach(function (t) {{ t.addEventListener('click', function () {{ showTab(t.id.slice(4)); }}); }});
    if (tabs.length && /^#tt-(debdale|goalkeeping)$/.test(location.hash)) showTab(location.hash.slice(4));
    var fd = document.querySelector('.full-dialog');
    document.querySelectorAll('.js-full').forEach(function (b) {{ b.addEventListener('click', function () {{ if (!fd) return; var g = b.dataset.group; fd.querySelector('.full-group').textContent = g; fd.querySelector('.full-link').href = 'contact.html?waitlist=1&group=' + encodeURIComponent(g); fd.showModal(); }}); }});
    if (fd) {{ fd.querySelector('.full-close').addEventListener('click', function () {{ fd.close(); }}); fd.addEventListener('click', function (e) {{ if (e.target === fd) fd.close(); }}); }}
    var qs = new URLSearchParams(location.search), grp = qs.get('group'), form = document.querySelector('.form');
    if (form && grp) {{
      var msg = form.querySelector('[name=message]'), sel = form.querySelector('[name=interest]');
      if (msg) msg.value = qs.get('waitlist') ? 'Please add my child to the waiting list for: ' + grp + '.' : (/1-2-1/.test(grp) ? "I'd like to ask about " + grp + '.' : "I'd like to book a place for my child in: " + grp + '.');
      if (sel) sel.value = /goalkeep/i.test(grp) ? 'Goalkeeping' : (/1-2-1/.test(grp) ? '1-2-1 coaching' : 'Group sessions');
      if (form.group) form.group.value = grp; if (form.waitlist && qs.get('waitlist')) form.waitlist.value = '1';
      var nm = form.querySelector('[name=contact_name]'); if (nm) nm.focus();
    }}
    var dlg = document.querySelector('.lightbox');
    document.querySelectorAll('.g-tile[data-full]').forEach(function (t) {{ t.addEventListener('click', function () {{ if (!dlg) return; var i = dlg.querySelector('img'); i.src = t.dataset.full; i.alt = t.querySelector('img').alt; dlg.showModal(); }}); }});
    if (dlg) dlg.addEventListener('click', function () {{ dlg.close(); }});
  }})();
</script>
</body>
</html>
"""
    for a in ("img/barcelona/", "img/paris/", "img/"):
        doc = doc.replace(a, "")
    (OUT / file).write_text(doc, encoding="utf-8")


# Photo galleries: add (file, description) pairs and the page fills itself in.
GALLERIES = {"barcelona": [('img/barcelona/bcn-1.jpg', 'The team with their medals on the Barcelona Girls Cup stage'), ('img/barcelona/bcn-2.jpg', "The older girls' team with their medals and trophy on the Barcelona Girls Cup stage"), ('img/barcelona/bcn-3.jpg', 'Players celebrating with the trophy on the Barcelona Girls Cup stage'), ('img/barcelona/bcn-4.jpg', 'The girls lifting the trophy at the Barcelona Girls Cup'), ('img/barcelona/bcn-5.jpg', 'The squad and coaches with the PP On Tour banner in Barcelona'), ('img/barcelona/bcn-6.jpg', 'The younger girls and coaches with the PP On Tour banner in Barcelona')], "paris": [('img/paris/paris-1.jpg', 'The squad and coaches with their medals, trophies and the PP On Tour banner in Paris'), ('img/paris/paris-2.jpg', "The boys' team lined up arm in arm in Paris"), ('img/paris/paris-3.jpg', 'Players on the pitch at the Paris International Tournament'), ('img/paris/paris-4.jpg', 'The team in the evening sun at the Paris International Tournament'), ('img/paris/paris-5.jpg', 'Four players with the PP On Tour banner at the airport on the way to Paris'), ('img/paris/paris-6.jpg', 'The team with their medals at the Paris International Tournament')]}


def gallery(key, title, empty_note):
    items = GALLERIES.get(key, [])
    if not items:
        tiles = "".join(f'<div class="g-tile">{photo(f"{title} photo {i}", empty_note)}</div>' for i in range(1, 7))
    else:
        tiles = "".join(f'<button type="button" class="g-tile" data-full="{src}" aria-label="Open photo: {html.escape(alt)}"><img src="{src}" alt="{html.escape(alt)}" loading="lazy"></button>' for src, alt in items)
    return f'<div class="gallery" aria-label="{html.escape(title)} photo gallery">{tiles}</div>'


def cta_band(title="Ready to get better?", text="Book your child's first session or ask us anything."):
    return f"""<section class="cta-band"><div class="wrap"><div><h2>{title}</h2><p style="margin:0;opacity:.9">{text}</p></div>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-dark arrow" href="group-sessions.html#timetable">See the timetable </a><a class="btn btn-ghost" href="contact.html">Contact us</a></div></div></section>"""


# ---------------------------------------------------------------- Home
home = f"""
<section class="hero"><div class="wrap">
  <div>
    <p class="eyebrow">Football development · Ages 4–16</p>
    <h1>Built for players <span class="pink">who want more.</span></h1>
    <p class="lead">We offer group development sessions, small group training and 1-2-1 football coaching, along with our goalkeeper sessions. Based in Sutton-in-Ashfield and Mansfield Woodhouse, we help young players of all ages find their potential and build the confidence to use it on match day.</p>
    <div class="cta"><a class="btn btn-pink arrow" href="group-sessions.html#timetable">Book a session </a><a class="btn btn-line" href="{SIGNIN}">Parent portal</a></div>
    <p class="tagline">Detail · Intensity · Results</p>
  </div>
  {photo("Hero photo", src="img/hero-player.jpg", alt="A Player Performance player in PP kit dribbling the ball on the 4G pitch at PP HQ", pos="center 40%")}
</div></section>

<section class="dark"><div class="wrap">
  <div class="stats">
    <div class="stat"><b>4–16+</b><span>Ages we coach</span></div>
    <div class="stat"><b>250+</b><span>Children attending weekly</span></div>
    <div class="stat"><b>Indoor 4G</b><span>All-weather pitch at PP HQ</span></div>
    <div class="stat"><b>FA &amp; UEFA</b><span>Qualified coaches</span></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">What we offer</p><h2>Train with us</h2></div><p class="lead">Pick the way that suits your child. All abilities welcome.</p></div>
  <div class="grid g4">
    <a class="card card-link" href="group-sessions.html">{photo("Group session photo", wide=True, src="img/group-session.jpg", alt="Two players racing for the ball during a session on the 4G pitch at PP HQ, with parents watching", pos="40% 60%")}<h3>Group sessions</h3><p>Weekly small-group sessions by age and level, Monday to Friday, 4:30pm to 9:30pm.</p><span class="btn btn-line btn-sm arrow">See the timetable </span></a>
    <a class="card card-link" href="1-2-1.html">{photo("1-2-1 photo", wide=True, src="img/one-to-one.jpg", alt="A Player Performance player in PP kit, focused and ready to move, at PP HQ", pos="center 30%")}<h3>1-2-1 coaching</h3><p>Private sessions built around exactly what your child needs to work on.</p><span class="btn btn-line btn-sm arrow">Find out more </span></a>
    <a class="card card-link" href="goalkeeping.html">{photo("Goalkeeping photo", wide=True, src="img/goalkeeping.jpg", alt="A young goalkeeper crouched by the post, holding the ball safely in her gloves", pos="center 42%")}<h3>Goalkeeping coaching</h3><p>Specialist goalkeeper sessions on Fridays at Debdale Park: handling, diving, footwork and distribution for U9s to U13s.</p><span class="btn btn-line btn-sm arrow">Find out more </span></a>
    <a class="card card-link" href="camps.html">{photo("Camp photo", wide=True, src="img/camp.jpg", alt="Players on the indoor 4G pitch at PP HQ during a camp, with footballs ready for the next drill", pos="center 60%")}<h3>Camps</h3><p>Technical camps for children who want to improve over half term.</p><span class="btn btn-line btn-sm arrow">See camp dates </span></a>
  </div>
</div></section>

<section class="white"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">The PP way</p><h2>Four things we work on</h2></div><p class="lead">Every session builds the whole player, not just the drills.</p></div>
  <div class="grid g4">
    <div class="card"><span class="num">01</span><h3>Technical</h3><p>First touch, passing, dribbling, 1v1s and overload scenarios. Lots of touches on the ball in small and big spaces.</p></div>
    <div class="card"><span class="num">02</span><h3>Tactical</h3><p>Knowing where to be, when to pass and how to make good decisions under pressure.</p></div>
    <div class="card"><span class="num">03</span><h3>Physical</h3><p>Speed, agility, balance and strength, matched to your child's age.</p></div>
    <div class="card"><span class="num">04</span><h3>Psychological</h3><p>Confidence, focus and a never-give-up attitude, so players can perform when it matters.</p></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="grid g2" style="align-items:center;gap:48px">
    <div class="phone-shot"><img src="img/portal-phone.jpg" alt="The Player Performance parent portal on a phone, showing My bookings, Progress, Offers and Camps" loading="lazy"></div>
    <div><p class="eyebrow">For parents</p><h2>Everything in one place</h2><p class="lead">Our parent portal keeps it simple: tell us if your child is coming, see their next sessions, book spare spaces and follow their progress from their coaches.</p>
    <ul class="ticks"><li>Attending or not, in one tap</li><li>Spare spaces offered first to our families</li><li>Monthly progress reports from your coaches</li><li>Notifications straight to your phone</li></ul>
    <a class="btn btn-dark arrow" href="{SIGNIN}">Go to the parent portal </a></div>
  </div>
</div></section>

<section class="white"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">Parents say</p><h2>Reviews</h2></div><a class="btn btn-line arrow" href="reviews.html">More about our reviews </a></div>
  <div class="tp-card">
    <div class="tp-score"><span class="tp-stars" aria-hidden="true">★★★★★</span><b>Excellent</b><span>Rated <strong>4.7 out of 5</strong> from <strong>41+ reviews</strong> on Trustpilot</span></div>
    <div class="tp-actions"><a class="btn arrow" href="https://uk.trustpilot.com/review/playerperformance.uk" target="_blank" rel="noopener">Read our reviews </a><a class="btn btn-line arrow" href="https://uk.trustpilot.com/evaluate/playerperformance.uk" target="_blank" rel="noopener">Leave a review </a></div>
  </div>
  <div class="grid g2" style="margin-top:24px">
    <div class="review"><div class="stars">★★★★★</div><p>The best place we have found to develop our boys ⚽️ Top coaches that bring out the absolute best in the children that attend no matter their ability! Wouldn't want them anywhere else.</p><cite>Emily · Google review</cite></div>
    <div class="review"><div class="stars">★★★★★</div><p>Excellent football coaching! The sessions are well organised, engaging and enjoyable. The coach is supportive and encouraging, helping the children build their confidence, improve their skills and develop a real love for football. It's great to see the progress the children are making. Highly recommended</p><cite>EB · Trustpilot review</cite></div>
    <div class="review"><div class="stars">★★★★★</div><p>The best place to be! Dev absolutely loves his sessions at Player Performance... The coaches Jaz, Tomo, Ty, everyone is super friendly. They give every child their attention and work with them through their strengths and weaknesses. The sessions are intense and fun at the same time... I am so grateful to the team for how much support they have given to Dev and would recommend to anyone looking for a place where their child can truly feel supported, can grow in skills and confidence and come out feeling very happy.</p><cite>Payel · Trustpilot review</cite></div>
    <div class="review"><div class="stars">★★★★★</div><p>Great coaches and great set up for kids that want to get their football skills to that next level! All coaches are brilliant with the kids and make the sessions challenging but still fun! My son loves it and would highly recommend them.</p><cite>Mrs S. C · Trustpilot review</cite></div>
  </div>
</div></section>
{cta_band()}
"""
page("index.html", "Player Performance | Youth football coaching in Sutton-in-Ashfield",
     "Football development coaching for 4 to 16 year olds at PP HQ, Sutton-in-Ashfield: weekly group sessions, 1-2-1 coaching, goalkeeping and half term camps.", home)

# ---------------------------------------------------------------- Group sessions
TT = {
 "Monday": [("4:30–6pm", "U8s & U9s", "", "few"), ("5:30–7pm", "U10s & U11s", "", "full"), ("6:30–8pm", "U12s & U13s", "High level", "few"), ("7:30–9pm", "U14+", "High level", "full")],
 "Tuesday": [("4:30–6pm", "U9s & U10s", "", "full"), ("5:30–7pm", "U10s & U11s", "High level", "full"), ("6:30–8pm", "U12s & U13s", "High level", "few"), ("7:30–9pm", "U14+", "High level", "full")],
 "Wednesday": [("4–5pm", "Minis ages 4 to 6", "", "full"), ("4:30–6pm", "U7s & U8s", "", "few"), ("5:30–7pm", "U9s & U10s", "", "few"), ("6:30–8pm", "U10s & U11s", "", "few"), ("7:30–9pm", "U12s & U13s", "", "few"), ("8:15–9:30pm", "U14+", "High level", "full")],
 "Thursday": [("4:30–6pm", "U9s & U10s", "", "full"), ("5:30–7pm", "U10s & U11s", "High level", "few"), ("6:30–8pm", "U11s & U12s", "High level", "full"), ("7:30–9pm", "U14+", "High level", "full")],
 "Friday": [("4:30–6pm", "U9s & U10s", "High level", "few"), ("5:30–7pm", "U9s & U10s", "High level", "full"), ("6:30–8pm", "All Girls U10s & U11s", "Girls only", "few"), ("7:30–9pm", "U14+", "High level", "full")],
}
DAY_SUB = {"Monday": "Group development", "Tuesday": "Group development", "Wednesday": "Minis &amp; group development",
           "Thursday": "Group development", "Friday": "Group development"}
DAY_NOTE = {
 "Monday": ("1-2-1s with Coach Ty Short", "Ask us for available times"),
 "Tuesday": ("1-2-1s / small groups with Coach Jaz Goundry", "Ask us for available times"),
 "Wednesday": ("1-2-1s with Coach Ty Short", "Ask us for available times"),
 "Thursday": ("1-2-1s / small groups with Coach Jaz Goundry", "Ask us for available times"),
}
DEBDALE = [
 ("Groups with Coach Ty Short", [("6:30–7:30pm", "U8s & U9s", "Mixed", 2), ("7:30–8:30pm", "All Girls U12s & U13s", "Girls only", "full")]),
 ("Goalkeeping with Coach Joe Marson", [("6:30–7:30pm", "U9s & U10s", "Goalkeepers", 2), ("7:30–8:30pm", "U11s, U12s & U13s", "Goalkeepers", "full")]),
]
LABEL = {"full": "Full", "few": "1 space left", "open": "Spaces available"}


def status(s):
    if isinstance(s, int):
        return ("few", f"{s} spaces left" if s != 1 else "1 space left")
    return (s, LABEL[s])


def slot_rows(slots, where=""):
    from urllib.parse import quote
    out = ""
    for t, g, n, s in slots:
        cls, lab = status(s)
        label = f"{where} {t} {g}".strip()
        q = quote(label)
        if cls == "full":
            btn = f'<button type="button" class="pill full js-full" data-group="{html.escape(label)}" aria-label="{html.escape(label)} is full. Join the waiting list">Full</button>'
        else:
            btn = f'<a class="pill {cls} pill-book" href="contact.html?group={q}" aria-label="Book {html.escape(label)}: {lab}">{lab} · Book</a>'
        out += f'<div class="slot"><span class="time">{t}</span><span class="group">{g}{f"<small>{n}</small>" if n else ""}</span>{btn}</div>'
    return out


hq = '<div class="venue-head"><h3>PP HQ</h3><p>Springbank House, 2 Craster Street, Sutton-in-Ashfield NG17 5AG · Monday to Friday</p></div><div class="days">'
for d, slots in TT.items():
    note = DAY_NOTE.get(d)
    if note:
        from urllib.parse import quote
        nq = quote(f"{d} (PP HQ) {note[0]}")
        note_html = f'<div class="day-note"><div>{note[0]}<small>{note[1]}</small></div><a class="btn btn-pink btn-sm arrow" href="contact.html?group={nq}">Contact us </a></div>'
    else:
        note_html = ""
    hq += f'<div class="day"><h3>{d}</h3><div class="day-sub">{DAY_SUB[d]}</div>{slot_rows(slots, f"{d} (PP HQ)")}{note_html}</div>'
hq += '</div>'
deb_head = '<div class="venue-head"><h3>Debdale Park Sports Club</h3><p>Mansfield Woodhouse, NG19 7NS · Fridays</p></div>'
deb_panels = []
for title, slots in DEBDALE:
    deb_panels.append(deb_head + f'<div class="days"><div class="day"><h3>Friday</h3><div class="day-sub">{title}</div>{slot_rows(slots, "Friday (Debdale)" + (" Goalkeeping" if "Goalkeeping" in title else ""))}</div></div>')
TABS = [("hq", "PP HQ", hq), ("debdale", "Debdale group sessions", deb_panels[0]), ("goalkeeping", "Debdale goalkeeping", deb_panels[1])]
days = '<div class="tt-tabs" role="tablist" aria-label="Choose a venue">' + "".join(
    f'<button type="button" role="tab" id="tab-{k}" aria-controls="tt-{k}" aria-selected="{"true" if n == 0 else "false"}" class="tt-tab">{lab}</button>'
    for n, (k, lab, _) in enumerate(TABS)) + '</div>'
days += "".join(f'<div class="tt-panel" role="tabpanel" id="tt-{k}" aria-labelledby="tab-{k}"{"" if n == 0 else " hidden"}>{body}</div>' for n, (k, _, body) in enumerate(TABS))

def price_card(title, price, ticks, featured=False):
    lis = "".join(f"<li>{t}</li>" for t in ticks)
    return (f'<div class="card{" featured" if featured else ""}"><h3>{title}</h3><div class="price">£{price}<small>a month</small></div>'
            f'<ul class="ticks">{lis}</ul><a class="btn {"btn-pink" if featured else "btn-line"} btn-sm arrow" href="contact.html">Ask about a place </a></div>')
PRICES = {
 "hq": [price_card("Minis", 32, ["1 session a week", "Wednesday 4–5pm", "Ages 4 to 6"]),
        price_card("90 minute session", 77, ["1 session a week", "90 minutes", "Monthly progress report"], True),
        price_card("60 minute session", 65, ["1 session a week", "60 minutes", "Monthly progress report"])],
 "debdale": [price_card("Debdale group sessions", 65, ["1 session a week", "Fridays, 60 minutes", "Debdale Park, Mansfield Woodhouse"], True)],
 "goalkeeping": [price_card("Debdale goalkeeping", 60, ["1 session a week", "Fridays, 60 minutes", "With Coach Joe Marson"], True)],
}
price_panels = "".join(
    f'<div class="price-panel" data-for="{k}"{"" if n == 0 else " hidden"}><div class="grid g3">{"".join(cards)}</div></div>'
    for n, (k, cards) in enumerate(PRICES.items()))

groups = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Group sessions</p><h1>Weekly group<br>development</h1>
<p class="lead">Small groups by age and level, Monday to Friday at PP HQ. 60 and 90 minute sessions available. Indoor venue, so weather cancellations are never an issue.</p>
<a class="btn btn-pink arrow" href="#timetable">See the timetable </a></div></section>

<section><div class="wrap">
  <div class="grid g3">
    <div class="card"><h3>Small groups</h3><p>A maximum of 10 players per group, so every child gets coached, not just supervised.</p></div>
    <div class="card"><h3>Right level</h3><p>Groups by age, with High Level groups for players ready for more challenge.</p></div>
    <div class="card"><h3>All weather</h3><p>Indoor 4G pitch at PP HQ, so sessions go ahead in the rain and the dark.</p></div>
  </div>
</div></section>

<section class="white" id="timetable"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">This term</p><h2>Timetable</h2></div><p class="lead">Spaces go quickly. Once your child is signed up, you'll manage everything in the parent portal.</p></div>
  {todo("When live, spaces update automatically from the portal")}
  <div class="legend"><span class="pill full">Full</span><span class="pill few">1 space left</span><span class="pill open">Spaces available</span></div>
  {days}
</div></section>
<dialog class="full-dialog" aria-labelledby="full-title">
  <h3 id="full-title">This group is full</h3>
  <p class="full-group"></p>
  <p>To join the waiting list, please contact us and we'll let you know as soon as a place comes up.</p>
  <div class="full-actions"><a class="btn btn-pink arrow full-link" href="contact.html">Contact us </a><button type="button" class="btn btn-line full-close">Close</button></div>
</dialog>

<section><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">Monthly membership</p><h2>Prices</h2></div><p class="lead">Paid monthly by card through Square. Cancel any time with a month's notice.</p></div>
  {price_panels}
</div></section>

<section class="dark" id="girls"><div class="wrap">
  <div class="grid g2" style="align-items:center;gap:48px">
    <div><p class="eyebrow">Girls football</p><h2>All Girls group</h2><p class="lead">Fridays 6:30–8pm for U10s and U11s. A group built for girls, with the same high standards as every PP session. Girls are welcome in all our mixed groups too.</p>
    {todo()}
    <a class="btn btn-pink arrow" href="contact.html">Ask about a place </a></div>
    {photo("Girls group photo", wide=True, src="img/barcelona-girls.jpg", alt="The Player Performance girls squad in their pink and black kit", pos="center 55%")}
  </div>
</div></section>

<section class="white"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Already with us?</p><h2>Spare spaces</h2></div></div>
<p class="lead">When a child can't make it, we offer the space to other PP families as a one-off: £15 for 60 minutes, £17.50 for 90 minutes. Offers go out at 10am on session days through the parent portal.</p>
<a class="btn btn-dark arrow" href="{PORTAL}/parent/spaces">See spare spaces </a></div></section>
{cta_band("Find the right group", "Not sure which group fits? Tell us your child's age and we'll help.")}
"""
page("group-sessions.html", "Group sessions | Player Performance",
     "Weekly small-group football development for ages 4 to 16 at PP HQ, Sutton-in-Ashfield. Timetable, groups and prices.", groups)

# ---------------------------------------------------------------- 1-2-1
one = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">1-2-1 coaching · Ages 6+</p><h1>Individual<br>development</h1>
<p class="lead">Private sessions built around your child's age, ability and goals. We focus on the details that make the biggest difference to their game.</p>
<a class="btn btn-pink arrow" href="contact.html">Ask about availability </a></div></section>

<section><div class="wrap"><div class="grid g2" style="align-items:center;gap:48px">
  {photo("1-2-1 photo", src="img/one-to-one.jpg", alt="A Player Performance player in PP kit, focused and ready to move, at PP HQ", pos="center 35%")}
  <div><p class="eyebrow">Why 1-2-1</p><h2>Work on what matters most</h2>
  {todo()}
  <p class="lead">Every 1-2-1 starts with what your child wants to get better at. Then we build sessions to get them there, and track it in their progress report.</p>
  <ul class="ticks"><li>First touch, weak foot and ball mastery</li><li>1v1 attacking and defending</li><li>Position-specific work</li><li>Confidence and decision making</li></ul></div>
</div></div></section>

<section class="white"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">Prices</p><h2>1-2-1 packages</h2></div></div>
  {todo("Placeholder: check prices")}
  <div class="grid g2">
    <div class="card"><h3>Block of 4</h3><div class="price">£120</div><ul class="ticks"><li>Four 1-2-1 sessions</li><li>Plan built for your child</li><li>Progress notes after each block</li></ul><a class="btn btn-line btn-sm arrow" href="contact.html">Enquire </a></div>
    <div class="card featured"><span class="badge">Best value</span><h3>Quarter (12 sessions)</h3><div class="price">£330</div><ul class="ticks"><li>Twelve 1-2-1 sessions</li><li>Longer-term plan and goals</li><li>Progress report every month</li></ul><a class="btn btn-pink btn-sm arrow" href="contact.html">Enquire </a></div>
  </div>
</div></section>
{cta_band("Book a 1-2-1", "Tell us what your child wants to work on and we'll find a time.")}
"""
page("1-2-1.html", "1-2-1 football coaching | Player Performance",
     "Private 1-2-1 football coaching for ages 6+ at PP HQ, Sutton-in-Ashfield, built around your child's goals.", one)

# ---------------------------------------------------------------- Goalkeeping
gk = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Goalkeeping · U9s to U13s</p><h1>Goalkeeper<br>coaching</h1>
<p class="lead">Specialist sessions just for goalkeepers, every Friday at Debdale Park Sports Club in Mansfield Woodhouse. Small groups, lots of saves, and the confidence to command their box on match day.</p>
<a class="btn btn-pink arrow" href="contact.html">Ask about a place </a></div></section>

<section><div class="wrap"><div class="grid g2" style="align-items:center;gap:48px">
  {photo("Goalkeeping photo", src="img/goalkeeping.jpg", alt="A young goalkeeper crouched by the post, holding the ball safely in her gloves", pos="center 35%")}
  <div><p class="eyebrow">What we work on</p><h2>Everything a keeper needs</h2>
  <p class="lead">Goalkeeping is a position of its own, so it gets its own coaching. Every session is planned around the age and level of the group.</p>
  <ul class="ticks"><li><b>Handling:</b> catching, holding and dealing with crosses</li><li><b>Diving:</b> technique, getting up quickly and staying safe</li><li><b>Footwork:</b> set position, moving across goal and angles</li><li><b>Distribution:</b> throwing, kicking and playing out from the back</li><li><b>Communication:</b> organising the defence and calling for the ball</li></ul></div>
</div></div></section>

<section><div class="wrap"><div style="max-width:760px">
  <div><p class="eyebrow">Meet the coach</p><h2>Joe Marson</h2>
  <p class="lead">We are delighted to bring Joe Marson in as our new goalkeeper coach. A former Mansfield Town goalkeeper, Joe brings first-hand experience from the game and will now be helping the next generation of aspiring goalkeepers.</p></div>
</div></div></section>

<section class="white"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">Timetable</p><h2>Fridays at Debdale</h2></div><p class="lead">Debdale Park Sports Club, Mansfield Woodhouse, NG19 7NS.</p></div>
  <div class="grid g2">
    <div class="card"><h3>U9s &amp; U10s</h3><div class="price">6:30<small>to 7:30pm</small></div><ul class="ticks"><li>Every Friday</li><li>60 minutes</li><li>Boys and girls</li></ul></div>
    <div class="card"><h3>U11s, U12s &amp; U13s</h3><div class="price">7:30<small>to 8:30pm</small></div><ul class="ticks"><li>Every Friday</li><li>60 minutes</li><li>Boys and girls</li></ul></div>
  </div>
  <div class="card featured" style="margin-top:24px"><h3>Price</h3><div class="price">£60<small>a month</small></div><p>One goalkeeping session a week, paid monthly.</p><a class="btn btn-pink btn-sm arrow" href="contact.html">Book a place </a></div>
</div></section>
{cta_band("Got a keeper?", "Ask us about a place in Friday's goalkeeping sessions.")}
"""
page("goalkeeping.html", "Goalkeeper coaching | Player Performance",
     "Specialist goalkeeper coaching for U9s to U13s, Fridays at Debdale Park Sports Club, Mansfield Woodhouse. £60 a month.", gk)

# ---------------------------------------------------------------- Camps
camps = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Camps</p><h1>Half term camps</h1>
<p class="lead">Full days of high-intensity football over half term. Technical and tactical sessions, possession games, tournaments and much more, led by our coaches at PP HQ.</p>
<a class="btn btn-pink arrow" href="#dates">See camp dates </a></div></section>
<section><div class="wrap"><div class="grid g2" style="align-items:center;gap:48px">
  <div><p class="eyebrow">What's it like</p><h2>Fun, full-on days</h2>{todo()}
  <ul class="ticks"><li>Ages 5 to 14, grouped by age</li><li>Skills sessions, matches and competitions</li><li>Indoor 4G pitch, whatever the weather</li><li>Bring a packed lunch and water bottle</li></ul></div>
  {photo("Camp photo", wide=True, src="img/camp.jpg", alt="Players on the indoor 4G pitch at PP HQ during a camp, with footballs ready for the next drill", pos="center 55%")}
</div></div></section>
<section class="white" id="dates"><div class="wrap"><div class="section-head"><div><p class="eyebrow">Coming up</p><h2>Camp dates</h2></div></div>
{todo("Placeholder: send Claude your next camp dates and prices")}
<div class="grid g2">
  <div class="card"><h3>February half term</h3><p>Dates coming soon</p><a class="btn btn-line btn-sm arrow" href="contact.html">Register interest </a></div>
  <div class="card"><h3>Easter camp</h3><p>Dates coming soon</p><a class="btn btn-line btn-sm arrow" href="contact.html">Register interest </a></div>
</div></div></section>
{cta_band("Don't miss a camp", "Camps fill up fast. Register your interest and we'll tell you first.")}
"""
page("camps.html", "Half term camps | Player Performance", "Half term football camps at PP HQ, Sutton-in-Ashfield.", camps)

# ---------------------------------------------------------------- Tournaments
tour = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">International experiences</p><h1>Taking PP<br>abroad</h1>
<p class="lead">Playing in international tournaments gives our players a taste of the game at the next level: new opponents, new styles of football and memories that last for ever.</p>
<a class="btn btn-pink arrow" href="#next-year">See next year's trips </a></div></section>

<section><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">2026</p><h2>This year</h2></div><p class="lead">Where our players went this year.</p></div>
  <div class="grid g2">
    <div class="card">{photo("Barcelona Girls Cup photo", wide=True, src="img/barcelona-girls.jpg", alt="The Player Performance girls squad in their pink and black kit, lined up for a team photo", pos="center 55%")}<span class="tag">Girls</span><h3>Barcelona Girls Cup</h3><p>Our girls travelled to Barcelona to take on teams from across Europe at the Barcelona Girls Cup.</p>{todo("Optional: add a line on how it went")}</div>
    <div class="card">{photo("Paris tournament photo", wide=True, src="img/paris/paris-1.jpg", alt="The squad and coaches with their medals, trophies and the PP On Tour banner in Paris", pos="center 72%")}<span class="tag">Boys &amp; girls</span><h3>Paris International Tournament</h3><p>Our boys' and girls' teams headed to Paris to compete at the Paris International Tournament.</p>{todo("Optional: add a line on how it went")}</div>
  </div>
  <h3 class="gallery-title" id="barcelona-video">Barcelona Girls Cup video</h3>
  <div class="reel"><iframe src="https://www.instagram.com/reel/DZZjYyttnZN/embed" title="Barcelona Girls Cup video on Instagram" loading="lazy" allowtransparency="true" allowfullscreen scrolling="no"></iframe></div>
  <h3 class="gallery-title" id="barcelona-gallery">Barcelona Girls Cup gallery</h3>
  {gallery("barcelona", "Barcelona Girls Cup", "Photo from Barcelona")}
  <h3 class="gallery-title" id="paris-gallery">Paris International Tournament gallery</h3>
  {gallery("paris", "Paris International Tournament", "Photo from Paris")}
</div></section>

<section class="white" id="next-year"><div class="wrap">
  <div class="section-head"><div><p class="eyebrow">2027</p><h2>Next year</h2></div><p class="lead">Two trips confirmed. Both fully booked.</p></div>
  <div class="grid g2">
    <div class="card featured"><span class="badge">Coming back</span>{photo("Barcelona photo", wide=True, src="img/barcelona-girls.jpg", alt="The Player Performance girls squad", pos="center 55%")}<span class="tag">Girls</span><h3>Barcelona Girls Cup</h3><p>We're going back to the Barcelona Girls Cup, and this time it's bigger, with more of our girls getting the chance to go.</p>{todo("Dates, ages and price")}<span class="booked">Fully booked</span> <a class="btn btn-line btn-sm arrow" href="contact.html">Join the waiting list </a></div>
    <div class="card featured"><span class="badge">New for 2027</span><h3>Benfica trip</h3><p>A new trip to Lisbon to experience Benfica, one of Europe's most famous clubs.</p>{todo("Who it's for, dates and price")}<span class="booked">Fully booked</span> <a class="btn btn-line btn-sm arrow" href="contact.html">Join the waiting list </a></div>
  </div>
</div></section>
{cta_band("Want your child on the next trip?", "Get in touch and we'll let you know as soon as places open.")}
"""
page("tournaments.html", "International experiences | Player Performance",
     "Player Performance international experiences: the Barcelona Girls Cup, the Paris International Tournament and our 2027 trip to Benfica.", tour)

# ---------------------------------------------------------------- About
about = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">About us</p><h1>Player<br>Performance</h1>
<p class="lead">A football development business in Sutton-in-Ashfield, built to give local players the coaching we wish we'd had.</p></div></section>
<section><div class="wrap"><div class="grid g2" style="align-items:center;gap:48px">
  <div><p class="eyebrow">Our story</p><h2>Why we started</h2>{todo("Placeholder: tell Claude your story")}
  <p class="lead">Player Performance was set up to give young players in Ashfield detailed, high-intensity coaching in a positive environment, so they can find their potential and take it onto the pitch on match day.</p>
  
  <p><b>Winner, Best Start Up</b> at the Discover Ashfield Awards 2026.</p></div>
  {photo("Team photo", src="img/team.jpg", alt="Three Player Performance coaches in PP kit at PP HQ, the one in the middle holding the Discover Ashfield Best Start Up award", pos="center 70%")}
</div></div></section>
<section class="white"><div class="wrap"><div class="section-head"><div><p class="eyebrow">The team</p><h2>Our coaches</h2></div></div>
<div class="grid g4">
  <div class="card"><h3>Jaz Goundry</h3></div>
  <div class="card"><h3>Tomo Usher</h3></div>
  <div class="card"><h3>Ty Short</h3></div>
  <div class="card"><h3>Joe Marson</h3></div>
</div></div></section>
<section class="dark"><div class="wrap"><div style="max-width:760px">
  <div><p class="eyebrow">Our home</p><h2>PP HQ</h2><p class="lead">Our own indoor 4G facility at Springbank House, Sutton-in-Ashfield. Sessions go ahead all year round, whatever the weather.</p>
  <p style="color:rgba(255,255,255,.7)">Units 2 &amp; 3, Springbank House, 2 Craster Street, Sutton-in-Ashfield NG17 5AG</p></div>
</div></div></section>
{cta_band()}
"""
page("about.html", "About us | Player Performance", "About Player Performance, our coaches and PP HQ in Sutton-in-Ashfield.", about)

# ------------------------------------------------------------------ Careers
careers = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Careers</p><h1>We're growing our team</h1>
<p class="lead">Join us. Make a difference.</p></div></section>

<section class="white"><div class="wrap" style="max-width:720px">
  <figure style="margin:0 0 16px"><img src="img/careers-coaching.jpg" alt="A Player Performance coach working with a group of young players at PP HQ" loading="lazy" style="width:100%;border-radius:12px"></figure>
  <p>Player Performance is looking to add to our coaching team. We coach children aged 4–16, Monday to Friday, from 1-to-1 sessions to groups of 10. Holding a high standard for every player to find their potential and show it on match day.</p>
  <p style="text-align:center;color:var(--ink-50);font-size:.95rem;margin-bottom:48px">Coaching the next generation at PP HQ, Sutton-in-Ashfield.</p>
  <p style="font-size:1.15rem;line-height:1.7">As a coach with us, you'll deliver engaging sessions, develop players and help build an environment where young people genuinely get better. If you think you'd be a good fit, fill in the form below.</p>
</div></section>

<section><div class="wrap"><div class="grid g2" style="gap:48px">
  <div>
    <h2>Requirements</h2>
    <ul class="ticks">
      <li>Experience coaching football</li>
      <li>Have or working towards FA Level 2 / UEFA C qualification or equivalent</li>
      <li>Energetic, enthusiastic and passionate about the game</li>
      <li>Committed to making a positive difference to young players</li>
      <li>Reliable, professional and able to work independently</li>
    </ul>
    <h2 style="margin-top:40px">What you get</h2>
    <ul class="ticks">
      <li>1–3 evenings of coaching per week, with flexible opportunities</li>
      <li>Competitive pay</li>
      <li>Opportunities to develop your coaching career and gain valuable experience</li>
      <li>Be part of an ambitious, growing football programme</li>
    </ul>
    <p style="margin-top:32px"><b>Any questions?</b><br>Email us at <a href="mailto:{EMAIL}">{EMAIL}</a></p>
  </div>
  <form class="form card" id="careers-form" novalidate>
    <div class="hp" aria-hidden="true"><label>Leave this empty<input name="company_website" tabindex="-1" autocomplete="off"></label></div>
    <h3>Your details</h3>
    <label>Full name<input name="contact_name" autocomplete="name" required maxlength="120"></label>
    <label>Email<input name="contact_email" type="email" autocomplete="email" required maxlength="254"></label>
    <label>Phone<input name="contact_phone" type="tel" autocomplete="tel" maxlength="30"></label>
    <label>Age<input name="applicant_age" inputmode="numeric" maxlength="2"></label>
    <label>Location<input name="applicant_location" maxlength="120" placeholder="e.g. Sutton-in-Ashfield"></label>

    <h3 style="margin-top:24px">Football background</h3>
    <label>Playing experience<textarea name="playing_exp" rows="3" maxlength="1000" placeholder="Where have you played, at what level?"></textarea></label>
    <label>Coaching experience<textarea name="coaching_exp" rows="3" maxlength="1000" placeholder="Where have you coached, age groups, how long?"></textarea></label>
    <label>Qualifications<select name="qualifications"><option value="">Choose one</option><option>FA Level 1</option><option>FA Level 2 / UEFA C</option><option>FA Level 3 / UEFA B or higher</option><option>Working towards a qualification</option><option>Other</option></select></label>

    <h3 style="margin-top:24px">Safeguarding</h3>
    <label>DBS check<select name="dbs_status"><option value="">Choose one</option><option>Yes — Enhanced DBS on the update service</option><option>Yes — Enhanced DBS (not on the update service)</option><option>Yes — Basic DBS</option><option>No — willing to get one</option><option>No</option></select></label>
    <label>First aid certificate<select name="first_aid"><option value="">Choose one</option><option>Yes — in date</option><option>Yes — expired, willing to renew</option><option>No — willing to get one</option><option>No</option></select></label>

    <h3 style="margin-top:24px">Availability</h3>
    <label>Which days and times can you commit to?<textarea name="availability" rows="3" maxlength="500" placeholder="e.g. Monday and Wednesday evenings, flexible on Fridays"></textarea></label>

    <label>Anything else you'd like us to know?<textarea name="extra" rows="3" maxlength="1000"></textarea></label>

    <button class="btn btn-pink" type="submit">Send application</button>
    <p class="notice ok" role="status">Thanks for your application. We'll be in touch soon.</p>
    <p class="notice bad" role="alert">Sorry, that didn't send. Please try again, or email us at {EMAIL}.</p>
  </form>
</div></div></section>
<script>
(function(){
  var f=document.getElementById('careers-form');if(!f)return;
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var ok=f.querySelector('.notice.ok'),bad=f.querySelector('.notice.bad'),btn=f.querySelector('button[type="submit"]');
    if(ok)ok.hidden=true;if(bad)bad.hidden=true;
    var v=function(n){var el=f.querySelector('[name="'+n+'"]');return el?el.value.trim():''};
    if(v('company_website')){return}
    if(!v('contact_name')||(!v('contact_email')&&!v('contact_phone'))){if(bad){bad.textContent='Please fill in your name and either email or phone.';bad.hidden=false}return}
    btn.disabled=true;btn.textContent='Sending...';
    var d={name:v('contact_name'),email:v('contact_email'),phone:v('contact_phone'),age:v('applicant_age'),location:v('applicant_location'),playing_experience:v('playing_exp'),coaching_experience:v('coaching_exp'),qualifications:v('qualifications'),dbs_check:v('dbs_status'),first_aid:v('first_aid'),availability:v('availability'),anything_else:v('extra')};
    fetch('https://app.windmill.dev/api/r/player-performance/careers/apply',{method:'POST',headers:{'content-type':'application/json'},body:JSON.stringify(d)})
    .then(function(r){if(!r.ok)throw new Error(r.status);return r.json()})
    .then(function(){if(ok){ok.hidden=false}f.reset()})
    .catch(function(){if(bad){bad.hidden=false}})
    .then(function(){btn.disabled=false;btn.textContent='Send application'});
  });
})();
</script>
"""
page("careers.html", "Careers | Player Performance", "Join the Player Performance coaching team. We're looking for committed, qualified football coaches in Sutton-in-Ashfield.", careers)

# ---------------------------------------------------------------- Reviews
reviews = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Parent reviews</p><h1>What parents say</h1>
<p class="lead">Don't just take our word for it. Take a look at what the parents think.</p></div></section>
<section><div class="wrap">
  <div class="tp-card">
    <div class="tp-score"><span class="tp-stars" aria-hidden="true">★★★★★</span><b>Excellent</b><span>Rated <strong>4.7 out of 5</strong> from <strong>41+ reviews</strong> on Trustpilot</span></div>
    <div class="tp-actions"><a class="btn arrow" href="https://uk.trustpilot.com/review/playerperformance.uk" target="_blank" rel="noopener">Read our reviews </a><a class="btn btn-line arrow" href="https://uk.trustpilot.com/evaluate/playerperformance.uk" target="_blank" rel="noopener">Leave a review </a></div>
  </div>
  <div class="grid g2" style="margin-top:32px">
    <div class="review"><div class="stars">★★★★★</div><p>The best place we have found to develop our boys ⚽️ Top coaches that bring out the absolute best in the children that attend no matter their ability! Wouldn't want them anywhere else.</p><cite>Emily · Google review</cite></div>
    <div class="review"><div class="stars">★★★★★</div><p>Excellent football coaching! The sessions are well organised, engaging and enjoyable. The coach is supportive and encouraging, helping the children build their confidence, improve their skills and develop a real love for football. It's great to see the progress the children are making. Highly recommended</p><cite>EB · Trustpilot review</cite></div>
    <div class="review"><div class="stars">★★★★★</div><p>The best place to be! Dev absolutely loves his sessions at Player Performance... The coaches Jaz, Tomo, Ty, everyone is super friendly. They give every child their attention and work with them through their strengths and weaknesses. The sessions are intense and fun at the same time... I am so grateful to the team for how much support they have given to Dev and would recommend to anyone looking for a place where their child can truly feel supported, can grow in skills and confidence and come out feeling very happy.</p><cite>Payel · Trustpilot review</cite></div>
    <div class="review"><div class="stars">★★★★★</div><p>Great coaches and great set up for kids that want to get their football skills to that next level! All coaches are brilliant with the kids and make the sessions challenging but still fun! My son loves it and would highly recommend them.</p><cite>Mrs S. C · Trustpilot review</cite></div>
  </div>
  <div class="grid g2" style="margin-top:32px">
    <div class="card"><h3>Had a session with us?</h3><p>We'd love to hear what you think, good or bad. It helps other parents choose and helps us get better.</p><a class="btn btn-line arrow" href="https://uk.trustpilot.com/evaluate/playerperformance.uk" target="_blank" rel="noopener">Review us on Trustpilot </a></div>
    <div class="card"><h3>Prefer Google?</h3><p>You can also read our reviews or leave one on Google.</p><div class="tp-actions"><a class="btn btn-line arrow" href="https://search.google.com/local/writereview?placeid=ChIJN_UokyiVeUgRQ6IYcfJpFl0" target="_blank" rel="noopener">Review us on Google </a><a class="btn btn-line arrow" href="https://search.google.com/local/reviews?placeid=ChIJN_UokyiVeUgRQ6IYcfJpFl0" target="_blank" rel="noopener">Read Google reviews </a></div></div>
  </div>
</div></section>
{cta_band()}
"""
page("reviews.html", "Parent reviews | Player Performance", "Reviews from Player Performance parents.", reviews)

# ---------------------------------------------------------------- FAQs
QA = [
 ("What ages do you coach?", "We coach children from 4 to 16. Our Minis group is for 4 to 6 year olds, and our groups go up to U14+."),
 ("Where are sessions?", "Most sessions are at PP HQ, our indoor 4G pitch at Springbank House, 2 Craster Street, Sutton-in-Ashfield NG17 5AG. Our Friday groups and goalkeeping sessions are at Debdale Park Sports Club, Mansfield Woodhouse, NG19 7NS."),
 ("How do I pay?", "Group sessions are a monthly membership paid by card through Square. 1-2-1s are paid in blocks."),
 ("What should my child bring?", "Football boots or astro trainers, shin pads, a water bottle and comfortable sportswear."),
 ("What if my child can't make a session?", "Tap Not attending in the parent portal. If you know in advance, we can offer the space to another family."),
 ("Do you run girls-only sessions?", "Yes. Our All Girls U10s & U11s group runs on Fridays, 6:30 to 8pm. Girls are welcome in every group too."),
]
faq = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in QA)
faqs = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">FAQs</p><h1>Your questions</h1>
<p class="lead">Everything parents usually ask before their child's first session.</p></div></section>
<section><div class="wrap">{todo("Placeholder: check every answer")}<div class="faq">{faq}</div></div></section>
{cta_band("Still got a question?", "Send us a message and we'll get back to you.")}
"""
page("faqs.html", "FAQs | Player Performance", "Answers to common questions about Player Performance coaching.", faqs)

# ---------------------------------------------------------------- Contact
contact = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Contact</p><h1>Get in touch</h1>
<p class="lead">Ask about a place, a 1-2-1 or a camp. We usually reply within a day.</p></div></section>
<section><div class="wrap"><div class="grid g2" style="gap:48px">
  <form class="form card" data-enquiry novalidate>
    <div class="hp" aria-hidden="true"><label>Leave this empty<input name="company_website" tabindex="-1" autocomplete="off"></label></div>
    <label>Your name<input name="contact_name" autocomplete="name" required maxlength="120"></label>
    <label>Email<input name="contact_email" type="email" autocomplete="email" required maxlength="254"></label>
    <label>Phone (optional)<input name="contact_phone" type="tel" autocomplete="tel" maxlength="30"></label>
    <label>Child's age<input name="child_age" inputmode="numeric" maxlength="2"></label>
    <label>Playing experience<select name="experience"><option value="">Choose one</option><option>New to football</option><option>Plays for fun (school, garden, park)</option><option>Plays for a grassroots team</option><option>Plays at academy or development centre level</option></select></label>
    <label>I'm interested in<select name="interest"><option>Group sessions</option><option>1-2-1 coaching</option><option>Goalkeeping</option><option>Camps</option><option>Something else</option></select></label>
    <label>Message<textarea name="message" rows="5" maxlength="2000"></textarea><input type="hidden" name="group"><input type="hidden" name="waitlist"></label>
    <button class="btn btn-pink" type="submit">Send message</button>
    <p class="notice ok" role="status">Thanks, your message has been sent. We usually reply within a day.</p>
    <p class="notice bad" role="alert">Sorry, that didn't send. Please try again, or email us at {EMAIL}.</p>
  </form>
  <div><h2>Find us</h2><p class="lead">PP HQ, Units 2 &amp; 3, Springbank House, 2 Craster Street, Sutton-in-Ashfield NG17 5AG</p>
  <p><b>Email</b><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
  <p><b>Instagram</b><br><a href="{INSTA}">@playerperformanceuk</a></p>
  <p><b>Facebook</b><br><a href="{FACEBOOK}" target="_blank" rel="noopener">Player Performance on Facebook</a></p>
  <p><b>TikTok</b><br><a href="{TIKTOK}" target="_blank" rel="noopener">@playerperformanceuk</a></p></div>
</div></div></section>
"""
page("contact.html", "Contact | Player Performance", "Contact Player Performance, PP HQ, Sutton-in-Ashfield.", contact)

# ---------------------------------------------------------------- Mindset check-up
MINDSET_Q = [
 ("Making mistakes", "Gets upset or stops trying after a mistake", "Recovers, but it takes a while", "Shakes it off and goes again straight away"),
 ("Confidence on the ball", "Avoids the ball or gets rid of it quickly", "Confident sometimes, depends on the game", "Wants the ball and is happy to take players on"),
 ("Effort when tired", "Drops off when it gets hard", "Keeps going most of the time", "Works hard right to the final whistle"),
 ("Listening to coaches", "Finds it hard to take on feedback", "Listens, but doesn't always try it", "Listens, asks questions and tries new things"),
 ("Bouncing back after a loss", "Stays down for a long time", "Gets over it after a day or so", "Learns from it and looks forward to the next game"),
 ("Nerves before games", "Nerves stop them playing their best", "Nervous, but copes once the game starts", "Calm and excited to play"),
 ("Talking on the pitch", "Very quiet with teammates", "Talks sometimes", "Communicates and encourages others"),
 ("Under pressure", "Panics or hides when pressed", "Copes in some situations", "Stays calm and makes good decisions"),
 ("Practising at home", "Rarely practises outside sessions", "Practises now and then", "Practises regularly on their own"),
 ("Enjoyment", "Often doesn't enjoy football", "Enjoys it most of the time", "Loves playing and can't wait for the next session"),
]
_mq = json.dumps([{"q": q, "red": r, "amber": a, "green": g} for q, r, a, g in MINDSET_Q])
mindset = f"""
<section class="page-hero"><div class="wrap">
<a class="btn btn-pink arrow" href="#questionnaire" style="margin-bottom:28px">Mindset questionnaire </a>
<p class="eyebrow">Mindset</p><h1>Shines in training.<br>A different player on match day?</h1>
<p class="lead">You're not alone. It's the thing we hear from parents more than anything else, and it's the part of the game nobody teaches.</p></div></section>

<section class="white" id="guide"><div class="wrap"><div class="grid g2 gd-grid">
  <div class="gd-cover"><img src="guide-cover.jpg" alt="Cover of the free guide Across the White Line: a mindset guide for players aged 10 to 16" loading="lazy"></div>
  <div>
    <p class="eyebrow">Free guide · Players aged 10–16</p><h2>Across the White Line</h2>
    <p class="lead">Our free 12-page guide for parents and players: why confident trainers freeze on match day, and simple tools to help them take their best self across the white line.</p>
    <form class="form gd-form" novalidate>
      <h3 style="margin:0">Get the free guide</h3>
      <div class="hp" aria-hidden="true"><label>Leave this empty<input name="company_website" tabindex="-1" autocomplete="off"></label></div>
      <label>Your name<input name="parent_name" autocomplete="name" required maxlength="120"></label>
      <label>Email<input name="parent_email" type="email" autocomplete="email" required maxlength="254"></label>
      <label>Phone number<input name="phone" type="tel" autocomplete="tel" required maxlength="20"></label>
      <label class="ms-consent"><span><input type="checkbox" name="consent"> I'm happy for Player Performance to email me the guide and contact me about mindset mentoring.</span></label>
      <p class="notice bad" role="alert"></p>
      <p class="notice ok" role="status">Check your inbox, the guide is on its way.</p>
      <button class="btn btn-pink arrow" type="submit">Send me the guide </button>
      <p class="gd-privacy">We only use your details to send you the guide and to talk to you about mindset mentoring. We never share them, and you can ask us to delete them at any time.</p>
    </form>
  </div>
</div></div></section>

<section class="dark"><div class="wrap" style="max-width:820px;text-align:center">
  <p class="eyebrow">1-2-1 mindset mentoring</p><h2>Mindset mentoring, built by an ex-player for players.</h2>
  <p class="lead" style="margin-left:auto;margin-right:auto;color:rgba(255,255,255,.75)">A complete platform to help your child get past the things holding them back on match day.</p>
  <a class="btn btn-pink arrow" href="https://wa.me/447955722914?text=Hi%20Jaz%2C%20I%27ve%20read%20Across%20the%20White%20Line%20and%20I%27d%20like%20to%20book%20a%20free%20chat%20about%20my%20child." target="_blank" rel="noopener">Book a free chat </a>
</div></section>

<section class="white" id="questionnaire"><div class="wrap" style="max-width:820px">
  <p class="eyebrow">Free check-up</p><h2>Mindset questionnaire</h2>
  <p class="lead">Ten quick questions about how your child thinks and feels on the pitch. Choose the colour that fits best and get their mindset score straight away.</p>
  <form class="form ms-start" novalidate>
    <h2 style="margin:0">Before you start</h2>
    <div class="hp" aria-hidden="true"><label>Leave this empty<input name="company_website" tabindex="-1" autocomplete="off"></label></div>
    <label>Your name<input name="parent_name" autocomplete="name" required maxlength="120"></label>
    <label>Your email<input name="parent_email" type="email" autocomplete="email" required maxlength="254"></label>
    <label>Child's first name<input name="child_name" required maxlength="80"></label>
    <label>Child's age<input name="child_age" inputmode="numeric" maxlength="2"></label>
    <label class="ms-consent"><span><input type="checkbox" name="consent"> I'm happy for Player Performance to keep these answers and contact me about them.</span></label>
    <p class="notice bad" role="alert"></p>
    <button class="btn btn-pink arrow" type="submit">Start the check-up </button>
  </form>
  <div class="ms-quiz" hidden>
    <div class="ms-key"><span class="ms-dot red"></span> Needs work <span class="ms-dot amber"></span> Getting there <span class="ms-dot green"></span> Strong</div>
    <ol class="ms-list"></ol>
    <p class="notice bad ms-err" role="alert"></p>
    <button class="btn btn-pink arrow ms-submit" type="button">See my score </button>
  </div>
  <div class="ms-result" hidden>
    <p class="eyebrow">Your result</p><h2 class="ms-score"></h2><p class="lead ms-msg"></p>
    <div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-pink arrow" href="group-sessions.html#timetable">See the timetable </a><a class="btn btn-line" href="contact.html">Talk to a coach</a></div>
  </div>
</div></section>
"""
MINDSET_JS = """
<script>
(function () {
  var Q = __MQ__, API = '__PORTAL__/api/mindset';
  var gf = document.querySelector('.gd-form');
  if (gf) gf.addEventListener('submit', function (e) {
    e.preventDefault();
    var bad = gf.querySelector('.notice.bad'), ok = gf.querySelector('.notice.ok'), btn = gf.querySelector('button[type=submit]');
    bad.style.display = 'none'; ok.style.display = 'none';
    var em = gf.parent_email.value.trim(), ph = gf.phone.value.trim();
    if (!gf.parent_name.value.trim() || !/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(em) || !/^[0-9 +()-]{7,20}$/.test(ph)) { bad.textContent = 'Please add your name, a valid email and a phone number.'; bad.style.display = 'block'; return; }
    if (!gf.consent.checked) { bad.textContent = 'Please tick the box so we can send you the guide.'; bad.style.display = 'block'; return; }
    btn.disabled = true; btn.textContent = 'Sending...';
    fetch('__PORTAL__/api/guide', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ parent_name: gf.parent_name.value.trim(), parent_email: em, phone: ph, consent: true, company_website: gf.company_website.value }) })
      .then(function (r) { if (!r.ok) throw new Error(r.status); ok.style.display = 'block'; gf.reset(); })
      .catch(function () { bad.textContent = "Sorry, that didn't send. Please try again, or email inquiries@playerperformance.uk."; bad.style.display = 'block'; })
      .then(function () { btn.disabled = false; btn.textContent = 'Send me the guide'; });
  });
  var start = document.querySelector('.ms-start'), quiz = document.querySelector('.ms-quiz'), res = document.querySelector('.ms-result');
  if (!start) return;
  var who = {};
  var list = quiz.querySelector('.ms-list');
  Q.forEach(function (item, i) {
    var li = document.createElement('li'); li.className = 'ms-q';
    var h = document.createElement('h3'); h.textContent = item.q; li.appendChild(h);
    ['red', 'amber', 'green'].forEach(function (c) {
      var lab = document.createElement('label'); lab.className = 'ms-opt ' + c;
      var inp = document.createElement('input'); inp.type = 'radio'; inp.name = 'q' + i; inp.value = c;
      var sp = document.createElement('span'); sp.textContent = item[c];
      lab.appendChild(inp); lab.appendChild(sp); li.appendChild(lab);
    });
    list.appendChild(li);
  });
  start.addEventListener('submit', function (e) {
    e.preventDefault();
    var bad = start.querySelector('.notice.bad'); bad.style.display = 'none';
    var f = start, email = f.parent_email.value.trim();
    if (!f.parent_name.value.trim() || !/^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(email) || !f.child_name.value.trim()) { bad.textContent = 'Please add your name, a valid email and your child\\'s name.'; bad.style.display = 'block'; return; }
    if (!f.consent.checked) { bad.textContent = 'Please tick the box so we can keep your answers.'; bad.style.display = 'block'; return; }
    who = { parent_name: f.parent_name.value.trim(), parent_email: email, child_name: f.child_name.value.trim(), consent: true, company_website: f.company_website.value };
    var age = parseInt(f.child_age.value, 10); if (age >= 3 && age <= 18) who.child_age = age;
    start.hidden = true; quiz.hidden = false; quiz.scrollIntoView({ behavior: 'smooth' });
  });
  quiz.querySelector('.ms-submit').addEventListener('click', function () {
    var err = quiz.querySelector('.ms-err'); err.style.display = 'none';
    var answers = [];
    for (var i = 0; i < Q.length; i++) { var c = quiz.querySelector('input[name=q' + i + ']:checked'); if (!c) { err.textContent = 'Please choose a colour for every question.'; err.style.display = 'block'; return; } answers.push({ question: Q[i].q, colour: c.value }); }
    var pts = { red: 0, amber: 1, green: 2 }, score = 0; answers.forEach(function (a) { score += pts[a.colour]; });
    var max = answers.length * 2, pct = score / max, band = pct >= 0.75 ? 'green' : pct >= 0.45 ? 'amber' : 'red';
    var btn = this; btn.disabled = true; btn.textContent = 'Working it out...';
    var body = Object.assign({}, who, { answers: answers });
    fetch(API, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) })
      .then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
      .then(function (d) {
        if (d && d.score != null) { score = d.score; max = d.max_score; band = d.band; }
        var msg = { green: 'A strong mindset. Our sessions will keep pushing ' + who.child_name + ' and build on what is already there.', amber: who.child_name + ' is getting there. Regular sessions with lots of encouragement will help turn ambers into greens.', red: 'There is real room to grow, and that is exactly what we are here for. Small groups or 1-2-1 coaching can make a big difference to ' + who.child_name + '\\'s confidence.' };
        res.querySelector('.ms-score').innerHTML = '<span class="ms-dot big ' + band + '"></span>' + score + ' / ' + max;
        res.querySelector('.ms-msg').textContent = msg[band];
        quiz.hidden = true; res.hidden = false; res.scrollIntoView({ behavior: 'smooth' });
      });
  });
})();
</script>"""
page("mindset.html", "Mindset check-up | Player Performance", "Free mindset guide Across the White Line and a 10-question mindset check-up for young footballers aged 10 to 16.",
     mindset + MINDSET_JS.replace("__MQ__", _mq).replace("__PORTAL__", PORTAL))

# ---------------------------------------------------------------- Google: old Square links, sitemap, robots
OLD_LINKS = """
<script>
  (function () {
    var p = location.pathname.toLowerCase(), to = '/';
    if (/1-2-1|one-to-one|private/.test(p)) to = '/1-2-1.html';
    else if (/camp|half-term|holiday/.test(p)) to = '/camps.html';
    else if (/goal/.test(p)) to = '/goalkeeping.html';
    else if (/tour|barcelona|paris|abroad/.test(p)) to = '/tournaments.html';
    else if (/pro-training|about/.test(p)) to = '/about.html';
    else if (/training|session|product|shop|group|development/.test(p)) to = '/group-sessions.html';
    else if (/contact/.test(p)) to = '/contact.html';
    else if (/review/.test(p)) to = '/reviews.html';
    else if (/faq/.test(p)) to = '/faqs.html';
    location.replace(to);
  })();
</script>"""
notfound = f"""
<section class="page-hero"><div class="wrap"><p class="eyebrow">Page moved</p><h1>We've got<br>a new website</h1>
<p class="lead">This page has moved. Taking you to the right place now. If nothing happens, use the buttons below.</p>
<div style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn btn-pink arrow" href="/group-sessions.html#timetable">See the timetable </a><a class="btn btn-line" href="/">Home</a></div></div></section>
"""
page("404.html", "Page moved | Player Performance", "Player Performance has a new website.", notfound,
     extra_head='\n<base href="/">\n<meta name="robots" content="noindex">' + OLD_LINKS)
pages = [f for f, _ in NAV]
(OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
    f'  <url><loc>{SITE}/{"" if f == "index.html" else f}</loc></url>\n' for f in pages) + '</urlset>\n', encoding="utf-8")
(OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n", encoding="utf-8")
print("built", len(NAV), "pages")
