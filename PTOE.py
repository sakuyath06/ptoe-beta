#setup phase
import pygame
import math
pygame.init()
clock=pygame.time.Clock()
FPS=60
screen=pygame.display.set_mode((1455, 775))
pygame.display.set_caption("Periodic Table of Elements with Extra Informations")
pygame.display.set_icon(pygame.image.load('PTOE.ico'))
state="menu"

#asset loading phase
h_elm=pygame.image.load('resource/h.png').convert_alpha()
h_inf=pygame.image.load('resource/h_inf.png')
he_elm=pygame.image.load('resource/he.png').convert_alpha()
he_inf=pygame.image.load('resource/he_inf.png')
li_elm=pygame.image.load('resource/li.png').convert_alpha()
li_inf=pygame.image.load('resource/li_inf.png')
be_elm=pygame.image.load('resource/be.png').convert_alpha()
be_inf=pygame.image.load('resource/be_inf.png')
b_elm=pygame.image.load('resource/b.png').convert_alpha()
b_inf=pygame.image.load('resource/b_inf.png')
c_elm=pygame.image.load('resource/c.png').convert_alpha()
c_inf=pygame.image.load('resource/c_inf.png')
n_elm=pygame.image.load('resource/n.png').convert_alpha()
n_inf=pygame.image.load('resource/n_inf.png')
o_elm=pygame.image.load('resource/o.png').convert_alpha()
o_inf=pygame.image.load('resource/o_inf.png')
f_elm=pygame.image.load('resource/f.png').convert_alpha()
f_inf=pygame.image.load('resource/f_inf.png')
ne_elm=pygame.image.load('resource/ne.png').convert_alpha()
ne_inf=pygame.image.load('resource/ne_inf.png')
na_elm=pygame.image.load('resource/na.png').convert_alpha()
na_inf=pygame.image.load('resource/na_inf.png')
mg_elm=pygame.image.load('resource/mg.png').convert_alpha()
mg_inf=pygame.image.load('resource/mg_inf.png')
al_elm=pygame.image.load('resource/al.png').convert_alpha()
al_inf=pygame.image.load('resource/al_inf.png')
si_elm=pygame.image.load('resource/si.png').convert_alpha()
si_inf=pygame.image.load('resource/si_inf.png')
p_elm=pygame.image.load('resource/p.png').convert_alpha()
p_inf=pygame.image.load('resource/p_inf.png')
s_elm=pygame.image.load('resource/s.png').convert_alpha()
s_inf=pygame.image.load('resource/s_inf.png')
cl_elm=pygame.image.load('resource/cl.png').convert_alpha()
cl_inf=pygame.image.load('resource/cl_inf.png')
ar_elm=pygame.image.load('resource/ar.png').convert_alpha()
ar_inf=pygame.image.load('resource/ar_inf.png')
k_elm=pygame.image.load('resource/k.png').convert_alpha()
k_inf=pygame.image.load('resource/k_inf.png')
ca_elm=pygame.image.load('resource/ca.png').convert_alpha()
ca_inf=pygame.image.load('resource/ca_inf.png')
sc_elm=pygame.image.load('resource/sc.png').convert_alpha()
sc_inf=pygame.image.load('resource/sc_inf.png')
ti_elm=pygame.image.load('resource/ti.png').convert_alpha()
ti_inf=pygame.image.load('resource/ti_inf.png')
v_elm=pygame.image.load('resource/v.png').convert_alpha()
v_inf=pygame.image.load('resource/v_inf.png')
cr_elm=pygame.image.load('resource/cr.png').convert_alpha()
cr_inf=pygame.image.load('resource/cr_inf.png')
mn_elm=pygame.image.load('resource/mn.png').convert_alpha()
mn_inf=pygame.image.load('resource/mn_inf.png')
fe_elm=pygame.image.load('resource/fe.png').convert_alpha()
fe_inf=pygame.image.load('resource/fe_inf.png')
co_elm=pygame.image.load('resource/co.png').convert_alpha()
co_inf=pygame.image.load('resource/co_inf.png')
ni_elm=pygame.image.load('resource/ni.png').convert_alpha()
ni_inf=pygame.image.load('resource/ni_inf.png')
cu_elm=pygame.image.load('resource/cu.png').convert_alpha()
cu_inf=pygame.image.load('resource/cu_inf.png')
zn_elm=pygame.image.load('resource/zn.png').convert_alpha()
zn_inf=pygame.image.load('resource/zn_inf.png')
ga_elm=pygame.image.load('resource/ga.png').convert_alpha()
ga_inf=pygame.image.load('resource/ga_inf.png')
ge_elm=pygame.image.load('resource/ge.png').convert_alpha()
ge_inf=pygame.image.load('resource/ge_inf.png')
as_elm=pygame.image.load('resource/as.png').convert_alpha()
as_inf=pygame.image.load('resource/as_inf.png')
se_elm=pygame.image.load('resource/se.png').convert_alpha()
se_inf=pygame.image.load('resource/se_inf.png')
br_elm=pygame.image.load('resource/br.png').convert_alpha()
br_inf=pygame.image.load('resource/br_inf.png')
kr_elm=pygame.image.load('resource/kr.png').convert_alpha()
kr_inf=pygame.image.load('resource/kr_inf.png')
rb_elm=pygame.image.load('resource/rb.png').convert_alpha()
rb_inf=pygame.image.load('resource/rb_inf.png')
sr_elm=pygame.image.load('resource/sr.png').convert_alpha()
sr_inf=pygame.image.load('resource/sr_inf.png')
y_elm=pygame.image.load('resource/y.png').convert_alpha()
y_inf=pygame.image.load('resource/y_inf.png')
zr_elm=pygame.image.load('resource/zr.png').convert_alpha()
zr_inf=pygame.image.load('resource/zr_inf.png')
nb_elm=pygame.image.load('resource/nb.png').convert_alpha()
nb_inf=pygame.image.load('resource/nb_inf.png')
mo_elm=pygame.image.load('resource/mo.png').convert_alpha()
mo_inf=pygame.image.load('resource/mo_inf.png')
tc_elm=pygame.image.load('resource/tc.png').convert_alpha()
tc_inf=pygame.image.load('resource/tc_inf.png')
ru_elm=pygame.image.load('resource/ru.png').convert_alpha()
ru_inf=pygame.image.load('resource/ru_inf.png')
rh_elm=pygame.image.load('resource/rh.png').convert_alpha()
rh_inf=pygame.image.load('resource/rh_inf.png')
pd_elm=pygame.image.load('resource/pd.png').convert_alpha()
pd_inf=pygame.image.load('resource/pd_inf.png')
ag_elm=pygame.image.load('resource/ag.png').convert_alpha()
ag_inf=pygame.image.load('resource/ag_inf.png')
cd_elm=pygame.image.load('resource/cd.png').convert_alpha()
cd_inf=pygame.image.load('resource/cd_inf.png')
in_elm=pygame.image.load('resource/in.png').convert_alpha()
in_inf=pygame.image.load('resource/in_inf.png')
sn_elm=pygame.image.load('resource/sn.png').convert_alpha()
sn_inf=pygame.image.load('resource/sn_inf.png')
sb_elm=pygame.image.load('resource/sb.png').convert_alpha()
sb_inf=pygame.image.load('resource/sb_inf.png')
te_elm=pygame.image.load('resource/te.png').convert_alpha()
te_inf=pygame.image.load('resource/te_inf.png')
i_elm=pygame.image.load('resource/i.png').convert_alpha()
i_inf=pygame.image.load('resource/i_inf.png')
xe_elm=pygame.image.load('resource/xe.png').convert_alpha()
xe_inf=pygame.image.load('resource/xe_inf.png')
cs_elm=pygame.image.load('resource/cs.png').convert_alpha()
cs_inf=pygame.image.load('resource/cs_inf.png')
ba_elm=pygame.image.load('resource/ba.png').convert_alpha()
ba_inf=pygame.image.load('resource/ba_inf.png')
lan_elm=pygame.image.load('resource/lan.png').convert_alpha()
hf_elm=pygame.image.load('resource/hf.png').convert_alpha()
hf_inf=pygame.image.load('resource/hf_inf.png')
ta_elm=pygame.image.load('resource/ta.png').convert_alpha()
ta_inf=pygame.image.load('resource/ta_inf.png')
w_elm=pygame.image.load('resource/w.png').convert_alpha()
w_inf=pygame.image.load('resource/w_inf.png')
re_elm=pygame.image.load('resource/re.png').convert_alpha()
re_inf=pygame.image.load('resource/re_inf.png')
os_elm=pygame.image.load('resource/os.png').convert_alpha()
os_inf=pygame.image.load('resource/os_inf.png')
ir_elm=pygame.image.load('resource/ir.png').convert_alpha()
ir_inf=pygame.image.load('resource/ir_inf.png')
pt_elm=pygame.image.load('resource/pt.png').convert_alpha()
pt_inf=pygame.image.load('resource/pt_inf.png')
au_elm=pygame.image.load('resource/au.png').convert_alpha()
au_inf=pygame.image.load('resource/au_inf.png')
hg_elm=pygame.image.load('resource/hg.png').convert_alpha()
hg_inf=pygame.image.load('resource/hg_inf.png')
tl_elm=pygame.image.load('resource/tl.png').convert_alpha()
tl_inf=pygame.image.load('resource/tl_inf.png')
pb_elm=pygame.image.load('resource/pb.png').convert_alpha()
pb_inf=pygame.image.load('resource/pb_inf.png')
bi_elm=pygame.image.load('resource/bi.png').convert_alpha()
bi_inf=pygame.image.load('resource/bi_inf.png')
po_elm=pygame.image.load('resource/po.png').convert_alpha()
po_inf=pygame.image.load('resource/po_inf.png')
at_elm=pygame.image.load('resource/at.png').convert_alpha()
at_inf=pygame.image.load('resource/at_inf.png')
rn_elm=pygame.image.load('resource/rn.png').convert_alpha()
rn_inf=pygame.image.load('resource/rn_inf.png')
fr_elm=pygame.image.load('resource/fr.png').convert_alpha()
fr_inf=pygame.image.load('resource/fr_inf.png')
ra_elm=pygame.image.load('resource/ra.png').convert_alpha()
ra_inf=1
act_elm=pygame.image.load('resource/act.png').convert_alpha()
rf_elm=pygame.image.load('resource/rf.png').convert_alpha()
rf_inf=1
db_elm=pygame.image.load('resource/db.png').convert_alpha()
db_inf=1
sg_elm=pygame.image.load('resource/sg.png').convert_alpha()
sg_inf=1
bh_elm=pygame.image.load('resource/bh.png').convert_alpha()
bh_inf=1
hs_elm=pygame.image.load('resource/hs.png').convert_alpha()
hs_inf=1
mt_elm=pygame.image.load('resource/mt.png').convert_alpha()
mt_inf=1
ds_elm=pygame.image.load('resource/ds.png').convert_alpha()
ds_inf=1
rg_elm=pygame.image.load('resource/rg.png').convert_alpha()
rg_inf=1
cn_elm=pygame.image.load('resource/cn.png').convert_alpha()
cn_inf=1
nh_elm=pygame.image.load('resource/nh.png').convert_alpha()
nh_inf=1
fl_elm=pygame.image.load('resource/fl.png').convert_alpha()
fl_inf=1
mc_elm=pygame.image.load('resource/mc.png').convert_alpha()
mc_inf=1
lv_elm=pygame.image.load('resource/lv.png').convert_alpha()
lv_inf=1
ts_elm=pygame.image.load('resource/ts.png').convert_alpha()
ts_inf=1
og_elm=pygame.image.load('resource/og.png').convert_alpha()
og_inf=1
la_elm=pygame.image.load('resource/la.png').convert_alpha()
la_inf=pygame.image.load('resource/la_inf.png')
ce_elm=pygame.image.load('resource/ce.png').convert_alpha()
ce_inf=1
pr_elm=pygame.image.load('resource/pr.png').convert_alpha()
pr_inf=1
nd_elm=pygame.image.load('resource/nd.png').convert_alpha()
nd_inf=1
pm_elm=pygame.image.load('resource/pm.png').convert_alpha()
pm_inf=1
sm_elm=pygame.image.load('resource/sm.png').convert_alpha()
sm_inf=1
eu_elm=pygame.image.load('resource/eu.png').convert_alpha()
eu_inf=1
gd_elm=pygame.image.load('resource/gd.png').convert_alpha()
gd_inf=1
tb_elm=pygame.image.load('resource/tb.png').convert_alpha()
tb_inf=1
dy_elm=pygame.image.load('resource/dy.png').convert_alpha()
dy_inf=1
ho_elm=pygame.image.load('resource/ho.png').convert_alpha()
ho_inf=1
er_elm=pygame.image.load('resource/er.png').convert_alpha()
er_inf=1
tm_elm=pygame.image.load('resource/tm.png').convert_alpha()
tm_inf=1
yb_elm=pygame.image.load('resource/yb.png').convert_alpha()
yb_inf=1
lu_elm=pygame.image.load('resource/lu.png').convert_alpha()
lu_inf=1
ac_elm=pygame.image.load('resource/ac.png').convert_alpha()
ac_inf=1
th_elm=pygame.image.load('resource/th.png').convert_alpha()
th_inf=1
pa_elm=pygame.image.load('resource/pa.png').convert_alpha()
pa_inf=1
u_elm=pygame.image.load('resource/u.png').convert_alpha()
u_inf=1
np_elm=pygame.image.load('resource/np.png').convert_alpha()
np_inf=1
pu_elm=pygame.image.load('resource/pu.png').convert_alpha()
pu_inf=1
am_elm=pygame.image.load('resource/am.png').convert_alpha()
am_inf=1
cm_elm=pygame.image.load('resource/cm.png').convert_alpha()
cm_inf=1
bk_elm=pygame.image.load('resource/bk.png').convert_alpha()
bk_inf=1
cf_elm=pygame.image.load('resource/cf.png').convert_alpha()
cf_inf=1
es_elm=pygame.image.load('resource/es.png').convert_alpha()
es_inf=1
fm_elm=pygame.image.load('resource/fm.png').convert_alpha()
fm_inf=1
md_elm=pygame.image.load('resource/md.png').convert_alpha()
md_inf=1
no_elm=pygame.image.load('resource/no.png').convert_alpha()
no_inf=1
lr_elm=pygame.image.load('resource/lr.png').convert_alpha()
lr_inf=1
plc_holder=pygame.image.load('resource/placeholder.png')
cms=pygame.image.load('resource/cms.png')
debug=pygame.image.load('resource/debug1.png')
menu0=pygame.image.load('resource/menu0.png')
menu1=pygame.image.load('resource/menu1.png')
resume_btn=pygame.image.load('resource/resume1.png').convert_alpha()
start=pygame.image.load('resource/start.png').convert_alpha()
loadtimer=0

