import pandas as pd
import numpy as np
import  random
import matplotlib.pyplot as plt
import overpass
#api = overpass.API()
import datetime
from matplotlib.backends.backend_pdf import PdfPages


################### fichier pdf ##############################
pp = PdfPages( 'Exploration abstentions.pdf')
firstPage = plt.figure(figsize=(11.69,8.27))
firstPage.clf()
txt = "titre "
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=12, ha="center")
pp.savefig(firstPage)



data = pd.read_csv('../../data/raw/Presid_2017_Communes_Tour_1.csv')

alist = list()
absten = list()
communes = list()
inscrits = list()
for i in range(100):
    larger = data['% Abs/Ins'] > i
    smaller = data['% Abs/Ins'] <= i+1
    alist.append(data[larger & smaller])
    #print(alist[i]['Inscrits'].sum())
    absten.append(alist[i]['Abstentions'].sum())
    inscrits.append(alist[i]['Inscrits'].sum())
    #print(len(alist[i]), " communes ", i, "% d'abstention pour ", inscrits[i], " inscrits")

    communes.append(len(alist[i]))
fig1 = plt.figure(figsize=(14,10))
plt.bar(range(100), communes)
plt.title("Nombre de communes par pourcentage d'abstention")
plt.ylabel('Nombre de communes')
plt.xlabel('% Abs/Ins')

pp.savefig(fig1)

fig2 = plt.figure(figsize=(14,10))
plt.bar(range(100), inscrits)
plt.title("Nombre d'inscrits dans les communes par pourcentage d'abstention")
plt.ylabel("Nombre d'inscrtis")
plt.xlabel('% Abs/Ins')

pp.savefig(fig2)

fig3 = plt.figure(figsize=(14,10))
plt.bar(range(100), absten)
plt.title("Nombre d'abstentions dans les communes par pourcentage d'abstention")
plt.ylabel("Nombre d'inscrtis")
plt.xlabel('% Abs/Ins')

pp.savefig(fig3)



word_list = ['Haute-Corse', 'Corse-du-Sud', 'La Réunion','Nouvelle-Calédonie','Guadeloupe','Martinique','Guyane','Mayotte','Saint-Martin/Saint-Barthélemy','Polynésie française','Français établis hors de France']
df_metro = data

for word in word_list:
    df_metro = df_metro[~df_metro["Libellé du département"].str.contains(word)] #string does not contain


alist = list()
absten = list()
communes = list()
inscrits = list()
for i in range(100):
    larger = df_metro['% Abs/Ins'] > i
    smaller = df_metro['% Abs/Ins'] <= i+1
    alist.append(df_metro[larger & smaller])
    #print(alist[i]['Inscrits'].sum())
    absten.append(alist[i]['Abstentions'].sum())
    inscrits.append(alist[i]['Inscrits'].sum())


fig4 = plt.figure(figsize=(14,10))
plt.bar(range(100), absten)
plt.title("Nombre d'abstentions dans les communes par pourcentage d'abstention en France Métropolitaine")
plt.ylabel("Nombre d'inscrtis")
plt.xlabel('% Abs/Ins')

pp.savefig(fig4)

pp.close()