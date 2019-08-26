import pandas as pd
import numpy as np
import os
import rebound


data = pd.read_csv("DataEnigma", dtype={"NO": int, "NOBS": int, "OBS": int,
"OBSLAST": int, "EPOCH": float, "CALEPO": float, "MA": float, "W": float, "OM": float, "IN": float, "EC": float, "A": float, "QR": float, "TP": float,
"TPCAL": float, "TPFRAC": float, "SOLDAT": float, "DESIG": str, "IREF": str, "ASTNAM": str})


data = data[['ASTNAM', 'MA', "EC", "IN"]]

lst = [x.ASTNAM for x in data.itertuples(index=False) if (x.A>=2.9999 and x.A<=2.99999)]
lst = set(lst)

for ind, x in enumerate(lst,1):
#     print("Object {} : {}".format(ind,x))
