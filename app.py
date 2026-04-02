import streamlit as st
import math
import time
import numpy as np
import matplotlib.pyplot as plt



st.set_page_config(page_title= "Heart Rate Monitor")

st.title("Real-Time Heart Rate Monitor")
st.write("Simulates PPG signals and detects heartbeats in real time.")

st.sidebar.header("Settings")
heart_rate_target = st.sidebar.slider("target Heart Rate (BPM)", 50, 120, 75)
threshold = st.sidebar.slider("Detection Threshold", 0.5, 0.9, 0.7)
min_beat_gap = st.sidebar.slider("Min Time Between Beats (seconds)", 0.4, 0.8, 0.6)

def make_heartbeat(t, heart_rate):
    secounds_per_beat = 60/ heart_rate
    position_in_beat = (t %secounds_per_beat)/ secounds_per_beat

    if position_in_beat < 0.3:
        value = (position_in_beat/0.3) ** 2
    else:
        value = math.exp(-(position_in_beat - 0.3) * 8)

    noise = math.sin(t * 50) * 0.05
    breathing = math.sin(t * 0.2) * 0.1

    return value + noise + breathing

if 'running' not in st.session_state:
    st.session_state.running = False
if 'beat_count' not in st.session_state:
    st.session_state.beat_count = 0
if 'peak_times' not in st.session_state:
    st.session_state.peak_times = []

col1, col2 = st.columns(2)

with col1:
    if st.button("Start Monitor"):
        st.session_state.running = True
        st.session_state.beat_count = 0
        st.session_state.peak_times = []

with col2:
    if st.button("Stop"):
        st.session_state.running = False

metric_placeholder = st.empty()
plot_placeholder = st.empty()
beat_placeholder = st.empty()

if st.session_state.running:
    start_time = time.time()
    last_beat_time = 0
    times = []
    signals = []

    st.info("Monitoring... Press Stop to end")

    while st.session_state.running and time.time() - start_time < 30:
        current_time = time.time() - start_time
        signal = make_heartbeat(current_time, heart_rate_target)
        times.append(current_time)
        signals.append(signal)

        if len(times) > 250:
            times = times[-250:]
            signals = signals[-250:]

        if signal > threshold and (current_time - last_beat_time) > min_beat_gap:
            last_beat_time = current_time
            st.session_state.beat_count +=1
            st.session_state.peak_times.append(current_time)

            if len(st.session_state.peak_times) >= 2:
                recent = st.session_state.peak_times[-5:]
                intervals= []
                for i in range(len(recent) - 1):
                    intervals.append(recent[i+1] - recent[i])
                avg_interval = sum(intervals) / len(intervals)
                current_bpm = 60 / avg_interval
            else:
                current_bpm = 0