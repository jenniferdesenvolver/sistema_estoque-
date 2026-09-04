import streamlit as st 
st.title (" SISTEMA AFTER") 
produto= st.text_input (" PRODUTO: ") 
estoque= st.number_input ("QUANTIDADE ESTOQUE ", min_value=0, step=1) 
preco= st.number_input (" PREÇO DE VENDA (R$)", min_value=0.0, step=0.50) 
custo= st.number_input (" CUSTO DO PRODUTO (R$)", min_value=0.0, step=0.50) 
compra= st.number_input ( " QUANTIDADE VENDA", min_value=1, step=1) 
if st.button (" REALIZAR VENDA ") :
  st.write ("VENDA REALIZADA COM SUCESSO ") 
if st.button (" CANCELAR VENDA " ) :
  st.write (" VENDA CANCELADA COM SUCESSO") 
if compra <= estoque:
  estoque= estoque - compra
  st.write("estoque:", estoque) 
else:
  st. write("estoque insuficiente") 
