import streamlit as st
import streamlit.components.v1 as stc
#import seaborn as sns
import pandas as pd
from datetime import datetime
import time
import base64
#import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from io import BytesIO
import numpy as np
#import altair as alt
from PIL import Image
def main():
    st.set_page_config(layout="wide")
    st.info("Happy anniversary Ullu")
    #st.markdown("<h1 style='text-align: left;font-weight:italics;color: bold red;'>Happy anniversary Ullu</h1>", unsafe_allow_html=True)
    col1,col2=st.beta_columns(2)
    img = Image.open("the-owl-and-the-pussycat.jpg")
    col1.image(img)
    img2=Image.open("oie_oie_framed_it (1).png")
    col2.image(img2)
    if col2.button("ClickMeowwww"):
        st.balloons()

    audio_file = open('Gotten.mp3', 'rb')
    audio_bytes = audio_file.read()
    col2.audio(audio_bytes, format='audio / ogg')



if __name__ == '__main__':
    main()
