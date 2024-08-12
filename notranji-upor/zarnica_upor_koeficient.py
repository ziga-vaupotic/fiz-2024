import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import ploti

df = pd.read_excel('fizika_podatki_vaja_zarnica.xlsx')

print(df.keys())

napetost_upornik = []
tok_upornik = []
upor_upornik = []

napetost_zarnica = []
tok_zarnica = []
upor_zarnice = []

for i in df.keys():
    if(i == "n"):
        continue
    if(i == 1):
        continue
    napetost_upornik.append(df[i][0])
    tok_upornik.append(df[i][1] / 1000)
    upor_upornik.append(df[i][0] / (df[i][1] / 1000))

    napetost_zarnica.append(df[i][7])
    tok_zarnica.append(df[i][8] / 1000)
    upor_zarnice.append(df[i][7] / (df[i][8] / 1000))

print(napetost_upornik)


model_upornbik = np.poly1d(np.polyfit(napetost_upornik, upor_upornik, 1))
model_zarnica = np.poly1d(np.polyfit(napetost_zarnica, upor_zarnice, 3))

polyline_upornik = np.linspace(0, 8 , 50)
polyline_zarnica = np.linspace(0, 8, 50)

fig, axs = plt.subplots(1, 2)

axs[0].plot(napetost_upornik, upor_upornik, linestyle="none", marker="x", color ="black", label = "Meritve", markersize = 3)
axs[0].hlines(590, 0, 8, linestyle="dashed" , label="Povprečni upor $\overline{R}$")
axs[0].set_title("Upornik")
axs[0].set_ylim([300,700])
axs[0].set_xlim([0,8.04])
axs[1].plot(napetost_zarnica, upor_zarnice, linestyle="none", marker="d", color ="black", label = "Meritve", markersize = 3)
axs[1].plot(polyline_upornik, model_zarnica(polyline_upornik), linestyle="dashed" , label="Približek uporu $\\tilde{R}$")
axs[1].set_title("Žarnica")

for i in range(0,2):
    axs[i].set_ylabel(r"Upornost $R[\Omega]$")
    axs[i].set_xlabel(r"Napetost $U[V]$")
    axs[i].grid()
    axs[i].legend()

plt.suptitle("Graf upornosti v odvisnosti od napetosti")
plt.savefig("zarnica_upor_upornost.pdf")