#loading screen setup
class Loading(pygame.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		self.sprites = []
		self.sprites.append(pygame.image.load('resource/loading/frame0.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame1.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame2.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame3.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame4.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame5.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame6.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame7.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame8.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame9.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame10.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame11.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame12.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame13.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame14.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame15.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame16.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame17.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame18.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame19.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame20.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame21.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame22.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame23.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame24.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame25.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame26.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame27.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame28.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame29.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame30.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame31.gif'))
		self.sprites.append(pygame.image.load('resource/loading/frame32.gif'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [x,y]

	def update(self):
		global loadtimer
		self.current_sprite += 1

		if self.current_sprite >= len(self.sprites):
			self.current_sprite = 0
			loadtimer = loadtimer + 200

		self.image = self.sprites[self.current_sprite]

#loading screen loading phase
move_sprites=pygame.sprite.Group()
loading = Loading(627, 287)
move_sprites.add(loading)

#button setup phase
class Button():
	def __init__(self, x, y, image, scale):
		width=image.get_width()
		height=image.get_height()
		self.image=pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect=self.image.get_rect()
		self.rect.topleft=(x, y)
		self.clicked=False

	def draw(self, surface):
		action=False
		#get mouse position phase
		pos=pygame.mouse.get_pos()

		#check mouse hover and clicked conditions phase
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked=True
				action=True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked=False

		#draw button phase
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#button rendering phase
h=Button(10, 10, h_elm, 1)
he=Button(1370, 10, he_elm, 1)
li=Button(10, 90, li_elm, 1)
be=Button(90, 90, be_elm, 1)
b=Button(970, 90, b_elm, 1)
c=Button(1050, 90, c_elm, 1)
n=Button(1130, 90, n_elm, 1)
o=Button(1210, 90, o_elm, 1)
f=Button(1290, 90, f_elm, 1)
ne=Button(1370, 90, ne_elm, 1)
na=Button(10, 170, na_elm, 1)
mg=Button(90, 170, mg_elm, 1)
al=Button(970, 170, al_elm, 1)
si=Button(1050, 170, si_elm, 1)
p=Button(1130, 170, p_elm, 1)
s=Button(1210, 170, s_elm, 1)
cl=Button(1290, 170, cl_elm, 1)
ar=Button(1370, 170, ar_elm, 1)
k=Button(10, 250, k_elm, 1)
ca=Button(90, 250, ca_elm, 1)
sc=Button(170, 250, sc_elm, 1)
ti=Button(250, 250, ti_elm, 1)
v=Button(330, 250, v_elm, 1)
cr=Button(410, 250, cr_elm, 1)
mn=Button(490, 250, mn_elm, 1)
fe=Button(570, 250, fe_elm, 1)
co=Button(650, 250, co_elm, 1)
ni=Button(730, 250, ni_elm, 1)
cu=Button(810, 250, cu_elm, 1)
zn=Button(890, 250, zn_elm, 1)
ga=Button(970, 250, ga_elm, 1)
ge=Button(1050, 250, ge_elm, 1)
as_btn=Button(1130, 250, as_elm, 1)
se=Button(1210, 250, se_elm, 1)
br=Button(1290, 250, br_elm, 1)
kr=Button(1370, 250, kr_elm, 1)
rb=Button(10, 330, rb_elm, 1)
sr=Button(90, 330, sr_elm, 1)
y=Button(170, 330, y_elm, 1)
zr=Button(250, 330, zr_elm, 1)
nb=Button(330, 330, nb_elm, 1)
mo=Button(410, 330, mo_elm, 1)
tc=Button(490, 330, tc_elm, 1)
ru=Button(570, 330, ru_elm, 1)
rh=Button(650, 330, rh_elm, 1)
pd=Button(730, 330, pd_elm, 1)
ag=Button(810, 330, ag_elm, 1)
cd=Button(890, 330, cd_elm, 1)
in_btn=Button(970, 330, in_elm, 1)
sn=Button(1050, 330, sn_elm, 1)
sb=Button(1130, 330, sb_elm, 1)
te=Button(1210, 330, te_elm, 1)
i=Button(1290, 330, i_elm, 1)
xe=Button(1370, 330, xe_elm, 1)
cs=Button(10, 410, cs_elm, 1)
ba=Button(90, 410, ba_elm, 1)
hf=Button(250, 410, hf_elm, 1)
ta=Button(330, 410, ta_elm, 1)
w=Button(410, 410, w_elm, 1)
re=Button(490, 410, re_elm, 1)
os=Button(570, 410, os_elm, 1)
ir=Button(650, 410, ir_elm, 1)
pt=Button(730, 410, pt_elm, 1)
au=Button(810, 410, au_elm, 1)
hg=Button(890, 410, hg_elm, 1)
tl=Button(970, 410, tl_elm, 1)
pb=Button(1050, 410, pb_elm, 1)
bi=Button(1130, 410, bi_elm, 1)
po=Button(1210, 410, po_elm, 1)
at=Button(1290, 410, at_elm, 1)
rn=Button(1370, 410, rn_elm, 1)
fr=Button(10, 490, fr_elm, 1)
ra=Button(90, 490, ra_elm, 1)
rf=Button(250, 490, rf_elm, 1)
db=Button(330, 490, db_elm, 1)
sg=Button(410, 490, sg_elm, 1)
bh=Button(490, 490, bh_elm, 1)
hs=Button(570, 490, hs_elm, 1)
mt=Button(650, 490, mt_elm, 1)
ds=Button(730, 490, ds_elm, 1)
rg=Button(810, 490, rg_elm, 1)
cn=Button(890, 490, cn_elm, 1)
nh=Button(970, 490, nh_elm, 1)
fl=Button(1050, 490, fl_elm, 1)
mc=Button(1130, 490, mc_elm, 1)
lv=Button(1210, 490, lv_elm, 1)
ts=Button(1290, 490, ts_elm, 1)
og=Button(1370, 490, og_elm, 1)
la=Button(250, 615, la_elm, 1)
ce=Button(330, 615, ce_elm, 1)
pr=Button(410, 615, pr_elm, 1)
nd=Button(490, 615, nd_elm, 1)
pm=Button(570, 615, pm_elm, 1)
sm=Button(650, 615, sm_elm, 1)
eu=Button(730, 615, eu_elm, 1)
gd=Button(810, 615, gd_elm, 1)
tb=Button(890, 615, tb_elm, 1)
dy=Button(970, 615, dy_elm, 1)
ho=Button(1050, 615, ho_elm, 1)
er=Button(1130, 615, er_elm, 1)
tm=Button(1210, 615, tm_elm, 1)
yb=Button(1290, 615, yb_elm, 1)
lu=Button(1370, 615, lu_elm, 1)
ac=Button(250, 695, ac_elm, 1)
th=Button(330, 695, th_elm, 1)
pa=Button(410, 695, pa_elm, 1)
u=Button(490, 695, u_elm, 1)
np=Button(570, 695, np_elm, 1)
pu=Button(650, 695, pu_elm, 1)
am=Button(730, 695, am_elm, 1)
cm=Button(810, 695, cm_elm, 1)
bk=Button(890, 695, bk_elm, 1)
cf=Button(970, 695, cf_elm, 1)
es=Button(1050, 695, es_elm, 1)
fm=Button(1130, 695, fm_elm, 1)
md=Button(1210, 695, md_elm, 1)
no=Button(1290, 695, no_elm, 1)
lr=Button(1370, 695, lr_elm, 1)
resume=Button(1225, 10, resume_btn, 0.25)
start_btn=Button(620, 300, start, 0.5)

#running phase
run=True
while run:
	clock.tick(FPS)
	if state == "menu":
		screen.blit(menu1,(0, 0))
		if start_btn.draw(screen):
			state = "load"
	if state == "load":
		screen.fill((0,0,0))
		move_sprites.draw(screen)
		move_sprites.update()
		if loadtimer == 400:
			state = "main"
	if state == "main":
		screen.fill((0,0,0))
		screen.blit(lan_elm,(170, 410))
		screen.blit(act_elm,(170, 490))
		if h.draw(screen):
			state = "h"
		if he.draw(screen):
			state = "he"
		if li.draw(screen):
			state = "li"
		if be.draw(screen):
			state = "be"
		if b.draw(screen):
			state = "b"
		if c.draw(screen):
			state = "c"
		if n.draw(screen):
			state = "n"
		if o.draw(screen):
			state = "o"
		if f.draw(screen):
			state = "f"
		if ne.draw(screen):
			state = "ne"
		if na.draw(screen):
			state = "na"
		if mg.draw(screen):
			state = "mg"
		if al.draw(screen):
			state = "al"
		if si.draw(screen):
			state = "si"
		if p.draw(screen):
			state = "p"
		if s.draw(screen):
			state = "s"
		if cl.draw(screen):
			state = "cl"
		if ar.draw(screen):
			state = "ar"
		if k.draw(screen):
			state = "k"
		if ca.draw(screen):
			state = "ca"
		if sc.draw(screen):
			state = "sc"
		if ti.draw(screen):
			state = "ti"
		if v.draw(screen):
			state = "v"
		if cr.draw(screen):
			state = "cr"
		if mn.draw(screen):
			state = "mn"
		if fe.draw(screen):
			state = "fe"
		if co.draw(screen):
			state = "co"
		if ni.draw(screen):
			state = "ni"
		if cu.draw(screen):
			state = "cu"
		if zn.draw(screen):
			state = "zn"
		if ga.draw(screen):
			state = "ga"
		if ge.draw(screen):
			state = "ge"
		if as_btn.draw(screen):
			state = "as"
		if se.draw(screen):
			state = "se"
		if br.draw(screen):
			state = "br"
		if kr.draw(screen):
			state = "kr"
		if rb.draw(screen):
			state = "rb"
		if sr.draw(screen):
			state = "sr"
		if y.draw(screen):
			state = "y"
		if zr.draw(screen):
			state = "zr"
		if nb.draw(screen):
			state = "nb"
		if mo.draw(screen):
			state = "mo"
		if tc.draw(screen):
			state = "tc"
		if ru.draw(screen):
			state = "ru"
		if rh.draw(screen):
			state = "rh"
		if pd.draw(screen):
			state = "pd"
		if ag.draw(screen):
			state = "ag"
		if cd.draw(screen):
			state = "cd"
		if in_btn.draw(screen):
			state = "in"
		if sn.draw(screen):
			state = "sn"
		if sb.draw(screen):
			state = "sb"
		if te.draw(screen):
			state = "te"
		if i.draw(screen):
			state = "i"
		if xe.draw(screen):
			state = "xe"
		if cs.draw(screen):
			state = "cs"
		if ba.draw(screen):
			state = "ba"
		if hf.draw(screen):
			state = "hf"
		if ta.draw(screen):
			state = "ta"
		if w.draw(screen):
			state = "w"
		if re.draw(screen):
			state = "re"
		if os.draw(screen):
			state = "os"
		if ir.draw(screen):
			state = "ir"
		if pt.draw(screen):
			state = "pt"
		if au.draw(screen):
			state = "au"
		if hg.draw(screen):
			state = "hg"
		if tl.draw(screen):
			state = "tl"
		if pb.draw(screen):
			state = "pb"
		if bi.draw(screen):
			state = "bi"
		if po.draw(screen):
			state = "po"
		if at.draw(screen):
			state = "at"
		if rn.draw(screen):
			state = "rn"
		if fr.draw(screen):
			state = "fr"
		if ra.draw(screen):
			state = "ra"
		if rf.draw(screen):
			state = "rf"
		if db.draw(screen):
			state = "db"
		if sg.draw(screen):
			state = "sg"
		if bh.draw(screen):
			state = "bh"
		if hs.draw(screen):
			state = "hs"
		if mt.draw(screen):
			state = "mt"
		if ds.draw(screen):
			state = "ds"
		if rg.draw(screen):
			state = "rg"
		if cn.draw(screen):
			state = "cn"
		if nh.draw(screen):
			state = "nh"
		if fl.draw(screen):
			state = "fl"
		if mc.draw(screen):
			state = "mc"
		if lv.draw(screen):
			state = "lv"
		if ts.draw(screen):
			state = "ts"
		if og.draw(screen):
			state = "og"
		if la.draw(screen):
			state = "la"
		if ce.draw(screen):
			state = "ce"
		if pr.draw(screen):
			state = "pr"
		if nd.draw(screen):
			state = "nd"
		if pm.draw(screen):
			state = "pm"
		if sm.draw(screen):
			state = "sm"
		if eu.draw(screen):
			state = "eu"
		if gd.draw(screen):
			state = "gd"
		if tb.draw(screen):
			state = "tb"
		if dy.draw(screen):
			state = "dy"
		if ho.draw(screen):
			state = "ho"
		if er.draw(screen):
			state = "er"
		if tm.draw(screen):
			state = "tm"
		if yb.draw(screen):
			state = "yb"
		if lu.draw(screen):
			state = "lu"
		if ac.draw(screen):
			state = "ac"
		if th.draw(screen):
			state = "th"
		if pa.draw(screen):
			state = "pa"
		if u.draw(screen):
			state = "u"
		if np.draw(screen):
			state = "np"
		if pu.draw(screen):
			state = "pu"
		if am.draw(screen):
			state = "am"
		if cm.draw(screen):
			state = "cm"
		if bk.draw(screen):
			state = "bk"
		if cf.draw(screen):
			state = "cf"
		if es.draw(screen):
			state = "es"
		if fm.draw(screen):
			state = "fm"
		if md.draw(screen):
			state = "md"
		if no.draw(screen):
			state = "no"
		if lr.draw(screen):
			state = "lr"
	if state == "h":
		screen.fill((0,0,0))
		screen.blit(h_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "he":
		screen.fill((0,0,0))
		screen.blit(he_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "li":
		screen.fill((0,0,0))
		screen.blit(li_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "be":
		screen.fill((0,0,0))
		screen.blit(be_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "b":
		screen.fill((0,0,0))
		screen.blit(b_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "c":
		screen.fill((0,0,0))
		screen.blit(c_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "n":
		screen.fill((0,0,0))
		screen.blit(n_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "o":
		screen.fill((0,0,0))
		screen.blit(o_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "f":
		screen.fill((0,0,0))
		screen.blit(f_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ne":
		screen.fill((0,0,0))
		screen.blit(ne_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "na":
		screen.fill((0,0,0))
		screen.blit(na_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "mg":
		screen.fill((0,0,0))
		screen.blit(mg_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "al":
		screen.fill((0,0,0))
		screen.blit(al_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "si":
		screen.fill((0,0,0))
		screen.blit(si_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "p":
		screen.fill((0,0,0))
		screen.blit(p_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "s":
		screen.fill((0,0,0))
		screen.blit(s_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cl":
		screen.fill((0,0,0))
		screen.blit(cl_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ar":
		screen.fill((0,0,0))
		screen.blit(ar_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "k":
		screen.fill((0,0,0))
		screen.blit(k_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ca":
		screen.fill((0,0,0))
		screen.blit(ca_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "sc":
		screen.fill((0,0,0))
		screen.blit(sc_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ti":
		screen.fill((0,0,0))
		screen.blit(ti_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "v":
		screen.fill((0,0,0))
		screen.blit(v_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cr":
		screen.fill((0,0,0))
		screen.blit(cr_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "mn":
		screen.fill((0,0,0))
		screen.blit(mn_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "fe":
		screen.fill((0,0,0))
		screen.blit(fe_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "co":
		screen.fill((0,0,0))
		screen.blit(co_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ni":
		screen.fill((0,0,0))
		screen.blit(ni_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cu":
		screen.fill((0,0,0))
		screen.blit(cu_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "zn":
		screen.fill((0,0,0))
		screen.blit(zn_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ga":
		screen.fill((0,0,0))
		screen.blit(ga_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ge":
		screen.fill((0,0,0))
		screen.blit(ge_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "as":
		screen.fill((0,0,0))
		screen.blit(as_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "se":
		screen.fill((0,0,0))
		screen.blit(se_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "br":
		screen.fill((0,0,0))
		screen.blit(br_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "kr":
		screen.fill((0,0,0))
		screen.blit(kr_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "rb":
		screen.fill((0,0,0))
		screen.blit(rb_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "sr":
		screen.fill((0,0,0))
		screen.blit(sr_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "y":
		screen.fill((0,0,0))
		screen.blit(y_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "zr":
		screen.fill((0,0,0))
		screen.blit(zr_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "nb":
		screen.fill((0,0,0))
		screen.blit(nb_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "mo":
		screen.fill((0,0,0))
		screen.blit(mo_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "tc":
		screen.fill((0,0,0))
		screen.blit(tc_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ru":
		screen.fill((0,0,0))
		screen.blit(ru_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "rh":
		screen.fill((0,0,0))
		screen.blit(rh_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pd":
		screen.fill((0,0,0))
		screen.blit(pd_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ag":
		screen.fill((0,0,0))
		screen.blit(ag_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cd":
		screen.fill((0,0,0))
		screen.blit(cd_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "in":
		screen.fill((0,0,0))
		screen.blit(in_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "sn":
		screen.fill((0,0,0))
		screen.blit(sn_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "sb":
		screen.fill((0,0,0))
		screen.blit(sb_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "te":
		screen.fill((0,0,0))
		screen.blit(te_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "i":
		screen.fill((0,0,0))
		screen.blit(i_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "xe":
		screen.fill((0,0,0))
		screen.blit(xe_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cs":
		screen.fill((0,0,0))
		screen.blit(cs_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ba":
		screen.fill((0,0,0))
		screen.blit(ba_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "hf":
		screen.fill((0,0,0))
		screen.blit(hf_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ta":
		screen.fill((0,0,0))
		screen.blit(ta_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "w":
		screen.fill((0,0,0))
		screen.blit(w_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "re":
		screen.fill((0,0,0))
		screen.blit(re_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "os":
		screen.fill((0,0,0))
		screen.blit(os_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ir":
		screen.fill((0,0,0))
		screen.blit(ir_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pt":
		screen.fill((0,0,0))
		screen.blit(pt_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "au":
		screen.fill((0,0,0))
		screen.blit(au_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "hg":
		screen.fill((0,0,0))
		screen.blit(hg_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "tl":
		screen.fill((0,0,0))
		screen.blit(tl_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pb":
		screen.fill((0,0,0))
		screen.blit(pb_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "bi":
		screen.fill((0,0,0))
		screen.blit(bi_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "po":
		screen.fill((0,0,0))
		screen.blit(po_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "at":
		screen.fill((0,0,0))
		screen.blit(at_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "rn":
		screen.fill((0,0,0))
		screen.blit(rn_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "fr":
		screen.fill((0,0,0))
		screen.blit(fr_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ra":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "rf":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "db":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "sg":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "bh":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "hs":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "mt":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ds":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "rg":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cn":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "nh":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "fl":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "mc":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "lv":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ts":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "og":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "la":
		screen.fill((0,0,0))
		screen.blit(la_inf,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ce":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pr":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "nd":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pm":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "sm":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "eu":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "gd":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "tb":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "dy":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ho":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "er":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "tm":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "yb":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "lu":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "ac":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "th":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pa":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "u":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "np":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "pu":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "am":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cm":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "bk":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "cf":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "es":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "fm":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "md":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "no":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	if state == "lr":
		screen.fill((0,0,0))
		screen.blit(cms,(0,0))
		if resume.draw(screen):
			state = "main"
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run=False