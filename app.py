import streamlit as st 
st.title (" sistema estoque") 
produto= st.text_input (" nome do produto ") 
estoque= st.nunber_input ("quantidade no estoque", min_value=0, step=1) 
