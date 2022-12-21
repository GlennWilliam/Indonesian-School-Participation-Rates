import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd

path = './Angka Partisipasi Sekolah.xlsx'
df = pd.read_excel(path)
display(df.head())

path = r'C:\Users\USER\gadm36_IDN_2.json'
df_geo = gpd.read_file(path)
display(df_geo.head())

df_join = df_geo.merge(df, how='inner', left_on="NAME_1", right_on="Province")
df_join = df_join[['Province','7-12', '13-15', '16-18', '19-24','geometry']]
df_join.head()

df_geo.plot()

# set a variable that will call whatever column we want to visualise on the map
values = '19-24'
# set the value range for the choropleth
vmin, vmax = 0,100
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
ax.axis('off')
# add a title
title = 'School Participations Rate for Age {}'.format(values)
ax.set_title(title, fontdict={'fontsize': '25', 'fontweight' : '3'})
# create an annotation for the data source
ax.annotate('Source: Badan Pusat Statistik Indonesia',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12 ,color='#555555')
# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# add the colorbar to the figure
cbar = fig.colorbar(sm)
# create map
df_join.plot(column=values, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8',norm=plt.Normalize(vmin=vmin, vmax=vmax))

def make_plot(geo_df,values):
    # set a variable that will call whatever column we want to visualise on the map
    values = geo_df.columns[values]
# set the value range for the choropleth
    vmin, vmax = 0,100
# create figure and axes for Matplotlib
    fig, ax = plt.subplots(1, figsize=(30, 10))
# remove the axis
    ax.axis('off')
# add a title
    title = 'School Participations Rate for Age {}'.format(values)
    ax.set_title(title, fontdict={'fontsize': '25', 'fontweight' : '3'})
# create an annotation for the data source
    ax.annotate('Source: Badan Pusat Statistik Indonesia',xy=(0.1, .08),  xycoords='figure fraction', horizontalalignment='left', verticalalignment='top', fontsize=12 ,color='#555555')
# Create colorbar as a legend
    sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# add the colorbar to the figure
    cbar = fig.colorbar(sm)
# create map
    geo_df.plot(column=values, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8',norm=plt.Normalize(vmin=vmin, vmax=vmax))
    
for i in range(1,5):
    make_plot(df_join,i)
