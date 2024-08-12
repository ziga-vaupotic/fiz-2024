import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from collections import defaultdict
import math as mt 
import matplotlib.ticker as ticker


import sys
sys.path.append('..')
import plots

ex = pd.read_csv('Untitled2.csv')
keyss = ex.keys()

new_table = defaultdict(lambda : [])

for k in range(0, mt.floor((len(keyss)) /2) - 1):
    for i in range(0, len(ex[keyss[0]]) - 1):
        new_table[keyss[k + 1]].append(float(str(int(ex[keyss[k * 2 + 1]][i])) + "." + str(int(ex[keyss[k*2 + 2]][i]))))


P = [x for x in new_table["tlak"]]
T = [x for x in new_table["temperatura Kelvin"]]

fig, ax = plt.subplots(figsize=(8, 5))

#print(plt.yticks())
#plt.yticks([plt.yticks().index(x) for x in plt.yticks() if x[0].is_integer()])
 
ax.set_xlim(50, max(T))


x_apr = np.linspace(20, max(T), 20)

polyfit = np.polyfit(np.array(T), np.array(P), 1)

linear_approx = np.poly1d(polyfit)


ax.plot(x_apr, linear_approx(x_apr), label="$V = V_0$", linestyle="solid")



polyfit2 = np.polyfit(np.array(T), np.array(P), 1)

polyfit2[0] -= 0.12
linear_approx2 = np.poly1d(polyfit2)

ax.plot(x_apr, linear_approx2(x_apr), label="$V > V_0$", linestyle="dashed")

polyfit3 = np.polyfit(np.array(T), np.array(P), 1)

polyfit3[0] += 0.12

linear_approx3 = np.poly1d(polyfit3)


ax.plot(x_apr, linear_approx3(x_apr), label="$V < V_0$", linestyle="dashed")

ax.grid(linestyle="dotted")
ax.legend()
ax.set_title("Prikaz funkcije p(T) za različne začetne prostornine")
ax.set_xlabel(r"Temperatura $[K]$")
ax.set_ylabel(r"Tlak $[kPa]$")
plt.savefig("diab-prikaz.pdf", dpi=200)
#print(ex.keys())
