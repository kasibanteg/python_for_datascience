import streamlit as st
from dependencies.python_files.hide_trade_marks import *
from dependencies.python_files.html_files import *
import pandas as pd
import numpy as np
from dependencies.python_files.load_css import local_css
local_css("dependencies/css/style.css")

#Hide all Streamlit menus and trade marks
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#end all Streamlit menus and trade marks
#Begin Login Css Style
st.markdown(html_login_style, unsafe_allow_html=True)
#End Login Css Style

col1,col2 = st.beta_columns((2))

with col1:
    st.write()
    #button_clicked = st.button("Ok")
    #selected = st.text_input("", "Search...")

       

with col2:
    with st.form('Form1'):
        username_set_lable_css = "<div class='login_labels'>Enter User Name<div>"
        st.markdown(username_set_lable_css, unsafe_allow_html=True)
        username = st.text_input(label='')
        password_set_lable_css = "<div class='login_labels'>Enter Password<div>"
        st.markdown(password_set_lable_css, unsafe_allow_html=True)
        password = st.text_input(label=' ')
        submitted1 = st.form_submit_button('Login')
        
       
