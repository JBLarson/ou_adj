import pandas as pd
import numpy as np
from numpy import random
import matplotlib.pyplot as plt

import input_adj as adj

#import risk variables for analysis
b1s = adj.b1s
b2s = adj.b2s
b1r = adj.b1r
b2r = adj.b2r
b1o = adj.b1o
b2o = adj.b2o
b1w = adj.b1w
b2w = adj.b2w
bcs = adj.bcs
winloss = adj.winloss
losswin = adj.losswin
bcsT = adj.bcsT
winlossT = adj.winlossT
losswinT = adj.losswinT

#artificial numbers ou
if adj.comb == 'ou':
	#small num ou

	if b1s >= 30 and b1s <= 36:
		small_num = 28
	elif b1s > 36 and b1s <= 43:
		small_num = 34
	elif b1s > 43 and b1s <= 49:
		small_num = 38
	elif b1s > 49 and b1s <= 55:
		small_num = 46
	elif b1s > 55 and b1s <= 60:
		small_num = 51
	elif b1s >= 60:
		small_num = 52
	elif b1s < 30:
		small_num = 26

	#big num ou

	if b2s >= 33 and b2s < 40:
		big_num = 42
	elif b2s >= 40 and b2s < 48:
		big_num = 51
	elif b2s >= 48 and b2s < 54:
		big_num = 56
	elif b2s >= 54 and b2s < 60:
		big_num = 58
	elif b2s >= 60:
		big_num = 65
	elif b2s < 33:
		big_num = 39

#artificial numbers

med_num = (big_num+small_num)/2
avg = (b1s+b2s)/2

#ranges for over/under combination
if adj.comb == 'ou':

	med = ((b2s + med_num) - (b1s + avg))/4

	if avg < 35:		
		wl_range = ((big_num - b2s) + (b2s - small_num)) / 1.55

		lw_range = ((big_num - b1s) + (big_num - b1s)) / 1.7
	elif avg >= 35 and avg < 45:
		wl_range = ((big_num - b2s) + (b2s - small_num)) / 1.9

		lw_range = ((big_num - b1s) + (big_num - b1s)) / 1.95
	elif avg >= 45 and avg < 60:
		wl_range = ((big_num - b2s) + (b2s - small_num)) / 1.4

		lw_range = ((big_num - b1s) + (big_num - b1s)) / 1.3
	elif avg >= 60:
		wl_range = ((big_num - b2s) + (b2s - small_num)) / 1.5

		lw_range = ((big_num - b1s) + (big_num - b1s)) / 1.4

	bcs_range = b2s - b1s

	#alternate trials

	#p1 (high estimate) ranges
	if adj.b1t == 'o' and adj.b2t == 'u':
		p1_wl_range = wl_range * 1.2

		p1_lw_range = lw_range * .8
	elif adj.b1t == 'u' and adj.b2t == 'o':
		p1_wl_range = wl_range * .8

		p1_lw_range = lw_range * 1.2
	#p2 (low estimate) ranges
	if adj.b1t == 'o' and adj.b2t == 'u':
		p2_wl_range = wl_range * .8

		p2_lw_range = lw_range * 1.2
	elif adj.b1t == 'u' and adj.b2t == 'o':
		p2_wl_range = wl_range * 1.2

		p2_lw_range = lw_range * .8
	#p3 (v-high estimate) ranges
	if adj.b1t == 'o' and adj.b2t == 'u':
		p3_wl_range = wl_range * 1.4

		p3_lw_range = lw_range * .6
	elif adj.b1t == 'u' and adj.b2t == 'o':
		p3_wl_range = wl_range * .6

		p3_lw_range = lw_range * 1.4
	#p4 (v-low estimate) ranges
	if adj.b1t == 'o' and adj.b2t == 'u':
		p4_wl_range = wl_range * .55

		p4_lw_range = lw_range * 1.45
	elif adj.b1t == 'u' and adj.b2t == 'o':
		p4_wl_range = wl_range * 1.45

		p4_lw_range = lw_range * .55


#total range and rp for prob

total_range = (bcs_range + wl_range + lw_range)

