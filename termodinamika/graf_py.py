import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
import math as mt 
import matplotlib.ticker as ticker
from scipy.optimize import curve_fit
from matplotlib.patches import Polygon
from scipy import integrate

import sys
sys.path.append('..')
import plots



ex = pd.read_csv('Untitled.csv')
keyss = ex.keys()

P = [x for x in ex["Pressure1"]]
V = [x for x in ex["Volume1"]]

print(V)
print(P)


def func(x, a, b, c):
    return a**(-x+b) + c



fig, ax = plt.subplots( figsize=(8,5))

ax.scatter(np.array(V), np.array(P), marker="+", label="Meritve")


x_apr = np.linspace(0, max(V) + 3, 100)
popt, pcov = curve_fit(func, V, P)

ax.plot(x_apr, func(x_apr, *popt), label="Približek", linestyle="dashed", color="black")

#for i,x in enumerate(P):
#    if(i == len(P) - 1):
#        continue

#    plt.gca().add_patch(plt.Rectangle((V[i], 0), abs(V[i] - V[i+1]) -0.07 , abs( (P[i+1] + P[i]) / 2), alpha=0.2, color="purple", label="Ploščina" if i == 1 else "")
#)

x_apr_2 = np.linspace(min(V), max(V), 100)
ax.fill_between(x_apr_2,func(x_apr_2, *popt), color="black", alpha=0.2, label="Ploščina")


print(integrate.trapezoid(x_apr_2,func(x_apr_2, *popt)))

ax.grid(linestyle="dotted")
ax.legend()
ax.set_xlim([0, max(V) + 3])
ax.set_title("Odvisnost tlaka od prostornine")
ax.set_xlabel(r"Prostornina $[mL]$")
ax.set_ylabel(r"Tlak $[kPa]$")
plt.savefig("pv.pdf")
#print(ex.keys())