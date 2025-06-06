
import streamlit as st
import pandas as pd
from datetime import date, datetime
from utils import load_data

st.set_page_config(page_title="My Life Dashboard", page_icon="🏠", layout="wide")

st.title("🏠 My Life Dashboard")
st.markdown(
    "Use the sidebar to navigate to different trackers.\n\n"
    "Below is a simple calendar‑style overview of your sleep, expenses and tasks for this month."
)

sleep_df, exp_df, todo_df = load_data()

# KPI cards
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total Sleep Logs", len(sleep_df))
    if not sleep_df.empty:
        avg_sleep = sleep_df['duration'].mean()
        st.metric("Avg Sleep (hrs)", f"{avg_sleep:.1f}")
with col2:
    st.metric("Total Spent (Paid)", f"${exp_df[exp_df['status']=='Paid']['amount'].sum():,.2f}")
    st.metric("Pending", f"${exp_df[exp_df['status']=='Pending']['amount'].sum():,.2f}")
with col3:
    st.metric("Tasks Today", len(todo_df[todo_df['date']==pd.Timestamp(date.today())]))

# Generate a calendar‑style summary table for this month
start_month = date.today().replace(day=1)
dates = pd.date_range(start_month, periods=42)  # 6‑week view
summary = pd.DataFrame({'date': dates})

summary['Sleep (hrs)'] = summary['date'].map(
    lambda d: sleep_df[sleep_df['date']==pd.Timestamp(d.date())]['duration'].sum()
)
summary['Expense ($)'] = summary['date'].map(
    lambda d: exp_df[exp_df['date']==pd.Timestamp(d.date())]['amount'].sum()
)
summary['Tasks'] = summary['date'].map(
    lambda d: len(todo_df[todo_df['date']==pd.Timestamp(d.date())])
)

summary_view = summary[['date','Sleep (hrs)','Expense ($)','Tasks']].set_index('date')
st.dataframe(summary_view, use_container_width=True)
