import pandas as pd
import numpy as np
import  random
import matplotlib.pyplot as plt
import overpass
#api = overpass.API()
import datetime
from matplotlib.backends.backend_pdf import PdfPages
################### fichier pdf ##############################
pp = PdfPages(' Exploration communes.pdf')
firstPage = plt.figure(figsize=(11.69,8.27))
firstPage.clf()
txt = "Poucentage d'abstension par commune"
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=12, ha="center")
pp.savefig()



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

plt.bar(range(100), communes)
plt.title("Nombre de communes par pourcentage d'abstention")
plt.ylabel('Nombre de communes')
plt.xlabel('% Abs/Ins')

pp.savefig()
pp.close()