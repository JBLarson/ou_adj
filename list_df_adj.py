import pandas as pd

import input_adj as adj

#localize input variables
b1o = adj.b1o
b2o = adj.b2o
b1s = adj.b1s
b2s = adj.b2s
b1r = adj.b1r
b2r = adj.b2r
b1w = adj.b1w
b2w = adj.b2w

#bet1/2 score title variables
b1sT = "o" + str(b1s) + " risk"
b2sT = "u" + str(b2s) + " risk"

#trial 0 sum_stats
risk_sum = b1r + b2r
win_sum = b1w + b2w
wr = win_sum/risk_sum
ss = (adj.bcs + adj.winloss + adj.losswin)/3
sr = ss / risk_sum
bsµ = adj.bcs - ss
wsµ = adj.winloss - ss
lsµ = adj.losswin - ss
bs = bsµ / ss
ws = wsµ / ss
ls = lsµ / ss


#trial 1
#define win and loss variables (secondary variables)
b1w_t1 = round(adj.gamble(adj.b1r_t1,b1o),ndigits=2)
b1L_t1 = -adj.b1r_t1
b2w_t1 = round(adj.gamble(adj.b2r_t1,b2o),ndigits=2)
b2L_t1 = -adj.b2r_t1
#define scenarios (tertiary variables)
bcs_t1 = round((b1w_t1+b2w_t1),ndigits=2)
winloss_t1 = round((b1w_t1+b2L_t1),ndigits=2)
losswin_t1 = round((b1L_t1+b2w_t1),ndigits=2)
#sum stats (quartic variables)
risk_sum_t1 = adj.b1r_t1 + adj.b2r_t1
win_sum_t1 = b1w_t1 + b2w_t1
wr_t1 = win_sum_t1 / risk_sum_t1
ss_t1 = (bcs_t1 + winloss_t1 + losswin_t1)/3
sr_t1 = ss_t1 / risk_sum_t1
bsµ_t1 = bcs_t1 - ss_t1
wsµ_t1 = winloss_t1 - ss_t1
lsµ_t1 = losswin_t1 - ss_t1
bs_t1 = bsµ_t1 / ss_t1
ws_t1 = wsµ_t1 / ss_t1
ls_t1 = lsµ_t1 / ss_t1

#trial 2
#define win and loss variables
b1w_t2 = round(adj.gamble(adj.b1r_t2,b1o),ndigits=2)
b1L_t2 = -adj.b1r_t2
b2w_t2 = round(adj.gamble(adj.b2r_t2,b2o),ndigits=2)
b2L_t2 = -adj.b2r_t2
bcs_t2 = round((b1w_t2+b2w_t2),ndigits=2)
winloss_t2 = round((b1w_t2+b2L_t2),ndigits=2)
losswin_t2 = round((b1L_t2+b2w_t2),ndigits=2)
#sum stats
risk_sum_t2 = adj.b1r_t2 + adj.b2r_t2
win_sum_t2 = b1w_t2 + b2w_t2
wr_t2 = win_sum_t2 / risk_sum_t2
ss_t2 = (bcs_t2 + winloss_t2 + losswin_t2)/3
sr_t2 = ss_t2 / risk_sum_t2
bsµ_t2 = bcs_t2 - ss_t2
wsµ_t2 = winloss_t2 - ss_t2
lsµ_t2 = losswin_t2 - ss_t2
bs_t2 = bsµ_t2 / ss_t2
ws_t2 = wsµ_t2 / ss_t2
ls_t2 = lsµ_t2 / ss_t2

#trial 3
#define win and loss variables
b1w_t3 = round(adj.gamble(adj.b1r_t3,b1o),ndigits=2)
b1L_t3 = -adj.b1r_t3
b2w_t3 = round(adj.gamble(adj.b2r_t3,b2o),ndigits=2)
b2L_t3 = -adj.b2r_t3
bcs_t3 = round((b1w_t3+b2w_t3),ndigits=2)
winloss_t3 = round((b1w_t3+b2L_t3),ndigits=2)
losswin_t3 = round((b1L_t3+b2w_t3),ndigits=2)
#sum stats
risk_sum_t3 = adj.b1r_t3 + adj.b2r_t3
win_sum_t3 = b1w_t3 + b2w_t3
wr_t3 = win_sum_t3 / risk_sum_t3
ss_t3 = (bcs_t3 + winloss_t3 + losswin_t3)/3
sr_t3 = ss_t3 / risk_sum_t3
bsµ_t3 = bcs_t3 - ss_t3
wsµ_t3 = winloss_t3 - ss_t3
lsµ_t3 = losswin_t3 - ss_t3
bs_t3 = bsµ_t3 / ss_t3
ws_t3 = wsµ_t3 / ss_t3
ls_t3 = lsµ_t3 / ss_t3

