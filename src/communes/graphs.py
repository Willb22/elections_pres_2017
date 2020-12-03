#!/usr/bin/python3
import numpy as np
import pandas as pd

import  random
import matplotlib.pyplot as plt
import overpass
#api = overpass.API()
import re
from string import punctuation
import time
import datetime
from matplotlib.backends.backend_pdf import PdfPages

################### fichier pdf ##############################
pp = PdfPages(' Graphiques communes.pdf')
firstPage = plt.figure(figsize=(11.69,8.27))
firstPage.clf()
txt = "Poucentage d'abstension par commune"
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=12, ha="center")
pp.savefig()


data = pd.read_csv('../../data/raw/Presid_2017_Communes_Tour_1.csv')
fig_list = list()
#liste_communes = plt.figure()
for i in range(1,14):
    fig_list.append(plt.figure())
    comm = data[data['Code du département'] == str(i)]
    plt.bar(range(0, comm.shape[0]), comm['% Abs/Ins'].sort_values())
    plt.title(comm['Libellé du département'].iloc[0])
    plt.xlabel('communes')
    plt.ylabel('% Abs/Ins')
    pp.savefig(fig_list[i-1])
    

    #plt.show()
#pp.savefig(liste_communes)
pp.close()
