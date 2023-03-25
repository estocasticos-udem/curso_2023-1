# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 08:31:24 2022

@author: s307e22
"""


import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt


# Distribucion uniforme 𝑋~Exp(l) 
media = 4
l = 1/media
beta = 1/l

# VA: 𝑋 es una variable aleatoria continua ya que el tiempo se mide.


X = stats.expon(scale = media)

x = np.arange(0,40,0.1)

# FDP - Funcion de densidad de probabilidad (f(x))
pdf = X.pdf(x)
plt.plot(x, pdf)
plt.xlabel('X')
plt.ylabel('Probability')
plt.show()

# CDF - Funcion de distribucion acumulativa (F(x))
plt.figure()
cdf = X.cdf(x)
plt.plot(x, cdf)
plt.xlabel('X')
plt.ylabel('CDF')
plt.show()


# P(4 < X < 5)

P = X.cdf(5) - X.cdf(4)
print("P(4 < X < 5) =", P)
mu = X.mean()
sigma = X.var()  # VAR
std = X.std()
print("Media: ", mu)
print("Varianza: ", sigma)
print("Desviacion estandar: ", std)

