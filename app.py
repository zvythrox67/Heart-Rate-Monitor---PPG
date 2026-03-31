import streamlit as st
import math
import time

st.set_page_config(page_title= "Heart Rate Monitor")

st.title("Real-Time Heart Rate Monitor")
st.write("Simulates PPG signals and detects heartbeats in real time.")

st.sidebar.header("Settings")
heart_rate_target = st.sidebar.slider("target Heart Rate (BPM)", 50, 120, 75)
threshold = st.sidebar.slider("Detection Threshold", 0.5, 0.9, 0.7)
min_beat_gap = st.sidebar.slider("Min Time Between Beats (seconds)", 0.4, 0.8, 0.6)

if 'running' not in st.session_state:
    st.session_state.running = False
if 'beat_count' not in st.session_state:
    st.session_state.beat_count = 0
if 'peak_times' not in st.session_state:
    st.session_state.peak_times = []

col1, col2 = st.colums(2)

with col1:
    if st.buttom("Start Monitor"):
        st.session_state.running = True
        st.session_state.beat_count = 0
        st.session_state.peak_times = []

with col2:
    if st.button("Stop"):
        st.session_state.running = False