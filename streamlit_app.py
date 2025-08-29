import streamlit as st
import pandas as pd
import hmac


def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    if st.session_state.get("password_correct", False):
        return True

    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("Incorrect password.")
    return False

if check_password():

    st.title("Strategies for Democracy")
    st.write(
        "By Rob Hager"
    )

    df = pd.read_csv("dt/stratdem.csv")

    # Select which columns to display
    col1_val = st.selectbox("Select a chapter", df.chapter)

    # Find the corresponding value(s) in column2
    results = df.loc[df["chapter"] == col1_val, "summary"]

    st.write("##### Summary")
    for r in results:
        st.write(r)