import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Membaca dataset
df = pd.read_csv("Shunyi_clean_data.csv")

# Fungsi untuk membuat grafik rata-rata PM berdasarkan tahun
def plot_avg_pm_year(pm_column):
    rata2_pm_per_tahun = df.groupby('year')[pm_column].mean()
    plt.figure(figsize=(8, 6))
    plt.plot(rata2_pm_per_tahun.index, rata2_pm_per_tahun.values, marker='o', linestyle='-')
    plt.title(f'Rata-rata {pm_column} berdasarkan Tahun')
    plt.xlabel('Tahun')
    plt.ylabel(f'Rata-rata {pm_column}')
    plt.grid(True)

    # Menambahkan label nilai untuk setiap titik
    for i, txt in enumerate(rata2_pm_per_tahun.values):
        plt.text(rata2_pm_per_tahun.index[i], txt, f'{txt:.2f}', ha='right', va='bottom')

    # Menambahkan nilai tertinggi dan terendah
    max_value = rata2_pm_per_tahun.max()
    min_value = rata2_pm_per_tahun.min()
    
    st.pyplot()
    st.text(f'Nilai Tertinggi: {max_value:.2f}')
    st.text(f'Nilai Terendah: {min_value:.2f}')

# Fungsi untuk membuat grafik rata-rata PM berdasarkan bulan
def plot_avg_pm_month(pm_column, selected_years):
    filtered_df = df[df['year'].isin(selected_years)]
    rata2_pm_per_bulan = filtered_df.groupby(['year', 'month'])[pm_column].mean().unstack(level=0)
    plt.figure(figsize=(8, 6))
    for year in selected_years:
        plt.plot(rata2_pm_per_bulan.index, rata2_pm_per_bulan[year], marker='o', linestyle='-', label=f'Tahun {year}')
    plt.title(f'Rata-rata {pm_column} berdasarkan Bulan ({", ".join(map(str, selected_years))})')
    plt.xlabel('Bulan')
    plt.ylabel(f'Rata-rata {pm_column}')
    plt.legend()
    plt.grid(True)
    st.pyplot()

# Pemilihan kolom
st.sidebar.title('Pilih Kolom PM')
selected_pm_columns = st.sidebar.multiselect(
    'Kolom PM',
    ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'WSPM']
)

# Filter
st.sidebar.title('Filter Tahun ')
st.sidebar.write("Note : ")
st.sidebar.write("Filter ini hanya digunakan untuk visualiasi rata-rata berdasarkan bulan")
selected_years = st.sidebar.multiselect('Pilih Tahun', df['year'].unique())

# Menampilkan grafik
for pm_column in selected_pm_columns:
    st.subheader(f'Analisis {pm_column}')
    col1, col2 = st.columns(2)
    with col1:
        plot_avg_pm_year(pm_column)
    with col2:
        if selected_years:
            plot_avg_pm_month(pm_column, selected_years)

st.set_option('deprecation.showPyplotGlobalUse', False)