pip install streamlit ShellyPy

import streamlit as st
import pandas as pd
import math
from pathlib import Path

# titolo della pagina
st.set_page_config(
    page_title='QUINDI PRESA',
    page_icon=':earth_americas:',
)

# -----------------------------------------------------------------------------

# Inserisci qui l'indirizzo IP della tua presa Shelly

import streamlit as st
from ShellyPy import Shelly

# Creazione di un'istanza del dispositivo Shelly
shelly_ip = '172.16.10.134'
shelly = Shelly(shelly_ip)

try:
    relay_status = shelly.get_relay(0)
    print("Relay status retrieved:", relay_status)
except Exception as e:
    print(f"Errore nel recuperare i dati: {e}")


