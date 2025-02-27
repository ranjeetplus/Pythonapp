import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt

st.title("Python Application - Project")
st.write("Data Analysis [Pandas, Mathplotlib, GeoPandas & SeaBorn]")
st.write("_______________________________________________________________________________________")

# Title of the Streamlit App
st.write("State-wise TB Cases in India")

# Load TB Data
df = pd.read_csv('tb_cases1.csv')


# Load India Map Shapefile
india_map = gpd.read_file("India_State_Boundary.shp")  # Load the shapefile
india_map = india_map.to_crs(epsg=4326)
india_map = india_map.rename(columns={"Name": "State"})  # Ensure state names match

# Merge geospatial data with TB data
merged_data = india_map.merge(df, on="State", how="left")

# Plot Map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
merged_data.plot(column="TB_Cases", cmap="Reds", linewidth=0.8, edgecolor="black", legend=True, ax=ax)
ax.set_title("State-wise TB Cases in India", fontsize=14)

# Display plot in Streamlit
st.pyplot(fig)

st.write("## TB Cases Data", df)  # Display data in Streamlit
