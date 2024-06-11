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
import streamlit as st
import requests
import pandas as pd

# URL dell'endpoint Shelly
shelly_url = 'http://172.16.10.134/'

def fetch_shelly_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Errore nel recuperare i dati: {response.status_code}")
        return None

st.title('Monitoraggio dei Dati della Presa Shelly')

data = fetch_shelly_data(shelly_url)

if data:
    st.write("Dati ricevuti dalla presa Shelly:")
    st.json(data)
    
    # Supponendo che i dati siano in un formato tabellare
    df = pd.DataFrame(data)
    st.dataframe(df)
    
    # Puoi aggiungere ulteriori visualizzazioni dei dati qui
    # Ad esempio, se hai dati di potenza e vuoi visualizzarli con un grafico a linea:
    if 'power' in df.columns:
        st.line_chart(df['power'])
