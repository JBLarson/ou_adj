import pandas as pd
import execute_adj as ex
import numpy as np

statz = ex.nkstatz
trialz = ex.trialz

desc = pd.DataFrame(trialz[0:6]).copy()
sµ_r = pd.DataFrame(statz[7:11]).copy()


print(ex.statz)

#print(desc)
risk = np.array(desc[0:6])
print()

print(risk)
print()

#print(sµ_r)

bcsr = np.array(sµ_r[:1])
wlr = np.array(sµ_r[1:2])
lwr = np.array(sµ_r[2:3])

bcsrn = np.array(bcsr[0:1])
bcs2 = (bcsrn[0:1])
wlrn = np.array(wlr[0:1])
wl2 = (wlrn[0:1])
lwrn = np.array(lwr[0:1])
lw2 = (lwrn[0:1])

bcsx = np.array(bcs2).tolist()
wlx = np.array(wl2).tolist()
lwx = np.array(lw2).tolist()





bctot = bcsx[0]
wltot = wlx[0]
lwtot = lwx[0]



print("t1 - og (bcs-sµ)/sµ")



bcsµ = (bctot[1]-bctot[0])

wlsµ = (wltot[1]-wltot[0])

lwsµ = (lwtot[1]-lwtot[0])

print(bcsµ)
print(wlsµ)
print(lwsµ)


avgbcs = sum(bctot)/len(bctot)
avgwl = sum(wltot)/len(wltot)
avglw = sum(lwtot)/len(lwtot)

abcs_p = avgbcs*100
awl_p = avgwl*100
alw_p = avglw*100

print()
print("average bcs, wl, and lw dm from sµ")
bsµT = (str(round(abcs_p, ndigits=2)) + "%")
wlsµT = (str(round(awl_p, ndigits=2)) + "%")
lwsµT = (str(round(alw_p, ndigits=2)) + "%")

print(bsµT)
print(wlsµT)
print(lwsµT)


print()
