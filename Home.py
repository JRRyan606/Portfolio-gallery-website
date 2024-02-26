import streamlit as st
import pandas

st.set_page_config(page_title="Home", layout="wide")

col1, col2, col3 = st.columns([1, 1, 1])

# with col1:
#     st.image("images/image-3.png")

# Add an empty column to the left of col2 for centering
col2.write("")  

with col2:
    st.title("Justin Ryan")
    content = """
    My 20 Python Projects
    """
    st.info(content)

# Add an empty column to the right of col2 for centering
col3.write("")

content2 = """
"""
st.write(content2)

col4, empty_col, col5 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col5:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
