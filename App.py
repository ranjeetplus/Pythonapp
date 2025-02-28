import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import requests


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
st.write("_______________________________________________________________________________________")
st.title("Air Quality - API")

# OpenWeather API Key (Replace with your own key)
API_KEY = "6f9f0ef264f8c6837bc24086a584773e"
# List of Indian State Capitals with their latitudes and longitudes
capital_cities = {
    "New Delhi": (28.6139, 77.2090),
    "Mumbai": (19.0760, 72.8777),
    "Kolkata": (22.5726, 88.3639),
    "Chennai": (13.0827, 80.2707),
    "Bengaluru": (12.9716, 77.5946),
    "Hyderabad": (17.3850, 78.4867),
    "Ahmedabad": (23.0225, 72.5714),
    "Jaipur": (26.9124, 75.7873),
    "Lucknow": (26.8467, 80.9462),
    "Bhopal": (23.2599, 77.4126),
    "Patna": (25.5941, 85.1376),
    "Thiruvananthapuram": (8.5241, 76.9366),
    "Bhubaneswar": (20.2961, 85.8245),
    "Ranchi": (23.3441, 85.3096),
    "Guwahati": (26.1445, 91.7362),
    "Shimla": (31.1048, 77.1734),
    "Dehradun": (30.3165, 78.0322),
    "Shillong": (25.5788, 91.8933),
    "Aizawl": (23.7271, 92.7176),
    "Gangtok": (27.3314, 88.6138),
    "Agartala": (23.8315, 91.2868),
    "Imphal": (24.8170, 93.9368),
}

# Store results
data_list = []

# Fetch air quality data for each city
for city, (lat, lon) in capital_cities.items():
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_KEY}"
   
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data["list"]:
            aqi = data["list"][0]["main"]["aqi"]
            pm2_5 = data["list"][0]["components"]["pm2_5"]
            pm10 = data["list"][0]["components"]["pm10"]
            no2 = data["list"][0]["components"]["no2"]
            so2 = data["list"][0]["components"]["so2"]
            co = data["list"][0]["components"]["co"]
            o3 = data["list"][0]["components"]["o3"]

            data_list.append([city, aqi, pm2_5, pm10, no2, so2, co, o3])
        else:
            print("Error:", response.status_code)
            data_list.append([city, "No Data", "No Data", "No Data", "No Data", "No Data", "No Data", "No Data"])
    else:
        print("Error:", response.status_code)
        data_list.append([city, "API Error", "API Error", "API Error", "API Error", "API Error", "API Error", "API Error"])

# Create a DataFrame
df = pd.DataFrame(data_list, columns=["City", "AQI", "PM2.5", "PM10", "NO2", "SO2", "CO", "O3"])

# Display the DataFrame
st.write("## Air Quality of Capital Cities ", df)


