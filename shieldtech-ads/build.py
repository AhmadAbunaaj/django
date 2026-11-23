F = "node_modules/@fontsource/readex-pro/files/readex-pro-"
fonts = "".join(f"@font-face{{font-family:Readex;font-weight:{w};src:url({F}{s}-{w}-normal.woff2)}}" for w in (400,500,700) for s in ("arabic","latin"))
CSS = fonts + """
:root{--bg:#071A2B;--sf:#0A2740;--tx:#fff;--mu:#A9C1D4;--navy:#044366;--cy:#22B8F0;--rec:#FF4B4B}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden;background:var(--bg)}
body{font-family:Readex,sans-serif;color:var(--tx);position:relative}
.photo{position:absolute;inset:0;background-size:cover;background-position:center}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(34,184,240,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(34,184,240,.06) 1px,transparent 1px);background-size:60px 60px;pointer-events:none}
.top{position:absolute;top:64px;right:70px;left:70px;display:flex;justify-content:space-between;align-items:center;z-index:5}
.logo{background:#fff;padding:14px 18px;border-radius:6px;box-shadow:0 10px 40px rgba(0,0,0,.35)}
.logo img{height:118px;display:block}
.rec{font:500 28px Readex;letter-spacing:3px;color:#fff;display:flex;align-items:center;gap:12px;background:rgba(7,26,43,.6);border:1px solid rgba(34,184,240,.35);padding:10px 20px;backdrop-filter:blur(6px)}
.rec i{width:14px;height:14px;border-radius:50%;background:var(--rec);box-shadow:0 0 12px var(--rec)}
.tag{display:inline-flex;align-items:center;gap:14px;font:500 30px Readex;color:var(--cy);margin-bottom:22px}
.tag::before{content:"";width:46px;height:3px;background:var(--cy)}
h1{font:700 92px/1.18 Readex;letter-spacing:-.5px}
h1 em{font-style:normal;color:var(--cy)}
.sub{font:400 34px/1.6 Readex;color:var(--mu);margin-top:22px;max-width:900px}
.foot{position:absolute;left:0;right:0;bottom:0;height:150px;background:var(--navy);display:flex;align-items:center;justify-content:space-between;padding:0 70px;z-index:5}
.foot .cta{font:700 36px Readex}
.foot .cta small{display:block;font:400 28px Readex;color:#cfe3f1;margin-top:4px}
.ph{font:700 38px Readex;letter-spacing:1px;position:relative;padding:14px 26px}
.vf{position:relative}
.vf::before,.vf::after,.vf>b::before,.vf>b::after{content:"";position:absolute;width:26px;height:26px;border-color:var(--cy);border-style:solid}
.vf::before{top:0;right:0;border-width:3px 3px 0 0}.vf::after{top:0;left:0;border-width:3px 0 0 3px}
.vf>b::before{bottom:0;right:0;border-width:0 3px 3px 0}.vf>b::after{bottom:0;left:0;border-width:0 0 3px 3px}
.chips{display:flex;gap:16px;margin-top:30px;flex-wrap:wrap}
.chip{font:500 30px Readex;padding:12px 26px;border:1.5px solid rgba(34,184,240,.55);background:rgba(7,26,43,.55);color:#fff}
.mark{position:absolute;opacity:.07;filter:brightness(10);pointer-events:none}
.box{position:absolute;border:2px solid rgba(34,184,240,.8)}
"""
def foot():
    return '''<div class="foot"><div class="cta">تواصل معنا الآن<small>معاينة وتركيب احترافي</small></div>
<div class="ph vf" dir="ltr"><b></b>0787876612 &nbsp;|&nbsp; 0798193489</div></div>'''
TOP = '<div class="top"><div class="logo"><img src="img/logo-crop.png"></div>{right}</div>'
REC = '<div class="rec" dir="ltr"><i></i>REC</div>'
def page(body, extra=""):
    return f'<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>{body}</body></html>'
def label(t): return f'<div class="rec">{t}</div>'

posts = {}
# 1 CCTV — full-bleed, text bottom, viewfinder on camera
posts[1] = page(f'''<div class="photo" style="background-image:url(img/p1.png);background-position:30% center"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,26,43,.55) 0%,rgba(7,26,43,0) 22%,rgba(7,26,43,0) 42%,rgba(7,26,43,.92) 66%,#071A2B 82%)"></div>
<div class="grid" style="opacity:.6"></div>
<div class="vf" style="position:absolute;top:215px;left:110px;width:640px;height:480px"><b></b></div>
{TOP.format(right=REC)}
<div style="position:absolute;right:70px;left:70px;bottom:210px">
<div class="tag">كاميرات المراقبة CCTV</div>
<h1>عينك على مكانك<br><em>حتى وأنت بعيد</em></h1>
<p class="sub">تركيب أنظمة كاميرات المراقبة للمنازل والمحلات<br>والشركات، مع إمكانية المشاهدة عن بُعد.</p></div>{foot()}''')

