import streamlit as st
import pandas


def show_app_column(data_row):
    st.header(data_row['title'])
    st.write(data_row['description'])
    st.image(f"images/{data_row['image']}")
    st.write(f"[Source code]({data_row['url']})")


st.set_page_config(layout="wide")

with open("sample_text.txt") as file:
    sample_text = file.read()

content_intro = sample_text[:1000]

contact_message = sample_text[:200]

col_empty_1, col_image_under_const, col_empty_2 = st.columns([2, 3, 1])
with col_image_under_const:
    st.image("images/under-construction.png", caption='Website is under '
                                                      'construction')

st.markdown('<div style="margin: 120px 0;"></div>',
            unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.image("images/my_photo.png")

with col2:
    st.title("Emile Muller")
    st.info(content_intro)

st.write(contact_message)

col3, empty_col, col4 = st.columns([1.5, .5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:int(len(df) / 2)].iterrows():
        show_app_column(row)

with col4:
    for index, row in df[int(len(df) / 2):].iterrows():
        show_app_column(row)
        