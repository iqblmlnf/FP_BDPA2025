import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Judul Dashboard
st.title("Prediksi Harga Rumah Jabodetabek 🏠")
st.subheader("Final Project Big Data - Regresi Linier Berganda")

st.markdown("""
### Anggota Kelompok:
- Mu'ammar Nibros - 23.11.5465  
- Muhammad Nur Syafii - 23.11.5451  
- Iqbal Maulana Fajar - 23.11.5467  
- Nur Ikhsan Cleviriadi - 23.11.5487
""")

st.write("---")

# Sidebar untuk input data
st.sidebar.header("Input Data Rumah")

land_size = st.sidebar.slider("Luas Tanah (m²)", 10, 2000, 100)
building_size = st.sidebar.slider("Luas Bangunan (m²)", 10, 2000, 100)
bedrooms = st.sidebar.slider("Jumlah Kamar Tidur", 1, 10, 3)
bathrooms = st.sidebar.slider("Jumlah Kamar Mandi", 1, 10, 2)
carports = st.sidebar.slider("Jumlah Carport", 0, 5, 1)
floors = st.sidebar.slider("Jumlah Lantai", 1, 5, 2)
building_age = st.sidebar.slider("Usia Bangunan (tahun)", 0, 100, 5)

# Tampilkan data yang diinput user
st.header("Data yang Anda Masukkan")
input_data = {
    'Luas Tanah (m²)': land_size,
    'Luas Bangunan (m²)': building_size,
    'Kamar Tidur': bedrooms,
    'Kamar Mandi': bathrooms,
    'Carport': carports,
    'Lantai': floors,
    'Usia Bangunan (Tahun)': building_age
}
st.write(pd.DataFrame([input_data]))

st.write("---")

# Prediksi Harga
st.header("Hasil Prediksi Harga Rumah")

# Dummy model dengan koefisien dari eksperimen
model = LinearRegression()
model.coef_ = np.array([8.256103e+06, 2.110150e+07, -8.750051e+08, 1.866533e+08,
                        2.503562e+08, 4.865953e+08, 2.454835e+05])
model.intercept_ = -3.55183887e+08

# Proses prediksi
X_input = np.array([[land_size, building_size, bedrooms, bathrooms, carports, floors, building_age]])
predicted_price = model.predict(X_input)[0]

# Output prediksi dengan format ribuan
st.success(f"Perkiraan Harga Rumah Anda: **Rp {predicted_price:,.0f}**")

# Penjelasan hasil
st.info("""
Prediksi ini berdasarkan model regresi linier berganda. Hasil bisa berbeda dengan harga pasar sebenarnya karena faktor seperti lokasi spesifik, kondisi lingkungan, atau fasilitas sekitar tidak dipertimbangkan di model ini.
""")

# Visualisasi prediksi
st.header("Visualisasi Harga Prediksi")

labels = ['Harga Prediksi', 'Batas Atas (10% lebih mahal)', 'Batas Bawah (10% lebih murah)']
values = [predicted_price, predicted_price * 1.1, predicted_price * 0.9]

fig, ax = plt.subplots()
bars = ax.bar(labels, values, color=['#4CAF50', '#FFC107', '#FF5722'])
ax.set_ylabel("Harga Rumah (Rp)")
plt.xticks(rotation=15)
st.pyplot(fig)

# Footer
st.write("---")
st.caption("© Kelompok Prediksi Harga Rumah 2025 - Universitas Amikom Yogyakarta")
