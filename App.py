import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
df = pd.read_csv('tb_cases1.csv')
india_map = gpd.read_file("India_State_Boundary.shp")  # Load the shapefile
india_map = india_map.to_crs(epsg=4326)

# Ensure state names match between datasets
india_map = india_map.rename(columns={"Name": "State"})

# Merge geospatial data with TB data
merged_data = india_map.merge(df, on="State", how="left")
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
merged_data.plot(column="TB_Cases", cmap="Reds", linewidth=0.8, edgecolor="black", legend=True, ax=ax)
ax.set_title("State-wise TB Cases in India", fontsize=14)
plt.show()
