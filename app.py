# Импорты стандартной библиотеки


# Сторонние импорты
import pandas as pd
import streamlit as st


# Локальные импорты
from modules import load_xml

st.title('Демо журнала для трейдинга')
file_xml = st.sidebar.file_uploader("Загрузить файл xml", type="xml")

if file_xml:
     data = load_xml.parseXML(file_xml)
     df = pd.DataFrame.from_dict(data)
     st.write(df)

