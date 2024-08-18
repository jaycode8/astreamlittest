import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(
    page_title="James",
    page_icon="person",
    layout="wide",
    initial_sidebar_state='collapsed'
)

with st.sidebar:
    selected = option_menu(
        menu_title="",
        options=['home', 'about', 'form'],
        icons=['house', 'person', 'envelope']
    )
form_page = st.container()
form = st.form(key="information", clear_on_submit=True,border=True)

html_temp = """
    <div style="background: black; padding: 10px;">
        <h2 style="color: red">hello world</h2>
    </div>
"""

def getData(data):
    print(f"Wwlcome {data['name']}, you age is {data['age']}")

if selected == "home":
    st.title(f"You have selected {selected}")
    st.markdown(html_temp, unsafe_allow_html=True)

if selected == "about":
    st.title(f"You have selected {selected}")

if selected == "form":
    col1, col2 = form_page.columns(2)
    form2 = col1.form(key="data", clear_on_submit=True)
    form3 = col2.form(key="data3")
    with col1:
        with form2:
            form2.header("Form on column 1")
            num = st.number_input("you age", 20, 30)
            name = st.text_input("Enter name")
            if st.form_submit_button():
                getData({"name": name, "age":num})

    with col2:
        with form3:
            form3.header("Form on column 2")
            num = st.number_input("you age", 20, 30)
            name = st.text_input("Enter name")
            if st.form_submit_button():
                st.json({"name": name, "age":num})


    with form:
        form.header("Expanded form")
        num = st.number_input("you age", 20, 30)
        name = st.text_input("Enter name")
        if st.form_submit_button():
            st.json({"name": name, "age":num})