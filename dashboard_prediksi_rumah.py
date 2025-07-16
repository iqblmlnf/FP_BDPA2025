import streamlit as st
import numpy as np
from sklearn.linear_model import LinearRegression

# Judul Dashboard
st.title("Dashboard Prediksi Harga Rumah Jabodetabek")
st.subheader("Kelompok Prediksi Harga Rumah")

# Tampilkan nama anggota kelompok
st.markdown("""
**Anggota Kelompok:**

1. Mu'ammar Nibros - 23.11.5465  
2. Muhammad Nur Syafii - 23.11.5451  
3. Iqbal Maulana Fajar - 23.11.5467  
4. Nur Ikhsan Cleviriadi - 23.11.5487
""")

st.write("---")  # Garis pemisah

# Input user
st.header("Input Data Rumah")

land_size = st.number_input("Luas Tanah (m2)", min_value=10, max_value=2000, value=100)
building_size = st.number_input("Luas Bangunan (m2)", min_value=10, max_value=2000, value=100)
bedrooms = st.number_input("Jumlah Kamar Tidur", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Jumlah Kamar Mandi", min_value=1, max_value=10, value=2)
carports = st.number_input("Jumlah Carport", min_value=0, max_value=5, value=1)
floors = st.number_input("Jumlah Lantai", min_value=1, max_value=5, value=2)
building_age = st.number_input("Usia Bangunan (tahun)", min_value=0, max_value=100, value=5)

# Prediksi harga rumah
st.header("Hasil Prediksi")

# Model dummy (koefisien diambil dari hasil eksperimen)
model = LinearRegression()
model.coef_ = np.array([8.256103e+06, 2.110150e+07, -8.750051e+08, 1.866533e+08, 
                        2.503562e+08, 4.865953e+08, 2.454835e+05])
model.intercept_ = -3.55183887e+08

# Data input
input_data = np.array([[land_size, building_size, bedrooms, bathrooms, carports, floors, building_age]])

# Prediksi
predicted_price = model.predict(input_data)[0]

# Tampilkan hasil
st.success(f"Perkiraan Harga Rumah: Rp {predicted_price:,.0f}")
