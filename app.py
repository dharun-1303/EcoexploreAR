import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(page_title="Plant Anatomy AR & VR", page_icon="\U0001F331", layout="wide")

# Title and Banner
st.image("plant_banner.jpg", use_container_width=True)
st.title("🌿 Learning Plant Anatomy Through AR & VR")
st.subheader("Explore the inner structures of plants, cross-breeding, and diverse biomes through immersive AR and VR experiences.")

# About Us Section
st.header("About Us")
st.write("We are developing interactive AR and VR models to help users understand plant anatomy, cross-breeding techniques, and various ecosystems.")
st.write("Our goal is to make learning about plants more engaging through advanced visualization technologies.")

# AR Models Section
st.header("🌱 AR Models of Plants")
st.write("Our AR models allow you to explore the internal structures of plants in detail, including roots, stems, leaves, and reproductive organs.")
st.image("ar_model_example.jpg", caption="AR Model of a Plant's Inner Structure", use_container_width=True)

# Cross-Breeding and Pollination
st.header("🌾 New Plant Technologies")
st.write("We explain advanced plant breeding techniques, including cross-breeding and pollination processes, using immersive visuals.")
st.write("Example: Cross-breeding between a tomato and a currant tomato to produce new varieties with better traits.")
st.image("cross_breeding_example.jpg", caption="Cross-Breeding Process", use_container_width=True)

# Biomes Section
st.header("🌍 Exploring Biomes")
st.write("Discover different biomes such as Rainforests and Deserts, and learn how plants adapt to their environments.")
col1, col2 = st.columns(2)
with col1:
    st.subheader("🌧️ Rainforest Biome")
    st.image("rainforest_biome.jpg", use_container_width=True)
    st.write("Experience the lush greenery and diverse plant species of the rainforest through VR.")
with col2:
    st.subheader("🏜️ Desert Biome")
    st.image("desert_biome.jpg", use_container_width=True)
    st.write("Explore how cacti and other desert plants survive in extreme conditions.")

# Footer
st.write("---")
st.write("© 2025 Plant Anatomy AR & VR | Designed to revolutionize plant education.")
