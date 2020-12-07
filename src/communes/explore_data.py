import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages

################### fichier pdf ##############################



pp = PdfPages( 'Exploration abstentions' +str(datetime.now())+'.pdf')
firstPage = plt.figure(figsize=(11.69,8.27))
#firstPage.clf()
txt = "titre "
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=12, ha="center")
pp.savefig(firstPage)



data = pd.read_csv('../../data/raw/Presid_2017_Communes_Tour_1.csv')
df_bureaux = pd.read_table("../../data/raw/PR17_BVot_T1_FE (copy).txt", encoding = "ISO-8859-1", sep =';', decimal =',')

class hist:
    def __init__(self, a):
        self.df = a
        self.nombre = list()
        self.inscrits = list()
        self.asbten = list()

    def m(self):
        print(self.df)

    def prep_hist(self):
        for i in range(100):
            larger = data['% Abs/Ins'] > i
            smaller = data['% Abs/Ins'] <= i + 1
            el = data[larger & smaller]
            # print(alist[i]['Inscrits'].sum())
            self.asbten.append(el['Abstentions'].sum())
            self.inscrits.append(el['Inscrits'].sum())
            # print(len(alist[i]), " communes ", i, "% d'abstention pour ", inscrits[i], " inscrits")

            self.nombre.append(len(el.index))

    def plot_hist(self, f_rame, title=None, ylabel=None, xlabel=None):
        fig1 = plt.figure(figsize=(14, 10))
        plt.bar(range(100), f_rame)
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)

        pp.savefig(fig1)
        plt.close()



z = hist(data)
#print(hist.df['% Abs/Ins'])

#print(z.df['% Abs/Ins'])
z.prep_hist()
z.plot_hist(z.nombre, "Nombre de communes par pourcentage d'abstention", 'Nombre de communes', '% Abs/Ins')

z.plot_hist(z.inscrits, "Nombre d'inscrits dans les communes par pourcentage d'abstention", "Nombre d'inscrits" , '% Abs/Ins')
z.plot_hist(z.asbten, "Nombre d'abstentions dans les communes par pourcentage d'abstention", "Nombre d'abstentions" , '% Abs/Ins')

# fig1 = plt.figure(figsize=(14, 10))
# plt.bar(range(100), z.nombre)
# plt.title("Nombre de communes par pourcentage d'abstention")
# plt.ylabel('Nombre de communes')
# plt.xlabel('% Abs/Ins')
#
# pp.savefig(fig1)
# plt.close()

pp.close()