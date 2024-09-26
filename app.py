import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta
import os


data = pd.read_excel('gpi_analysis.xlsx')

st.title('RPP Dash')

st.dataframe(data)