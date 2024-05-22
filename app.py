import pandas as pd
import streamlit as st
from PIL import Image
from komputasi import data_summary, MBA

# Set layout halaman
st.set_page_config(layout="wide")

# Tampilkan navbar
st.markdown(
    """
    <style>
    .navbar {
        background-color: #333;
        overflow: hidden;
    }

    .navbar a {
        float: left;
        display: block;
        color: #f2f2f2;
        text-align: center;
        padding: 14px 20px;
        text-decoration: none;
        font-size: 17px;
    }

    .navbar a:hover {
        background-color: #ddd;
        color: black;
    }

    .navbar a.active {
        background-color: #04AA6D;
        color: white;
    }
    </style>
    """
    , unsafe_allow_html=True
)

st.markdown(
    """
    <div class="navbar">
        <a class="active" href="#" onclick="showPage('Home')">Home</a>
    </div>
    <script>
    function showPage(page) {
        window.location.hash = page;
        window.location.reload();
    }
    </script>
    """
    , unsafe_allow_html=True
)

# Fungsi untuk menampilkan konten halaman berdasarkan pilihan navbar
def show_page(page):
    if page == "Home":
        st.write("Selamat datang di Aplikasi Analisis Toko Tanaman Hias dengan Metode Apriori.")

# Mendapatkan halaman yang dipilih
page = st.session_state.get("page", "Home")

# Memanggil fungsi untuk menampilkan konten halaman
show_page(page)

# CSS styling untuk menambahkan efek frame dan warna
st.markdown(
    """
    <style>
    .frame {
        padding: 20px;
        border-radius: 10px;
        background-color: #d9ead3; /* Warna hijau muda */
        box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.1);
    }
    .title-text {
        color: #2e7166; /* Warna hijau tua */
        font-size: 24px;
        text-align: center;
        margin-bottom: 20px;
    }
    .content {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px 0 rgba(0, 0, 0, 0.1);
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 10px 0;
    }

    .footer-content {
        display: flex;
        justify-content: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Judul halaman
st.markdown('<h1 class="title-text">Analisis Toko Tanaman Hias dengan Metode Apriori</h1>', unsafe_allow_html=True)

# Menampilkan gambar header di tengah halaman
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    header_image = Image.open('images/header_image.png')
    st.image(header_image, use_column_width=True)

# Deskripsi dan tautan ke dataset
st.markdown('<div class="frame content">', unsafe_allow_html=True)
st.markdown('<h2>Unggah Dataset Anda</h2>', unsafe_allow_html=True)
st.markdown('<p>Mohon unggah dataset penjualan tanaman dalam format CSV.</p>', unsafe_allow_html=True)
st.markdown('<p>Contoh format dataset: ID, DATE, ITEM</p>', unsafe_allow_html=True)
st.markdown('<p><a href="https://www.kaggle.com/datasets/hanageofani/tanaman-toko" target="_blank">Kaggle Toko Tanaman</a></p>', unsafe_allow_html=True)

# Unggah dataset
dataset_file = st.file_uploader("Pilih file CSV", type=['csv'])

# Memproses dataset jika diunggah
if dataset_file is not None:
        try:
            # Membaca dataset
            df = pd.read_csv(dataset_file)

            # Memeriksa dataset kosong
            if df.empty:
                st.warning("Dataset kosong. Mohon unggah dataset yang valid.")
            else:
                # Memproses data
                pembeli, tanggal, produk = df.columns[0], df.columns[1], df.columns[2]
                df = data_summary(df, pembeli, tanggal, produk)

                # Analisis menggunakan Apriori
                MBA(df, pembeli, produk)

        except Exception as e:
            st.error(f"Terjadi kesalahan saat memproses dataset: {str(e)}")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(
    """
    <div class="footer">
        <div class="footer-content">
            © 2024 Aplikasi Analisis Data Penjualan dengan Apriori. All rights reserved.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
