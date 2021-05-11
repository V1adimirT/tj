# Импорты стандартной библиотеки
import xml.etree.ElementTree as etree
# Сторонние импорты
import streamlit as st
# Локальные импорты

@st.cache
def parseXML(file_xml):
    tree = etree.parse(file_xml)
    root = tree.getroot()

    data = []
    section = root.find('SECTIONS')
    futures = section.find('DB10')
    for child in futures:
        data.append(child.attrib)

    return data

