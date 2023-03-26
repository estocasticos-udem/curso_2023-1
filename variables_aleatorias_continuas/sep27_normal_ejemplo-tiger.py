# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 08:13:26 2022

@author: b12s301e19
"""


import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt

mu = 304
sigma = 8

# Variable Aleatoria: X ~ N(mu = 304, sigma = 8)
X = stats.norm(loc = mu, scale = sigma)

# P1 = P(x >= 290) = 1 - P(x <= 290) = 1 - F(290)
x1 = 290
P1 = 1 - X.cdf(x1)
print("P(x <= 290) =", P1)

# P2 = P(305 < x < 0.325)
P2 = X.cdf(325) - X.cdf(305) # P3 = F(325) - F(305)
print("P(305 < x < 0.325) =", P2)

x = np.arange(272,336,0.05)



fig, (ax1, ax2) = plt.subplots(2, 1)

# FDP
f = X.pdf(x)
ax1.plot(x, f)
ax1.set(ylabel='f')
ax1.grid()
# FDA
F = X.cdf(x)
ax2.plot(x, F)
ax2.set(xlabel='Distancia recorrida',
        ylabel='F')
ax2.grid()

