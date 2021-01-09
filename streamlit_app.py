import streamlit as st
import pandas as pd
import css_and_icons

st.set_page_config(page_title="", layout='wide')

@st.cache
def get_data():
    return(pd.read_csv('https://raw.githubusercontent.com/SaskOpenData/covid19-sask/master/data/cases-sk.csv'))


# case_data = get_data()

st.header('Covid in Saskatchewan')

col1, col2, col3 = st.beta_columns((2, 1, 1))

col1.header('column 1')
col2.header('column 2')
col3.header('column 3')


def value_box(value, caption, bgcolor):
    # setup colors and icons
    color_dict = {'primary': '#2780E3', 'danger': '#ff0039', 'warning': '#ff7517'}
    icon_dict = {'primary': 'notifications', 'danger': 'error', 'warning': 'warning'}
    icon_name = icon_dict[bgcolor]
    hexcolor = color_dict[bgcolor]

    # custom css
    st.markdown("""
        <style>
            .box-value {
                font-size: 38px;
                font-weight: bold;
                color: #F9F9F9;
            }
        </style>
    """, unsafe_allow_html=True)
    css_and_icons.google_material_icon_css()

    # html DIV
    html_design = f"""
        <div style="background-color:{hexcolor}">
            <div class='inner' style="padding-left: 20px; padding-right: 20px; padding: 10px;">
                <p class='box-value'>{value}</p>
                <p class='box-caption' style="color:#F9F9F9">{caption}</p>
            </div>
            <div class='icon'>
                <i class='material-icons' style='font-size: 80px; position: absolute; top: 15px; right: 15px; color: rgba(0, 0, 0, 0.15)'>{icon_name}</i>
            </div>
        </div>
    """
    st.markdown(html_design, unsafe_allow_html=True)


with col1:
    value_box(100, 'Just a number', 'primary')


with col2:
    value_box(500, 'This is a warning', 'warning')

with col3:
    value_box(400, 'DANGER!!', 'danger')


