# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 09:02:45 2022

@author: b12s301e19
"""

import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

mu = 0
sigma = 1

Z = stats.norm(loc = mu, scale = sigma)

z = np.arange(-4,4.05,0.05)

# FDP
f = Z.pdf(z)

fig, ax1 = plt.subplots()
ax1.plot(z,f)
ax1.set(xlabel = "z",
       ylabel ="f(z)",
       title = "Funcion de probabilidad estandar"
       )
ax1.grid()


# FDA
F = Z.cdf(z)

fig, ax2 = plt.subplots()
ax2.plot(z,F)
ax2.set(xlabel = "z",
       ylabel ="F(z)",
       title = "Funcion de probabilidad acumulativa"
       )
ax2.grid()

# Preguntas de probabilidades

# P1 = P(z <= -1.25)
z1 = -1.25
P1 = Z.cdf(z1)  # P1 = F(z1)
print("P(z <= -1.25) =", P1)

# P2 = P(z => 0.81)
z2 = 0.81
P2 = 1 - Z.cdf(z2) # P2 = 1 - F(z2)
print("P(z => 0.81) =", P2)

# P3 = P(−1.25 < z < 0.81)
P3 = Z.cdf(z2) - Z.cdf(z1) # P3 = F(z2) - F(z1)
print("P(−1.25 < z < 0.81) =", P3)
