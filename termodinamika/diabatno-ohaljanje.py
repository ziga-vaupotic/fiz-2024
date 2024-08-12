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
 
ax.scatter(np.array(T), np.array(P), marker="+", label="Meritve")


start, end = plt.xlim()


x_apr = np.linspace(start, end, 4)
linear_approx = np.poly1d(np.polyfit(np.array(T), np.array(P), 1))

print(np.polyfit(np.array(T), np.array(P), 1))

ax.plot(x_apr, linear_approx(x_apr), label="Linearni približek", linestyle="dashed", color="black")




ax.text(303.4, 96.2, r'$p(V) = 0.218 \frac{kPa}{K} \cdot V + 31.5 kPa$', fontsize = 12, 
         bbox = dict(facecolor = 'white', edgecolor="black", linestyle="dashed", alpha = 1))

#ax.arrow(302,  96.5, -1, 0.7, width = 0.02)

circle1 = plt.Circle((300.4, 97.6), 0.4, color='g', fill=False, linestyle="dotted", label="Napaka zaradi ledu")
ax.add_patch(circle1)

ax.grid(linestyle="dotted")
ax.legend()
ax.set_title("Odvisnost tlaka od temperature")
ax.set_xlabel(r"Temperatura $[K]$")
ax.set_ylabel(r"Tlak $[kPa]$")
plt.savefig("diab.pdf", dpi=200)
#print(ex.keys())
