#!/usr/bin/python3
import numpy as np
import pandas as pd

import  random
import matplotlib.pyplot as plt


import time
import datetime
from matplotlib.backends.backend_pdf import PdfPages
'''
Nous souhaitons générer un fichier pdf qui récapitule une paire de graphiques pour chaque département de France et d'Outre Mer. Pour chaque paire, nous observerons l'ordre croissant des pourcentages d'abstentions sur le département.

'''

################### fichier pdf ##############################
out = ' Graphiques communes'+str(datetime.datetime.now())+'.pdf'
pp = PdfPages(out)
firstPage = plt.figure(figsize=(11.69,8.27))
firstPage.clf()
txt = "Poucentage d'abstension \n Nous souhaitons avoir une vue d'ensemble sur l'information supplémentaire qu'offre \n la précision jusqu'aux bureaux de votes, \n par rapport celle sur les communes entière"
firstPage.text(0.5,0.5,txt, transform=firstPage.transFigure, size=12, ha="center")
pp.savefig()


communes = pd.read_csv('../data/raw/Presid_2017_Communes_Tour_1.csv')
bureaux = pd.read_table("../data/raw/PR17_BVot_T1_FE (copy).txt", encoding = "ISO-8859-1", sep =';', decimal =',')

#fig_list = list()
#liste_communes = plt.figure()
for i in communes ['Code du département'].unique():
    #fig_list.append(plt.figure())
    print( ' commune vaut '+ str(i))
    plt.figure(figsize=(15,10))

    plt.subplot(1,2,1)
    comm = communes [communes ['Code du département'].apply(lambda x : str(x)) == str(i)]
    plt.bar(range(0, comm.shape[0]), comm['% Abs/Ins'].sort_values())
    plt.title('Par commune:    ' + comm['Libellé du département'].iloc[0])
    plt.xlabel('communes')
    plt.ylabel('% Abs/Ins')

    plt.subplot(1, 2, 2)


    burr = bureaux[bureaux['Code du département'].apply(lambda x : str(x)) == str(i)]
    plt.bar(range(0, burr.shape[0]), burr['% Abs/Ins'].sort_values())
    plt.title('Par bureaux de vote:    ' + burr['Libellé du département'].iloc[0])
    plt.xlabel('bureaux de vote')
    plt.ylabel('% Abs/Ins')
    #pp.savefig(fig_list[i-1])
    pp.savefig()
    plt.close()
    

    #plt.show()
#pp.savefig(liste_communes)
pp.close()