#trial 4
#define win and loss variables
b1w_t4 = round(adj.gamble(adj.b1r_t4,b1o),ndigits=2)
b1L_t4 = -adj.b1r_t4
b2w_t4 = round(adj.gamble(adj.b2r_t4,b2o),ndigits=2)
b2L_t4 = -adj.b2r_t4
bcs_t4 = round((b1w_t4+b2w_t4),ndigits=2)
winloss_t4 = round((b1w_t4+b2L_t4),ndigits=2)
losswin_t4 = round((b1L_t4+b2w_t4),ndigits=2)
#sum stats
risk_sum_t4 = adj.b1r_t4 + adj.b2r_t4
win_sum_t4 = b1w_t4 + b2w_t4
wr_t4 = win_sum_t4 / risk_sum_t4
ss_t4 = (bcs_t4 + winloss_t4 + losswin_t4)/3
sr_t4 = ss_t4 / risk_sum_t4
bsµ_t4 = bcs_t4 - ss_t4
wsµ_t4 = winloss_t4 - ss_t4
lsµ_t4 = losswin_t4 - ss_t4
bs_t4 = bsµ_t4 / ss_t4
ws_t4 = wsµ_t4 / ss_t4
ls_t4 = lsµ_t4 / ss_t4






#describe bets and scenarios DataFrame

legend = []
ogx = []
t1x = []
t2x = []
t3x = []
t4x = []

legend.append("Over:")
legend.append("Under:")
legend.append("b1risk")
legend.append("b1win")
legend.append("b2risk")
legend.append("b2win")
legend.append("bcs")
legend.append("winloss")
legend.append("losswin")

ogx.append(b1s)
ogx.append(b2s)
ogx.append(b1r)
ogx.append(b1w)
ogx.append(b2r)
ogx.append(b2w)
ogx.append(adj.bcs)
ogx.append(adj.winloss)
ogx.append(adj.losswin)

t1x.append(b1s)
t1x.append(b2s)
t1x.append(adj.b1r_t1)
t1x.append(b1w_t1)
t1x.append(adj.b2r_t1)
t1x.append(b2w_t1)
t1x.append(bcs_t1)
t1x.append(winloss_t1)
t1x.append(losswin_t1)

t2x.append(b1s)
t2x.append(b2s)
t2x.append(adj.b1r_t2)
t2x.append(b1w_t2)
t2x.append(adj.b2r_t2)
t2x.append(b2w_t2)
t2x.append(bcs_t2)
t2x.append(winloss_t2)
t2x.append(losswin_t2)

t3x.append(b1s)
t3x.append(b2s)
t3x.append(adj.b1r_t3)
t3x.append(b1w_t3)
t3x.append(adj.b2r_t3)
t3x.append(b2w_t3)
t3x.append(bcs_t3)
t3x.append(winloss_t3)
t3x.append(losswin_t3)

t4x.append(b1s)
t4x.append(b2s)
t4x.append(adj.b1r_t4)
t4x.append(b1w_t4)
t4x.append(adj.b2r_t4)
t4x.append(b2w_t4)
t4x.append(bcs_t4)
t4x.append(winloss_t4)
t4x.append(losswin_t4)


print()

trialz = pd.DataFrame({'key': legend, 'og': ogx, 't1': t1x, 't2': t2x, 't3': t3x, 't4': t4x})

#print(trialz)







#statistical analysis (x1) DataFrame

legend1 = []
tx1 = []
t1x1 = []
t2x1 = []
t3x1 = []
t4x1 = []

legend1.append(b1sT)
legend1.append(b2sT)
legend1.append("∑risk")
legend1.append("∑win")
legend1.append("∑w/∑r")
legend1.append("sµ") #scenario avg is scenario sum (bcs + wl + lw) divided by the number of scenarios
legend1.append("sµ/∑r")

