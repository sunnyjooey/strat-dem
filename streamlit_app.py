import streamlit as st
import pandas as pd

st.title("Strategies for Democracy")
st.write(
    "By Rob Hager"
)

df = pd.read_csv("stratdem.csv")

# Select which columns to display
col1_val = st.selectbox("Select a chapter", df.chapter)

# Find the corresponding value(s) in column2
results = df.loc[df["chapter"] == col1_val, "summary"]

st.write("##### Summary")
for r in results:
    st.write(r)
