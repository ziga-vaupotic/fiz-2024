import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import ploti

df = pd.read_excel('fizika_podatki_vaja_zarnica.xlsx')

print(df.keys())

napetost_upornik = []
tok_upornik = []

napetost_zarnica = []
tok_zarnica = []

for i in df.keys():
    if(i == "n"):
        continue
    if(i == 1):
        continue
    napetost_upornik.append(df[i][0])
    tok_upornik.append(df[i][1] / 1000)

    napetost_zarnica.append(df[i][7])
    tok_zarnica.append(df[i][8] / 1000)

print(napetost_upornik)

model_upornbik = np.poly1d(np.polyfit(tok_upornik, napetost_upornik, 1))
model_zarnica = np.poly1d(np.polyfit(tok_zarnica, napetost_zarnica, 1))
model_zarnica_2 = np.poly1d(np.polyfit(tok_zarnica, napetost_zarnica, 2))

polyline_upornik = np.linspace(np.min(tok_upornik) - np.max(tok_upornik) * 0.05, np.max(tok_upornik) + np.max(tok_upornik) * 0.05, 50)
polyline_zarnica = np.linspace(np.min(tok_zarnica) - np.min(tok_zarnica) * 0.05, np.max(tok_zarnica) + np.max(tok_zarnica) * 0.05, 50)

fig, axs = plt.subplots(1, 2)

axs[0].plot(tok_upornik, napetost_upornik, linestyle="none", marker=".", color ="black", label = "Meritve")
axs[0].set_title("Upornik")

axs[1].plot(tok_zarnica, napetost_zarnica, linestyle="none", marker="+", color ="black", label = "Meritve")
axs[1].set_title("Žarnica")
axs[0].plot(polyline_upornik, model_upornbik(polyline_upornik), linestyle="dashed" , label="Linearna funkcija")
axs[1].plot(polyline_zarnica, model_zarnica(polyline_zarnica), linestyle="dashed" , label="Linearna funkcija")
axs[1].plot(polyline_zarnica, model_zarnica_2(polyline_zarnica), linestyle="dotted", color="chocolate", label="Kvadratna funkcija")

for i in range(0,2):
    axs[i].set_ylim([0,8])
    axs[i].set_ylabel(r"Napetost $U[V]$")
    axs[i].set_xlabel(r"Tok $I[A]$")
    axs[i].grid()
    axs[i].legend()

plt.suptitle("Graf napetosti v odvisnosti od toka")
plt.savefig("zarnica_upor.pdf")