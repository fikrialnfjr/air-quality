import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def loadData():
    df = pd.read_csv('Shunyi_clean_data.csv')
    return df

def distribution_page():

    df = loadData()

    st.sidebar.header("Pilihan Tahun")
    selected_year = st.sidebar.radio("Pilih tahun:", df['year'].unique())

    st.header("Distribusi Nilai Data")

    st.subheader(f"Tahun {selected_year}")
    year_data = df[df['year'] == selected_year]

    available_columns = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'WSPM']

    selected_columns = st.multiselect("Pilih kolom yang ingin ditampilkan distribusinya:", available_columns)

    if len(selected_columns) > 0:
        st.write(year_data[selected_columns].describe())
        
        for column in selected_columns:
            plt.figure(figsize=(10, 6))
            plt.hist(year_data[column], bins=20, edgecolor='k')
            plt.title(f'Distribusi {column}')
            plt.xlabel(column)
            plt.ylabel('Frekuensi')
            st.pyplot()
