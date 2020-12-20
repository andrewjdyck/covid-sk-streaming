import streamlit as st
import pandas as pd

@st.cache
def get_data():
    return(pd.read_csv('https://raw.githubusercontent.com/SaskOpenData/covid19-sask/master/data/cases-sk.csv'))

st.header('Covid in Saskatchewan')
st.write(get_data())
