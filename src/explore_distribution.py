import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_pdf import PdfPages

################### fichier pdf ##############################
'''
Nous souhaitons visualiser un histogramme du nombre de communes ou bureaux de votes en fonction du pourcentage d'abstention. Cela donne une idée de la distribution des valeurs d'absention

'''


pp = PdfPages( 'DistributionTerritoriale_' +str(datetime.now())+'.pdf')
#firstPage = plt.figure(figsize=(11.69,8.27))
#firstPage.clf()
#txt = "titre "
#firstPage.text(0.5,0.95,txt, transform=firstPage.transFigure, size=22, ha="center")
#firstPage.text(0.5,0.95,txt,  size=22)
#pp.savefig(firstPage)



communes = pd.read_csv('../data/raw/Presid_2017_Communes_Tour_1.csv')
bureaux = pd.read_table("../data/raw/PR17_BVot_T1_FE (copy).txt", encoding = "ISO-8859-1", sep =';', decimal =',')

class hist:
    def __init__(self, a):
        self.df = a
        self.nombre = list()
        self.inscrits = list()
        self.asbten = list()

    def prepare_hist(self):
        for i in range(100):
            larger = self.df['% Abs/Ins'] > i
            smaller = self.df['% Abs/Ins'] <= i + 1
            el = self.df[larger & smaller]
            # print(alist[i]['Inscrits'].sum())
            self.asbten.append(el['Abstentions'].sum())
            self.inscrits.append(el['Inscrits'].sum())
            # print(len(alist[i]), " communes ", i, "% d'abstention pour ", inscrits[i], " inscrits")

            self.nombre.append(len(el.index))

    def plot_hist(self, f_rame, title=None, ylabel=None, xlabel=None):

        plt.bar(range(100), f_rame)
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)


def plott_hist(f_rame, title=None, ylabel=None, xlabel=None):

    plt.bar(range(100), f_rame)
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)


def create_double_histogram(df1,df2, pagetitle = None, title1=None, y1=None, x1=None,  title2=None, y2=None, x2=None):
    fig = plt.figure(figsize=(16, 9))
    fig.text(0.5, 0.95, pagetitle, size=22, ha="center")
    left = plt.subplot(1, 2, 1)
    left.title.set_fontsize(12)
    left.xaxis.label.set_fontsize(14)
    left.yaxis.label.set_fontsize(14)

    plott_hist(df1, title1, y1, x1)

    left = plt.subplot(1, 2, 2)
    left.title.set_fontsize(12)
    left.xaxis.label.set_fontsize(14)
    left.yaxis.label.set_fontsize(14)

    plott_hist(df2, title2, y2, x2)
    pp.savefig(fig)
    plt.close()

z = hist(communes)
za = hist(bureaux)

z.prepare_hist()
za.prepare_hist()

create_double_histogram(z.nombre,  za.nombre,"France et Outre-Mer", "Nombre de communes par pourcentage d'abstention",'Nombre de communes','% Abs/Ins',  "Nombre de bureaux de vote par pourcentage d'abstention", 'Nombre de bureaux de vote', '% Abs/Ins')

create_double_histogram(z.inscrits,  za.inscrits,"France et Outre-Mer", "Nombre d'inscrits dans les communes par pourcentage d'abstention","Nombre d'inscrits",'% Abs/Ins',  "Nombre d'inscrits dans les bureaux de vote par pourcentage d'abstention", "Nombre d'inscrits", '% Abs/Ins')

create_double_histogram(z.asbten,  za.asbten,"France et Outre-Mer", "Nombre d'abstentions dans les communes par pourcentage d'abstention","Nombre d'abstentions",'% Abs/Ins',  "Nombre d'abstentions dans les bureaux de vote par pourcentage d'abstention", "Nombre d'abstentions", '% Abs/Ins')



word_list = ['Haute-Corse', 'Corse-du-Sud', 'La Réunion','Nouvelle-Calédonie','Guadeloupe','Martinique','Guyane','Mayotte','Saint-Martin/Saint-Barthélemy','Polynésie française','Français établis hors de France']
communes_metro = communes
bureaux_metro = bureaux

for word in word_list:
    communes_metro = communes_metro[~communes_metro["Libellé du département"].str.contains(word)] #string does not contain
    bureaux_metro = bureaux_metro[~bureaux_metro["Libellé du département"].str.contains(word)]


b = hist(communes_metro)
ba = hist(bureaux_metro)

b.prepare_hist()
ba.prepare_hist()

create_double_histogram(b.nombre,  ba.nombre,"France Métropolitaine", "Nombre de communes par pourcentage d'abstention",'Nombre de communes','% Abs/Ins',  "Nombre de bureaux de vote par pourcentage d'abstention", 'Nombre de bureaux de vote', '% Abs/Ins')

create_double_histogram(b.inscrits,  ba.inscrits, "France Métropolitaine","Nombre d'inscrits dans les communes par pourcentage d'abstention","Nombre d'inscrits",'% Abs/Ins',  "Nombre d'inscrits dans les bureaux de vote par pourcentage d'abstention", "Nombre d'inscrits", '% Abs/Ins')

create_double_histogram(b.asbten,  ba.asbten,"France Métropolitaine", "Nombre d'abstentions dans les communes par pourcentage d'abstention","Nombre d'abstentions",'% Abs/Ins',  "Nombre d'abstentions dans les bureaux de vote par pourcentage d'abstention", "Nombre d'abstentions", '% Abs/Ins')


# fig4 = plt.figure(figsize=(14,10))
# plt.bar(range(100), b.asbten)
# plt.title("Nombre d'abstentions dans les communes par pourcentage d'abstention en France Métropolitaine")
# plt.ylabel("Nombre d'abstenstions")
# plt.xlabel('% Abs/Ins')
#
# pp.savefig(fig4)
# plt.close()

pp.close()
