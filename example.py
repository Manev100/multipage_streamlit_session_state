import streamlit as st
import pandas as pd
import numpy as np

page = st.sidebar.radio("", options=["page 1", "page 2", "page 3"], key="radio_btns")

if page == "page 1":
    result = st.multiselect('Choose some options',
                 ["Option 1", "Option 2", "Option 3"],
            [], key="multiselect_widget" )
    if result:
        st.write("key of multiselect should be in session state.")
        st.write("Switch to page 2")
        st.write(st.session_state)
elif page == "page 2":
    st.write("key of multiselect is still there.")
    st.write(st.session_state["multiselect_widget"])
    st.write(st.session_state)
    st.write("Switch to page 3")
elif page == "page 3":
    st.write(st.session_state)
    st.write("key of multiselect is gone from session state.")