tx1.append(adj.b1r)
tx1.append(adj.b2r)
tx1.append(risk_sum)
tx1.append(win_sum)
tx1.append(wr)
tx1.append(ss)
tx1.append(sr)

t1x1.append(adj.b1r_t1)
t1x1.append(adj.b2r_t1)
t1x1.append(risk_sum_t1)
t1x1.append(win_sum_t1)
t1x1.append(wr_t1)
t1x1.append(ss_t1)
t1x1.append(sr_t1)

t2x1.append(adj.b1r_t2)
t2x1.append(adj.b2r_t2)
t2x1.append(risk_sum_t2)
t2x1.append(win_sum_t2)
t2x1.append(wr_t2)
t2x1.append(ss_t2)
t2x1.append(sr_t2)

t3x1.append(adj.b1r_t3)
t3x1.append(adj.b2r_t3)
t3x1.append(risk_sum_t3)
t3x1.append(win_sum_t3)
t3x1.append(wr_t3)
t3x1.append(ss_t3)
t3x1.append(sr_t3)

t4x1.append(adj.b1r_t4)
t4x1.append(adj.b2r_t4)
t4x1.append(risk_sum_t4)
t4x1.append(win_sum_t4)
t4x1.append(wr_t4)
t4x1.append(ss_t4)
t4x1.append(sr_t4)




#create dataframe

x_one = pd.DataFrame({'key': legend1, 'og': tx1, 't1': t1x1, 't2': t2x1, 't3': t3x1, 't4': t4x1})

#horizontal x_one = pd.DataFrame([legend1, tx1, t1x1, t2x1, t3x1, t4x1], index=['key', 'og', 't1', 't2', 't3', 't4'])

#x_one['avg'] = (x_one['og'] + x_one['t1'] + x_one['t2'] + x_one['t3'] + x_one['t4'])/5


print()
#print(x_one)



#scenario avg DataFrame

legen = []
one = []
s1x = []
s2x = []
s3x = []
s4x = []

legen.append("sµ")
legen.append("bcs")
legen.append("bcs-sµ")
legen.append("bsµ/sµ")
legen.append("winloss")
legen.append("wl-sµ")
legen.append("wsµ/sµ")
legen.append("losswin")
legen.append("lw-sµ")
legen.append("lsµ/sµ")



one.append(ss)
s1x.append(ss_t1)
s2x.append(ss_t2)
s3x.append(ss_t3)
s4x.append(ss_t4)

one.append(adj.bcs)
one.append(bsµ)
one.append(bs)

one.append(adj.winloss)
one.append(wsµ)
one.append(ws)

one.append(adj.losswin)
one.append(lsµ)
one.append(ls)


s1x.append(bcs_t1)
s1x.append(bsµ_t1)
s1x.append(bs_t1)

s1x.append(winloss_t1)
s1x.append(wsµ_t1)
s1x.append(ws_t1)

s1x.append(losswin_t1)
s1x.append(lsµ_t1)
s1x.append(ls_t1)


s2x.append(bcs_t2)
s2x.append(bsµ_t2)
s2x.append(bs_t2)

s2x.append(winloss_t2)
s2x.append(wsµ_t2)
s2x.append(ws_t2)

s2x.append(losswin_t2)
s2x.append(lsµ_t2)
s2x.append(ls_t2)


s3x.append(bcs_t3)
s3x.append(bsµ_t3)
s3x.append(bs_t3)

s3x.append(winloss_t3)
s3x.append(wsµ_t3)
s3x.append(ws_t3)

s3x.append(losswin_t3)
s3x.append(lsµ_t3)
s3x.append(ls_t3)


s4x.append(bcs_t4)
s4x.append(bsµ_t4)
s4x.append(bs_t4)

s4x.append(winloss_t4)
s4x.append(wsµ_t4)
s4x.append(ws_t4)

s4x.append(losswin_t4)
s4x.append(lsµ_t4)
s4x.append(ls_t4)



statz = pd.DataFrame({'key': legen, 'og': one, 's1': s1x, 's2': s2x, 's3': s3x, 's4': s4x})

print(statz)
print()
print()
