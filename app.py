import streamlit as st 
st.title (" sistema estoque") 
produto= st.text_input (" nome do produto ") 
estoque= st.number_input ("quantidade no estoque", min_value=0, step=1) 
preco= st.number_input (" preço de venda (R$)", min_value=0.0, step=0.50) 
custo= st.number_input ("custo do produto (R$)", min_value=0.0, step=0.50) 
compra= st.number_input ( " quantidade vendas", min_value=1, step=1) 
if st.button (" realizar venda") :
st.write (" venda after realizada com sucesso") 