# 2 Access control — photo top, solid panel bottom
posts[2] = page(f'''<div class="photo" style="bottom:auto;height:820px;background-image:url(img/p2.png);background-position:center 35%"></div>
<div style="position:absolute;top:620px;left:0;right:0;height:200px;background:linear-gradient(180deg,rgba(7,26,43,0),#071A2B)"></div>
<div class="grid" style="top:700px;-webkit-mask-image:linear-gradient(180deg,transparent,#000 200px)"></div>
{TOP.format(right=label("Access Control"))}
<div style="position:absolute;right:70px;left:70px;top:760px">
<div class="tag">أنظمة التحكم بالأبواب</div>
<h1>أنت تقرّر<br><em>مين يدخل ومتى</em></h1>
<p class="sub">أنظمة دخول بالبطاقة والرمز السري للمكاتب والشركات.</p></div>{foot()}''')

# 3 Fingerprint — text top, photo bottom
posts[3] = page(f'''<div class="photo" style="top:420px;background-image:url(img/p3.png);background-position:center 30%"></div>
<div style="position:absolute;top:400px;left:0;right:0;height:300px;background:linear-gradient(180deg,#071A2B,rgba(7,26,43,0))"></div>
<div class="grid" style="-webkit-mask-image:linear-gradient(180deg,#000 30%,transparent 55%)"></div>
<div class="vf" style="position:absolute;top:880px;left:470px;width:260px;height:260px"><b></b></div>
{TOP.format(right=label("Time Attendance"))}
<div style="position:absolute;right:70px;left:70px;top:250px">
<div class="tag">أجهزة البصمة وتسجيل الدوام</div>
<h1>دوام موظفيك <em>بدقّة</em></h1>
<p class="sub" style="max-width:820px">تركيب أجهزة البصمة لتسجيل حضور<br>وانصراف الموظفين في الشركات والمؤسسات.</p></div>{foot()}''')

# 4 Cabling — photo full, side gradient, list
posts[4] = page(f'''<div class="photo" style="background-image:url(img/p4.png);background-position:65% center"></div>
<div style="position:absolute;inset:0;background:linear-gradient(270deg,#071A2B 0%,rgba(7,26,43,.96) 48%,rgba(7,26,43,.5) 78%,rgba(7,26,43,.25) 100%)"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,26,43,.6),rgba(7,26,43,0) 25%)"></div>
{TOP.format(right=label("Network Cabling"))}
<div style="position:absolute;right:70px;width:700px;top:380px">
<div class="tag">تمديد وتأسيس الشبكات</div>
<h1>شبكة مرتّبة<br><em>من الأساس</em></h1>
<p class="sub">تمديد وتأسيس شبكات الإنترنت للبيوت<br>والمكاتب والمباني بتنظيم احترافي.</p>
<div style="margin-top:40px;display:grid;gap:18px">
{"".join(f'<div style="font:500 32px Readex;display:flex;gap:18px;align-items:center"><span dir="ltr" style="color:var(--cy);font:700 30px Readex">0{i+1}</span>{t}</div>' for i,t in enumerate(["تمديد كوابل الشبكة","تركيب وترتيب الكبائن","تجهيز نقاط الإنترنت"]))}
</div></div>{foot()}''')

# 5 Between apartments — photo, text top centre-right, chips
posts[5] = page(f'''<div class="photo" style="background-image:url(img/p5.png);background-position:center 70%"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,#071A2B 0%,rgba(7,26,43,.9) 36%,rgba(7,26,43,.15) 62%,rgba(7,26,43,.55) 100%)"></div>
{TOP.format(right=label("Building Network"))}
<div style="position:absolute;right:70px;left:70px;top:260px">
<div class="tag">توصيل الإنترنت داخل المبنى</div>
<h1>اشتراك واحد<br><em>يوصل لكل مكان</em></h1>
<p class="sub">نوصل الإنترنت بين الشقق والغرف والمكاتب<br>بحلول سلكية ولاسلكية.</p>
<div class="chips"><span class="chip">شقق</span><span class="chip">غرف</span><span class="chip">مكاتب</span></div></div>{foot()}''')

# 6 Access points — photo, text bottom, viewfinder on AP
posts[6] = page(f'''<div class="photo" style="background-image:url(img/p6.png);background-position:center 0%"></div>
<div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(7,26,43,.55) 0%,rgba(7,26,43,0) 20%,rgba(7,26,43,0) 45%,rgba(7,26,43,.92) 64%,#071A2B 80%)"></div>
<div class="vf" style="position:absolute;top:210px;left:120px;right:120px;height:330px"><b></b></div>
{TOP.format(right=label("Wi-Fi Access Point"))}
<div style="position:absolute;right:70px;left:70px;bottom:210px">
<div class="tag">نقاط توزيع الإنترنت</div>
<h1>واي فاي قوي<br><em>في كل زاوية</em></h1>
<p class="sub">تركيب نقاط توزيع الإنترنت Access Point<br>وحلول الشبكات للمنازل والشركات.</p></div>{foot()}''')

for k,v in posts.items(): open(f"post{k}.html","w").write(v)