bcs_rp = float(bcs_range / total_range)
wl_rp = float(wl_range / total_range)
lw_rp = float(lw_range / total_range)

#og random.choice() method



#win and loss variables to make scenario variables
b1w_t1 = round(adj.gamble(adj.b1r_t1,b1o),ndigits=2)
b1L_t1 = -adj.b1r_t1
b2w_t1 = round(adj.gamble(adj.b2r_t1,b2o),ndigits=2)
b2L_t1 = -adj.b2r_t1
b1w_t2 = round(adj.gamble(adj.b1r_t2,b1o),ndigits=2)
b1L_t2 = -adj.b1r_t2
b2w_t2 = round(adj.gamble(adj.b2r_t2,b2o),ndigits=2)
b2L_t2 = -adj.b2r_t2
b1w_t3 = round(adj.gamble(adj.b1r_t3,b1o),ndigits=2)
b1L_t3 = -adj.b1r_t3
b2w_t3 = round(adj.gamble(adj.b2r_t3,b2o),ndigits=2)
b2L_t3 = -adj.b2r_t3
b1w_t4 = round(adj.gamble(adj.b1r_t4,b1o),ndigits=2)
b1L_t4 = -adj.b1r_t4
b2w_t4 = round(adj.gamble(adj.b2r_t4,b2o),ndigits=2)
b2L_t4 = -adj.b2r_t4

#define scenario variables for each trial
bcs_t1 = round((b1w_t1+b2w_t1),ndigits=2)
winloss_t1 = round((b1w_t1+b2L_t1),ndigits=2)
losswin_t1 = round((b1L_t1+b2w_t1),ndigits=2)
bcs_t2 = round((b1w_t2+b2w_t2),ndigits=2)
winloss_t2 = round((b1w_t2+b2L_t2),ndigits=2)
losswin_t2 = round((b1L_t2+b2w_t2),ndigits=2)
bcs_t3 = round((b1w_t3+b2w_t3),ndigits=2)
winloss_t3 = round((b1w_t3+b2L_t3),ndigits=2)
losswin_t3 = round((b1L_t3+b2w_t3),ndigits=2)
bcs_t4 = round((b1w_t4+b2w_t4),ndigits=2)
winloss_t4 = round((b1w_t4+b2L_t4),ndigits=2)
losswin_t4 = round((b1L_t4+b2w_t4),ndigits=2)


#relative probability and total range (p1-p4)
#total range and rp p1
p1_total_range = (bcs_range + p1_wl_range + p1_lw_range)
p1_bcs_rp = float(bcs_range / p1_total_range)
p1_wl_rp = float(p1_wl_range / p1_total_range)
p1_lw_rp = float(p1_lw_range / p1_total_range)
#total range and rp p2
p2_total_range = (bcs_range + p2_wl_range + p2_lw_range)
p2_bcs_rp = float(bcs_range / p2_total_range)
p2_wl_rp = float(p2_wl_range / p2_total_range)
p2_lw_rp = float(p2_lw_range / p2_total_range)
#total range and rp p3
p3_total_range = (bcs_range + p3_wl_range + p3_lw_range)
p3_bcs_rp = float(bcs_range / p3_total_range)
p3_wl_rp = float(p3_wl_range / p3_total_range)
p3_lw_rp = float(p3_lw_range / p3_total_range)
#total range and rp p4
p4_total_range = (bcs_range + p4_wl_range + p4_lw_range)
p4_bcs_rp = float(bcs_range / p4_total_range)
p4_wl_rp = float(p4_wl_range / p4_total_range)
p4_lw_rp = float(p4_lw_range / p4_total_range)

#og and 4 trials
prob = pd.Series(adj.random.choice([bcs, winloss, losswin], p=[bcs_rp, wl_rp, lw_rp], size=(adj.n)))
p1 = pd.Series(random.choice([bcs_t1, winloss_t1, losswin_t1], p=[p1_bcs_rp, p1_wl_rp, p1_lw_rp], size=(adj.n)))
p2 = pd.Series(random.choice([bcs_t2, winloss_t2, losswin_t2], p=[p2_bcs_rp, p2_wl_rp, p2_lw_rp], size=(adj.n)))
p3 = pd.Series(random.choice([bcs_t3, winloss_t3, losswin_t3], p=[p3_bcs_rp, p3_wl_rp, p3_lw_rp], size=(adj.n)))
p4 = pd.Series(random.choice([bcs_t4, winloss_t4, losswin_t4], p=[p4_bcs_rp, p4_wl_rp, p4_lw_rp], size=(adj.n)))

