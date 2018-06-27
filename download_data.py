import geopandas as gpd
import osmnx as ox
import pandas as pd
import os

import matplotlib.pyplot as plt
matplotlib inline


partidos = pd.read_csv('partidos.csv',sep=';',header=None)[0]

for partido in partidos:
    try:
        G = ox.graph_from_place(partido, network_type='drive_service')
        partido = partido.split(',')[0]
        ox.save_load.save_graph_shapefile(G, filename=partido, folder='shapes', encoding='utf-8')
    except:
        print(partido)

callejero = pd.DataFrame()
esquinero = pd.DataFrame()

for partido in os.listdir('shapes'):
    calles = gpd.read_file('shapes/'+partido+'/edges/edges.shp')
    calles['partido'] = partido
    esquinas = gpd.read_file('shapes/'+partido+'/nodes/nodes.shp')
    esquinas['partido'] = partido
    callejero = callejero.append(calles)
    esquinero = esquinero.append(esquinas)

esquinero.to_file('esquinero')
callejero.to_file('callejero')
