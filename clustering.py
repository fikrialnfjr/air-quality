import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import streamlit as st

def loadData():
    df = pd.read_csv('Shunyi_clean_data.csv')
    return df

def getSelectedAttributes():
    selected_attributes = []
    col1, col2 = st.columns(2)

    with col1:
        if st.checkbox('year'):
            selected_attributes.append('year')
        if st.checkbox('day'):
            selected_attributes.append('day')
        if st.checkbox('PM2.5'):
            selected_attributes.append('PM2.5')
        if st.checkbox('SO2'):
            selected_attributes.append('SO2')
        if st.checkbox('CO'):
            selected_attributes.append('CO')
        if st.checkbox('TEMP'):
            selected_attributes.append('TEMP')
        if st.checkbox('DEWP'):
            selected_attributes.append('DEWP')
    with col2:
        if st.checkbox('month'):
            selected_attributes.append('month')
        if st.checkbox('hour'):
            selected_attributes.append('hour')
        if st.checkbox('PM10'):
            selected_attributes.append('PM10')
        if st.checkbox('NO2'):
            selected_attributes.append('NO2')
        if st.checkbox('O3'):
            selected_attributes.append('O3')
        if st.checkbox('PRES'):
            selected_attributes.append('PRES')
        if st.checkbox('WSPM'):
            selected_attributes.append('WSPM')

    return selected_attributes

def performClustering(df, selected_attributes, num_clusters):
    X = df[selected_attributes]
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(X)
    labels = kmeans.labels_
    df['Cluster'] = labels

    fig, ax = plt.subplots()
    for cluster in range(num_clusters):
        cluster_data = df[df['Cluster'] == cluster]
        ax.scatter(cluster_data[selected_attributes[0]], cluster_data[selected_attributes[1]], label=f'Cluster {cluster + 1}')
    ax.set_xlabel(selected_attributes[0])
    ax.set_ylabel(selected_attributes[1])
    ax.set_title('K-Means Clustering')
    ax.legend()
    st.pyplot(fig)

    st.subheader('Cluster Labels:')
    st.write(df[['Cluster'] + selected_attributes])

    st.subheader('Data Count per Cluster:')
    cluster_counts = df['Cluster'].value_counts().reset_index()
    cluster_counts.columns = ['Cluster', 'Count']
    st.write(cluster_counts)

def clustering_page():
    df = loadData()
    st.header("Clustering Options")

    selected_attributes = getSelectedAttributes()
    num_clusters = st.slider('Number of Clusters', min_value=2, max_value=10, value=3)

    if st.button('Perform Clustering'):
        performClustering(df, selected_attributes, num_clusters)