# Prediksi Harga Rumah Jabodetabek 🏠

Proyek ini adalah dashboard interaktif untuk **memprediksi harga rumah di Jabodetabek** menggunakan metode **Regresi Linier Berganda**.  
Aplikasi ini dibuat dengan Python dan Streamlit sehingga mudah digunakan secara online atau lokal.

---

## 📊 Fitur Input

Pengguna dapat memasukkan beberapa data properti sebagai input:

- Luas Tanah (m²)  
- Luas Bangunan (m²)  
- Jumlah Kamar Tidur  
- Jumlah Kamar Mandi  
- Jumlah Carport  
- Jumlah Lantai  
- Usia Bangunan (tahun)

---

## 🚀 Cara Menjalankan Aplikasi

1️⃣ **Clone Repo**

```bash
git https://github.com/iqblmlnf/FP_BDPA2025.git
cd FP_BDPA2025
```

2️⃣ **Install Library yang Dibutuhkan**

```bash
pip install -r requirements.txt
```

3️⃣ **Jalankan Dashboard**

```bash
streamlit run dashboard_prediksi_rumah.py
```

---

## 📈 Evaluasi Model

| Metode                  | MAE (Rp)        | RMSE (Rp)       | R²   |
|------------------------|-----------------|-----------------|-------|
| Regresi Linier Berganda | 1.789.435.978   | 4.046.591.330   | 0.70  |

---

## 👨‍💻 Anggota Kelompok

- Mu'ammar Nibros - 23.11.5465  
- Muhammad Nur Syafii - 23.11.5451  
- Iqbal Maulana Fajar - 23.11.5467  
- Nur Ikhsan Cleviriadi - 23.11.5487

---

## 🔧 Tools yang Digunakan

- Python  
- Streamlit  
- Scikit-Learn  
- Pandas  
- Numpy  
- Matplotlib
