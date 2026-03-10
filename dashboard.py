import streamlit as st
import requests

st.set_page_config(page_title="Thirdeye Signals", page_icon="👁️")

st.title("Thirdeye Signals")
st.subheader("AI Signal Detection Dashboard")

st.divider()

# Status check
st.markdown("### System Status")
try:
    response = requests.get("http://127.0.0.1:8000/status")
    data = response.json()
    st.success("API is Live and Running")
    st.json(data)
except:
    st.error("API is offline - start your FastAPI server first")

st.divider()

# Predict section
st.markdown("### Run a Signal")
user_input = st.text_input("Enter signal data:", placeholder="Type something...")

if st.button("Analyze Signal"):
    if user_input:
        result = requests.post(
            "http://127.0.0.1:8000/predict",
            json={"data": user_input}
        )
        st.json(result.json())
    else:
        st.warning("Please enter some signal data first")