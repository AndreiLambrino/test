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
shelly = Shelly(shelly_ip)

st.title('Stato della Presa Shelly')

def get_shelly_status():
    try:
        relay_status = shelly.get_relay(0)
        st.write("Relay status retrieved:", relay_status)
        return relay_status
    except Exception as e:
        st.error(f"Errore nel recuperare i dati: {e}")
        return None

# Debug: Mostra l'IP della Shelly
st.write(f"Collegamento alla presa Shelly all'indirizzo: {shelly_ip}")

relay_status = get_shelly_status()

if relay_status is not None:
    if relay_status['ison']:
        st.success("La presa Shelly è ACCESA.")
    else:
        st.warning("La presa Shelly è SPENTA.")
else:
    st.write("Nessun dato disponibile.")


