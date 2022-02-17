import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    
a1, a2, a3 = st.columns(3)

a1.image(Image.open('streamlit-logo-secondary-colormark-darktext.png'))
a2.metric("Wind", "9 mph", "-8%")
a3.metric("Humidity", "86%", "4%")

b1, b2, b3, b4 = st.columns(4)
with b1:
    st.metric("Temperature", "70 °F", "1.2 °F")
b2.metric("Wind", "9 mph", "-8%")
b3.metric("Humidity", "86%", "4%")
b4.metric("Humidity", "86%", "4%")

c1, c2 = st.columns(2)
c1.metric("ABC", "95%", "4%")
c2.metric("XYZ", "75%", "5%")
