import pandas as pd
import numpy as np
import os


data = pd.read_csv("DataEnigma", dtype={"NO": int, "NOBS": int, "OBS": int,
"OBSLAST": int, "EPOCH": float, "CALEPO": float, "MA": float, "W": float, "OM": float, "IN": float, "EC": float, "A": float, "QR": float, "TP": float,
"TPCAL": float, "TPFRAC": float, "SOLDAT": float, "DESIG": str, "IREF": str, "ASTNAM": str})


data = data[['ASTNAM', 'QR', 'EC']]

maxPer = -1.0
minPer = 1000000000000.0
maxAph = -1.0
minAph = 1000000000000.0


maxPerObj = ''
minPerObj = ''
maxAphObj = ''
minAphObj = ''

for x in data.itertuples(index=False):
    if x.QR<0:
        continue
    if x.QR > maxPer:
        maxPer = x.QR
        maxPerObj = x.ASTNAM
    if x.QR < minPer and x.QR>0:
        minPer = x.QR
        minPerObj = x.ASTNAM
    aph = (x.QR * (1+x.EC))/(1-x.EC)
    if aph > maxAph:
        maxAph = aph
        maxAphObj = x.ASTNAM
    if aph < minAph and aph>0:
        minAph = aph
        minAphObj = x.ASTNAM


print("Maximum Perihelion--> {} : {}".format(maxPerObj, maxPer))
print("Minimum Perihelion--> {} : {}".format(minPerObj, minPer))
print("Maximum Aphelion--> {} : {}".format(maxAphObj, maxAph))
print("Minimum Aphelion--> {} : {}".format(minAphObj, minAph))
