pip install streamlit ShellyPy

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

# Inserisci qui l'indirizzo IP della tua presa Shelly
shelly_ip = '172.16.10.134'

# Creazione di un'istanza del dispositivo Shelly
shelly = sp(shelly_ip)

st.title('Stato della Presa Shelly')

def get_shelly_status():
    try:
        relay_status = sp.get_relay(0)
        return relay_status
    except Exception as e:
        st.error(f"Errore nel recuperare i dati: {e}")
        return None

relay_status = get_shelly_status()

if relay_status is not None:
    if relay_status['ison']:
        st.success("La presa Shelly è ACCESA.")
    else:
        st.warning("La presa Shelly è SPENTA.")
else:
    st.write("Nessun dato disponibile.")

