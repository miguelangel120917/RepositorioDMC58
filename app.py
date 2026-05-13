import streamlit as st

st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Miguel Limaquispe")

sesion = st.sidebar.selectbox("Seleccione una sesión", ["Sesión 1","Sesión 2","Sesión 3","Sesión 4"])

if session == "Sesión 1":
  st.write("Bienvenido a la sesión 1")
elif session =="Sesión 2":
  st.write("Bienvenido a la sesión 2")
elif session =="Sesión 3":
  st.write("Bienvenido a la sesión 3")
else:
  st.write("Bienvenido a la sesión 4")
