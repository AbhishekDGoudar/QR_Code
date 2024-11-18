import streamlit as st
from html_main import css, index

st.write(css, unsafe_allow_html=True)
st.write(index, unsafe_allow_html=True)