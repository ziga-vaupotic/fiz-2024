import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
sys.path.append('..')
import plots

def function(x, T_s):
    K = 511 * T_s #PaL
    print(x)
    return K * 1/x

x = np.linspace(1, 30, 100)

fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(x, function(x, 1), label=r'$T=T_r$')
ax.plot(x, function(x, 5/4), label=r'$T > T_r$', linestyle="dashed")
ax.plot(x, function(x, 3/4), label=r'$T < T_r$', linestyle="dashed")
ax.set_ylim(0, 250)
ax.set_title(r"Prikaz funkcije $p(V)$ za različne temperature")
ax.set_ylabel(r"Tlak $[kPa]$")
ax.set_xlabel(r"Prostornina $[L]$")
ax.grid(linestyle="dotted")
ax.legend()
plt.savefig("ponazoritev.pdf")