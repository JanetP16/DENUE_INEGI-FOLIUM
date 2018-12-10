
# coding: utf-8

# In[1]:

import folium
import pandas as pd


# In[2]:

#file = pd.read_csv('minas.csv', sep=';')
file = pd.read_csv('denue_inegi_21_.csv', sep=',',header=0)
file=file.head(5)
file


# In[3]:

for index, row in file.iterrows():
    print ([row.longitud, row.latitud], row.nom_estab.decode('"windows-1252"', 'ignore'))


# In[7]:

m = folium.Map(location=[19.2499700, -103.7271400], zoom_start=5)


# In[8]:

for index, row in file.iterrows():
    print(row.latitud, row.longitud)
    folium.Marker(location=[row.latitud, row.longitud] ,popup=row.nom_estab.decode('"windows-1252"', 'ignore')             ).add_to(m)


# In[9]:

m


# In[ ]:



