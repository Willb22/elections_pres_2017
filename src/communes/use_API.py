import pandas as pd
import numpy as np
import  random
import matplotlib.pyplot as plt
import overpass
api = overpass.API()
import re
from string import punctuation
import time
import datetime


data = pd.read_csv('../../data/raw/Presid_2017_Communes_Tour_1.csv')
#print(data.shape)


api = overpass.API()
api = overpass.API(endpoint="https://overpass.myserver/interpreter")
api = overpass.API(timeout=15)

response = api.get('node["name"="L\'Abergement-de-Varey"]', responseformat="json") # Eg of how the API works
response = api.get('node["name"="This"]', responseformat="json")

def sp(stri):
    result = stri
    alist = list()

    if "'" in stri:
        ind = [m.start() for m in re.finditer("'", stri)]
        if len(ind) > 1:

            if ind[0] == 0:
                for i in ind[:len(ind)-1]:
                    alist.append(stri[ind[i]:ind[i + 1]])
                alist.append(stri[ind[len(ind)-1]:])
            else:
                alist.append(stri[:ind[0]])
                for i in ind[:len(ind)-1]:
                    alist.append(stri[ind[i-1]:ind[i]])
                alist.append(stri[ind[len(ind)-1]:])

            result = alist
        else:
            if stri.index("'") > 0:

                result = [stri[:stri.index("'")], stri[stri.index("'"):]]


    return result

#print(sp("l'pp'er"))
#print(sp("ff"))



def slash(stri):
    if type(stri) == list:

        newword = ""
        for i in range(0, len(stri)):
            if "'" in stri[i]:
                #print(type(stri[i]))
                word = stri[i]
                #temp = "".join([ punctuation[23], word])
                stri[i] = punctuation[23] + word #insert backslash before syllable
                #stri[i] =temp
                newword = newword+ stri[i]
            else:
                newword = newword + stri[i]
        stri = newword

    else:
        if "'" in stri:
            temp = "".join(["\\", stri])
            stri = temp

    return stri

tot = slash(sp(data['Libellé de la commune'][1]))
print(tot)


ticks = time.time()
response = api.get(''.join(['node["name"=', '"', tot, '"', ']' ]), responseformat="json")
secs = time.time()-ticks
print(response)


lati=list()
longi = list()
tick = time.time()
last_entry = 0
for i in range(last_entry, len(data['Libellé de la commune'])):
    tot = slash(sp(data['Libellé de la commune'][i]))
    response = api.get(''.join(['node["name"=', '"', tot, '"', ']' ]), responseformat="json")
    temps = time.time()-tick
    print(" round "+ str(i)+" seconds "+ str(temps))
    if response['elements']==[]:
        lati.append('NaN')
        longi.append('NaN')
    else:
        lati.append(response['elements'][0]['lat'])
        longi.append(response['elements'][0]['lon'])

df= pd.DataFrame()
#df['commune'] = data['Libellé de la commune']
df['latitude'] = pd.Series(lati)
df['longitude'] = pd.Series(longi)

file_name = "coord_communes" + str(datetime.datetime.now()) +".csv"
#df.to_csv("coord_communes.csv", sep= '\t')
df.to_csv(file_name)