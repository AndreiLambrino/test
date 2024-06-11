import streamlit as st
import ShellyPy as sp
import pandas as pd
import math
from pathlib import Path

# titolo della pagina
st.set_page_config(
    page_title='QUINDI PRESA',
    page_icon=':earth_americas:',
)

# -----------------------------------------------------------------------------
# Definisci il dato da esporre
dato = "Questo è un dato di esempio"

# Visualizza il dato
st.title("Il mio dato Streamlit")
st.write(dato)

ip_address = "172.16.10.134"
device = sp.Shelly(ip_address)

# Leggi il consumo cumulativo (in kWh)
energy = device.meter('0')
energy

st.write("Consumo", energy['power'])