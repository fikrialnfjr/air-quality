import streamlit as st
from clustering import performClustering, getSelectedAttributes, clustering_page, loadData
from distribusi import distribution_page, loadData

def main():
    st.title("Dashboard Air Quality Shunyi")
    st.sidebar.header("Options")

    page = st.sidebar.selectbox("Select a page", ["Show Dataset", "Clustering", "Distribusi"])

    if page == "Show Dataset":
        show_dataset()
    elif page == "Clustering":
        clustering_page()
    elif page == "Distribusi":
        distribution_page()

def show_dataset():
    df = loadData()
    st.header("Dataset")
    st.write(df)


if __name__ == '__main__':
    main()
    st.set_option('deprecation.showPyplotGlobalUse', False)
