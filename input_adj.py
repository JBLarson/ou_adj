#import packages and define gamble

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

def gamble(y,z):
	return round((y*(z-1)),ndigits=2)


#bet1 and bet2 input

b1s = float(43)
b1t = ("o")
b1o = float(1.952)
b1r = float(35)


b2s = float(47)
b2sx = float(-50)
b2t = ("u")
b2o = float(1.87)
b2r = float(38)

#number of trials
n = 1000

#define combination variable
if b1t == 'o' and b2t == 'u':
	comb = 'ou'
elif b1t == 'u' and b2t == 'o':
	comb = 'uo'

b1w = round(gamble(b1r,b1o),ndigits=2)
b1L = -b1r
b2w = round(gamble(b2r,b2o),ndigits=2)
b2L = -b2r

bcs = round((b1w+b2w),ndigits=2)
winloss = round((b1w+b2L),ndigits=2)
losswin = round((b1L+b2w),ndigits=2)

bcsT = "bcs: $" + str(bcs)
winlossT = "winloss: $" + str(winloss)
losswinT = "losswin: $" + str(losswin)

#describe bets
if comb == 'ou':
	print("Bet 1 | Over:",b1s,"pts - Risks: $",b1r,"Nets: $",b1w)
	print("Bet 2 | Under:",b2s,"pts - Risks: $",b2r,"Nets : $",b2w)

elif comb == 'uo':
	print("Bet 1 | Under:",b1s,"pts - Risks $",b1r,"Nets: $",b1w)
	print("Bet 2 | Over:",b2s,"pts - Risks: $",b2r,"Nets: $",b2w)










#adjustment values have a range of 0-1. 
#adj values determine how b1r and b2r will change in alternate trials.

#adjustment t1
adj_t1 = .35
#risk variables for trial
b1r_t1 = b1r + (adj_t1*b1r)
b2r_t1 = b2r - (adj_t1*b2r)

#adjustment t2
adj_t2 = .42
#risk variables for trial
b1r_t2 = b1r + (adj_t2*b1r)
b2r_t2 = b2r - (adj_t2*b2r)

#adjustment t3
adj_t3 = .33
#risk variables for trial
b1r_t3 = b1r - (adj_t3*b1r)
b2r_t3 = b2r + (adj_t3*b2r)

#adjustment t4
adj_t4 = .45
#risk variables for trial
b1r_t4 = b1r - (adj_t4*b1r)
b2r_t4 = b2r + (adj_t4*b2r)

