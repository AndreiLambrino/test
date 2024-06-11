import streamlit as st
import pandas as pd
import math
from pathlib import Path

# Set the title and favicon that appear in the Browser's tab bar.
st.set_page_config(
    page_title='GDP Dashboard',
    page_icon=':earth_americas:', # This is an emoji shortcode. Could be a URL too.
)

# -----------------------------------------------------------------------------
# Definisci il dato da esporre
dato = "Questo è un dato di esempio"

# Visualizza il dato
st.title("Il mio dato Streamlit")
st.write(dato)