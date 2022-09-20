import streamlit as st
import pandas as pd
import numpy as np

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Novus Electoral", page_icon="🗳️")

st.title('Novus Electoral 🗳️')

st.header("Define tu estrategia electoral ✍️")
st.subheader("Enfócate en ella 🎯")
st.subheader("Construye un Plan de Gobierno 🏛️")

with st.form(key='my_form'):
   username = st.text_input('Username')
   password = st.text_input('Password')
   st.form_submit_button('Login')
