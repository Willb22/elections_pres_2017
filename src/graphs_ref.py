#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime

def plot_ordered_bar(df, colname, xlabel=None, ylabel=None, title=None):
    plt.bar(x=range(0, len(df.index)), height=df[colname].sort_values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

def add_title_page(pp, text, figsize):
    """Add a title page to pdf.
    
    Args:
        pp (matplotlib.backends.backend_pdf.PdfPages): A PdfPages object.
        figsize (tuple): The (width, height) of the page.
    """
    plt.figure(figsize=figsize).text(
        x=0.5, y=0.5, s=text,
        size=12, ha="center"
    )
    pp.savefig()
    plt.close()

def add_body_page(pp, departement, figsize):
    """Add two subplots to pdf, filtering on departement.
    
    Args:
        pp (matplotlib.backends.backend_pdf.PdfPages): A PdfPages object.
        departement (str): The code of the departement: "01", "1", "33".
        figsize (tuple): The (width, height) of the page.
    """
    plt.figure(figsize=figsize)

    plt.subplot(1, 2, 1) 
    comm = communes[communes['Code du département'].astype(str) == departement]
    plot_ordered_bar(
        df=comm,
        colname='% Abs/Ins',
        xlabel="communes",
        ylabel='% Abs/Ins',
        title='Par commune: {nomDepartement}'.format(
            nomDepartement=comm['Libellé du département'].iloc[0])
    )

    plt.subplot(1, 2, 2)
    burr = bureaux[bureaux['Code du département'].astype(str) == departement]
    plot_ordered_bar(
        df=burr,
        colname='% Abs/Ins',
        xlabel="bureaux de vote",
        ylabel="% Abs/Ins",
        title='Par bureau de vote: {nomDepartement}'.format(
            nomDepartement=burr['Libellé du département'].iloc[0])
    )
    
    pp.savefig()
    plt.close()


communes = pd.read_csv('./data/raw/Presid_2017_Communes_Tour_1.csv')
bureaux = pd.read_table(
    "./data/raw/PR17_BVot_T1_FE (copy).txt",
    encoding="ISO-8859-1",
    sep=';',
    decimal=','
)

with PdfPages('communes_{timestamp}.pdf'.format(timestamp=str(datetime.now()))) as pp:
    add_title_page(pp, "Pourcentage d'abstension", figsize=(11.69, 8.27))

    departements_codes = communes["Code du département"].unique().astype(str)
    for dep in departements_codes:
        print("Département {0}".format(dep))
        add_body_page(pp, departement=dep, figsize=(15, 10))
