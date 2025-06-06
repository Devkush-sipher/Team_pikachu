
import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, date, time, timedelta
from utils import load_data, save_sleep

st.title("😴 Sleep Tracker")

# Add new log
st.header("Add New Sleep Log")
col1, col2 = st.columns(2)
with col1:
    sleep_date = st.date_input("Date", value=date.today())
    start_time = st.time_input("Bed Time", value=time(23, 0))
with col2:
    end_time = st.time_input("Wake Time", value=time(7, 0))

if st.button("Add Log"):
    start_dt = datetime.combine(sleep_date, start_time)
    end_dt = datetime.combine(
        sleep_date + timedelta(days=1 if end_time < start_time else 0),
        end_time
    )
    save_sleep(start_dt, end_dt)
    st.success("Sleep log saved! Please refresh to see the updated chart.")

# Display histogram
sleep_df, _, _ = load_data()
if sleep_df.empty:
    st.info("No sleep data yet.")
else:
    st.subheader("Sleep Duration Histogram (hours)")
    chart = alt.Chart(sleep_df).mark_bar().encode(
        x=alt.X('duration', bin=alt.Bin(maxbins=20), title="Hours Slept"),
        y='count()'
    ).properties(width=700, height=400)
    st.altair_chart(chart, use_container_width=True)

    st.dataframe(sleep_df.sort_values('date', ascending=False), use_container_width=True)
