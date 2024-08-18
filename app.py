import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=['home', 'about'],
        icons=['house', 'person']
    )

if selected == "home":
    st.title(f"You have selected {selected}")

if selected == "about":
    st.title(f"You have selected {selected}")