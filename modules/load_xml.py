# Импорты стандартной библиотеки
import xml.etree.ElementTree as etree
from typing import List, Dict


# Сторонние импорты
import pandas as pd
import streamlit as st
from streamlit.uploaded_file_manager import UploadedFile


# Локальные импорты

@st.cache
def parseXML(file_xml: UploadedFile):
    file_xml.__getattribute__
    tree = etree.parse(file_xml)
    root = tree.getroot()

    data = []
    section = root.find('SECTIONS')
    futures = section.find('DB10')
    for child in futures:
        if child.attrib.get('RqNo'):
            data.append(child.attrib)

    df = prepare_data(data)

    return df


def prepare_data(data: List[Dict[str, str]]):
    df = pd.DataFrame.from_dict(data)
    return df

