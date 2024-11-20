# Streamlit application for "Paris - Green City" - Redesigned Layout with Two Versions
import streamlit as st
import polars as pl
import json
import plotly.express as px
import folium
from streamlit_folium import st_folium

# Load data
@st.cache_data
def load_data():
    # Load CSV data
    locations_df = pl.read_csv('./data_daria/paris_green_city_locations.csv')
    # Load JSON data
    with open('./data_daria/paris_air_quality_and_green_zones.json') as f:
        air_quality_data = json.load(f)
    return locations_df, air_quality_data

# Load the data
locations_df, air_quality_data = load_data()

# Convert Polars DataFrame to Pandas for compatibility
locations_pd = locations_df.to_pandas()

######################
# Version 1 Layout
######################
st.title("Paris - Green City (Version 1)")

# Sidebar for user filters and inputs (Version 1)
st.sidebar.markdown("Filters and Selections <span style='color:orange;'>(to be developing)</span>", unsafe_allow_html=True)
region_filter = st.sidebar.selectbox("Select Region", ["All", "Montmartre", "Marais", "Saint-Germain-des-Prés", "Bastille", "La Villette"])
transport_filter = st.sidebar.multiselect("Select Transport Options", ["Bike Paths", "Electric Vehicle Charging Stations", "Bus Stops", "Bike Stands"])

# Version 1 Tabs: Map, Air Quality, Useful Contacts
tab1, tab2, tab3 = st.tabs(["Map View", "Air Quality & Green Zones", "Useful Contacts"])

# Tab 1: Map View of Eco-friendly Locations
with tab1:
    st.header("Eco-friendly Locations in Paris")
    # Folium map for custom visualization with arrondissement boundaries
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    # Adding markers for locations
    for _, row in locations_pd.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['location_name']} ({row['type']})\nRating: {row['rating']}\nHours: {row['opening_hours']}",
            icon=folium.Icon(color='green' if row['type'] == 'Park' else 'blue')
        ).add_to(m)
    # Displaying the Folium map in Streamlit
    st_folium(m, width=700, height=500, key='map_v1')

# Tab 2: Air Quality and Green Zones Overview
with tab2:
    st.header("Air Quality and Green Zones by Area")
    # Extract air quality and green zones data from JSON
    air_quality_df = pl.DataFrame(air_quality_data['areas']).to_pandas()
    # Displaying the data as a dataframe
    st.dataframe(air_quality_df)
    # Bar chart for air quality index per area
    st.subheader("Air Quality Index by Area")
    fig_aqi = px.bar(
        air_quality_df,
        x="area_name",
        y="air_quality_index",
        color="air_quality_index",
        labels={"air_quality_index": "Air Quality Index"},
        title="Air Quality Index per Area"
    )
    st.plotly_chart(fig_aqi)

# Tab 3: Useful Contacts for Eco-friendly Services
with tab3:
    st.header("Useful Contacts for Eco-friendly Services: coming soon")
    st.markdown("- Eco-friendly Boulangeries: Contact details <span style='color:orange;'>(to be developing)</span>", unsafe_allow_html=True)
    st.markdown("- Fitness Clubs focusing on sustainability: Contact details <span style='color:orange;'>(to be developing)</span>", unsafe_allow_html=True)
    st.markdown("- Electric Vehicle Charging Points: Locations <span style='color:orange;'>(to be developing)</span>", unsafe_allow_html=True)

# Modular Approach: Adding a placeholder for additional modules
st.sidebar.markdown("Future Features <span style='color:orange;'>(to be developing)</span>", unsafe_allow_html=True)
st.sidebar.markdown("- Comparative Analysis Module", unsafe_allow_html=True)
st.sidebar.markdown("- User Ratings Module", unsafe_allow_html=True)
st.sidebar.markdown("- Live Data Integration", unsafe_allow_html=True)

######################
# Version 2 Layout
######################
st.title("_______________________________")
st.title("Paris - Green City (Version 2)")

# Sidebar for user filters and inputs (Version 2)
st.sidebar.markdown("Interactive Modules <span style='color:orange;'>(to be developing)</span>", unsafe_allow_html=True)
activity_filter = st.sidebar.radio("Select Activity Type", ["Cycling Routes", "Parks & Gardens", "Organic Markets"])
quality_filter = st.sidebar.slider("Filter by Air Quality Index", 0, 100, (30, 70))

# Version 2 Pages: Map, Comparison Dashboard, Sustainability Highlights
page = st.selectbox("Select Page", ["Map of Green Locations", "Comparison Dashboard", "Sustainability Highlights"])

# Page 1: Map of Green Locations
if page == "Map of Green Locations":
    st.header("Map of Green Locations in Paris")
    # Folium map for arrondissement-level visualization
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)
    # Adding markers for locations
    for _, row in locations_pd.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"{row['location_name']} ({row['type']})\nRating: {row['rating']}\nHours: {row['opening_hours']}",
            icon=folium.Icon(color='green' if row['type'] == 'Park' else 'blue')
        ).add_to(m)
    # Displaying the Folium map in Streamlit
    st_folium(m, width=700, height=500, key='map_v2')

# Page 2: Comparison Dashboard
elif page == "Comparison Dashboard":
    st.header("Comparison of Air Quality and Green Features by Area")
    # Extract air quality and green zones data from JSON
    air_quality_df = pl.DataFrame(air_quality_data['areas']).to_pandas()
    # Displaying comparison metrics as charts
    st.subheader("Green Zones and Electric Vehicle Charging Stations")
    fig_compare = px.bar(
        air_quality_df,
        x="area_name",
        y=["green_zones", "electric_vehicle_charging_stations"],
        barmode="group",
        title="Green Zones and Charging Stations by Area"
    )
    st.plotly_chart(fig_compare)

# Page 3: Sustainability Highlights
elif page == "Sustainability Highlights":
    st.header("Sustainability Highlights of Different Areas")
    for area in air_quality_data['areas']:
        st.subheader(f"{area['area_name']}")
        st.markdown(f"Air Quality Index: {area['air_quality_index']}")
        st.markdown(f"Number of Green Zones: {area['green_zones']}")
        st.markdown(f"Renewable Energy Use: {area['renewable_energy_use_percentage']}%")
        st.markdown(f"Community Garden Participation: {area['community_garden_participation']} people")
