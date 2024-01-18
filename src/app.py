import streamlit as st

st.title('Pon a prueba tus neuronas')

st.image('neurona.jpg')

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas"])

with tab1:
   st.header("Una entrada")
   st.write("Una neurona con una entrada")
   peso = st.slider('Introduce un peso', 0.0, 5.0, step=0.01, key="0")
   entrada = st.number_input('Introduzca el valor de la entrada: ', key="6")
   if st.button('Comprobar salida'):
      st.write("Tu neurona solo da para esto ", peso * entrada, step=0.01)


with tab2:
   st.header("Dos entradas")
   st.write("Una neurona con dos entradas")
   col1, col2 = st.columns(2)
  
   with col1:
        weight1 = st.slider('Introduce un peso', 0.0, 5.0, step=0.01, key="1")
        entrada1 = st.number_input('Introduzca el valor de la entrada: ', key="7")
   with col2:
        weight2 = st.slider('Introduce un peso', 0.0, 5.0, step=0.01, key="2")
        entrada2 = st.number_input('Introduzca el valor de la entrada: ', key="8")
   if st.button('Comprobar salida', key="12"):
      st.write("Tu neurona solo da para esto ", weight1 * entrada1 + weight2 * entrada2, step=0.01)


with tab3:
   st.header("Tres entradas")
   st.write("Una neurona con tres entradas")
   colu1, colu2, colu3 = st.columns(3)
   
   with colu1:
    weight3 = st.slider('Introduce un peso', 0.0, 5.0, step=0.01, key="3")
    entrada3 = st.number_input('Introduzca el valor de la entrada: ', key="9")
   with colu2:
    weight4 = st.slider('Introduce un peso', 0.0, 5.0, step=0.01, key="4")
    entrada4 = st.number_input('Introduzca el valor de la entrada: ', key="10")
   with colu3:
    weight5 = st.slider('Introduce un peso', 0.0, 5.0, step=0.01, key="5")
    entrada5 = st.number_input('Introduzca el valor de la entrada: ', key="11")
   sesgo = st.number_input('Introduzca el valor del sesgo: ', key="13", step= 0.01)
   if st.button('Comprobar salida', key="14"):
      st.write("Tu neurona solo da para esto ", weight3 * entrada3 + weight4 * entrada4 + weight5 * entrada5 + sesgo, step=0.01)