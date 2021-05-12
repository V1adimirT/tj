# Импорты стандартной библиотеки


# Сторонние импорты
import streamlit as st


# Локальные импорты
from modules import load_xml

st.title('Демо журнала для трейдинга')
file_type = 'xml'
file_with_trades = st.sidebar.file_uploader("Загрузить файл", type=file_type)

if file_with_trades:
     if file_with_trades.__getattribute__('type') == 'text/xml':
          df = load_xml.parseXML(file_with_trades)
     
     st.write(df)

