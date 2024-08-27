import streamlit as st
import pandas

st.set_page_config(layout="wide")

content_intro = """
    Lorem ipsum odor amet, consectetuer adipiscing elit. Viverra arcu tristique
    magna aenean taciti. Tellus nunc gravida, curabitur metus tempor 
    himenaeos! Enim duis leo dolor senectus nullam dolor fusce consectetur. 
    Ornare at fusce augue litora; eget praesent. Vestibulum nec tincidunt id 
    habitasse faucibus hac himenaeos; pharetra etiam. Lacinia class porttitor 
    rutrum fusce urna etiam. Aliquet hendrerit platea cubilia mollis mus 
    vitae orci.\n
    Lacus condimentum eros hendrerit aliquam habitasse ut parturient. Per
    eleifend ultrices sollicitudin cursus tempor nostra vestibulum id. 
    Penatibus lacus quisque class commodo suspendisse. Bibendum torquent 
    turpis viverra pellentesque tortor diam ultrices. Maximus luctus leo 
    eleifend est donec phasellus. Tincidunt egestas purus vulputate 
    scelerisque justo risus. Placerat cras finibus augue adipiscing pharetra 
    netus semper tempor. Vulputate tempus feugiat massa eleifend libero 
    ridiculus. Euismod dictum ullamcorper enim tellus ex netus.
    """

contact_message = """
Hieronder vindt u enkele van de apps die ik heb ontwikkeld. Neem gerust 
contact met mij op!
"""

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
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[int(len(df) / 2):].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source code]({row['url']})")