bcs_count = adj.np.count_nonzero(prob == bcs)
wl_count = adj.np.count_nonzero(prob == winloss)
lw_count = adj.np.count_nonzero(prob == losswin)
bcsf = (bcs_count / adj.n)*100
wlf = (wl_count / adj.n)*100
lwf = (lw_count / adj.n)*100

bcs_count_t1 = adj.np.count_nonzero(p1 == bcs_t1)
wl_count_t1 = adj.np.count_nonzero(p1 == winloss_t1)
lw_count_t1 = adj.np.count_nonzero(p1 == losswin_t1)
bcsf_t1 = (bcs_count_t1 / adj.n)*100
wlf_t1 = (wl_count_t1 / adj.n)*100
lwf_t1 = (lw_count_t1 / adj.n)*100

bcs_count_t2 = adj.np.count_nonzero(p2 == bcs_t2)
wl_count_t2 = adj.np.count_nonzero(p2 == winloss_t2)
lw_count_t2 = adj.np.count_nonzero(p2 == losswin_t2)
bcsf_t2 = (bcs_count_t2 / adj.n)*100
wlf_t2 = (wl_count_t2 / adj.n)*100
lwf_t2 = (lw_count_t2 / adj.n)*100

bcs_count_t3 = adj.np.count_nonzero(p3 == bcs_t3)
wl_count_t3 = adj.np.count_nonzero(p3 == winloss_t3)
lw_count_t3 = adj.np.count_nonzero(p3 == losswin_t3)
bcsf_t3 = (bcs_count_t3 / adj.n)*100
wlf_t3 = (wl_count_t3 / adj.n)*100
lwf_t3 = (lw_count_t3 / adj.n)*100

bcs_count_t4 = adj.np.count_nonzero(p4 == bcs_t4)
wl_count_t4 = adj.np.count_nonzero(p4 == winloss_t4)
lw_count_t4 = adj.np.count_nonzero(p4 == losswin_t4)
bcsf_t4 = (bcs_count_t4 / adj.n)*100
wlf_t4 = (wl_count_t4 / adj.n)*100
lwf_t4 = (lw_count_t4 / adj.n)*100

print()




#pie-chart visual

#Pie Charts

if adj.comb == 'ou':

	labelz='bcs', 'winloss', 'losswin'
	sizes=[bcsf, wlf, lwf]
	sizes1=[bcsf_t1, wlf_t1, lwf_t1]
	sizes2=[bcsf_t2, wlf_t2, lwf_t2]
	sizes3=[bcsf_t3, wlf_t3, lwf_t3]


fig, axs = plt.subplots(2, 2)


#overall
axs[0,0].pie(sizes,
	explode=(0.1, 0.0, 0.0),
	labels=labelz,
	colors=['green','yellow','red'],
	autopct='%.0f%%',
	radius=0.4)
axs[0,0].axis('equal')
axs[0,0].set_title("OG Trial")


#bcs
axs[0,1].pie(sizes1,
	explode=(0.1, 0.0, 0.0),
	labels=labelz,
	colors=['green','yellow','red'],
	autopct='%.0f%%',
	radius=0.4)
axs[0,1].axis('equal')
axs[0,1].set_title("Trial 1")

#winloss
axs[1,0].pie(sizes2,
	explode=(0.1, 0.0, 0.0),
	labels=labelz,
	colors=['green','yellow','red'],
	autopct='%.0f%%',
	radius=0.4)

axs[1,0].axis('equal')
axs[1,0].set_title("Trial 2")


#losswin
axs[1,1].pie(sizes3,
	explode=(0.1, 0.0, 0.0),
	labels=labelz,
	colors=['green','yellow','red'],
	autopct='%.0f%%',
	radius=0.4)
axs[1,1].axis('equal')
axs[1,1].set_title("Trial 3")


plt.show()




