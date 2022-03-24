# -*- coding: utf-8 -*-
"""
Created on Sat Feb 19 09:43:15 2022

@author: saura
"""
import pandas as pd
import streamlit as st
import plotly.express as px
import Main_output
import pickle
import os
from matplotlib import pyplot as plt

st.title("Crowd Counting")
st.markdown("Welcome to the crowd counting web-tool")
st.header("1.Live Crowd Analysis Tool ")
st.markdown(">Useful for live crowd counting and tracking")
uploaded_file = st.file_uploader("Upload Image",type=["png","jpg","jpeg","mp4","mkv"])
if uploaded_file is not None:
    pass



st.header("2.Normal Crowd Analysis Tool")
st.markdown(">Useful and more accurate in case of large crowds")
uploaded_file_2 = st.file_uploader("Upload Image",type=["png","jpg","jpeg"])
if uploaded_file_2 is not None:
    print(type(uploaded_file_2))
    count,image = Main_output.Count(uploaded_file_2)
    st.subheader("Count :{}".format(count))
    st.image(uploaded_file_2,caption="Image",width=550)
    
    