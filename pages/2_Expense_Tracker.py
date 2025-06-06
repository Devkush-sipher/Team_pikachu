
import streamlit as st
import pandas as pd
import altair as alt
from datetime import date
from utils import load_data, save_expense

st.title("💰 Expense Tracker")

# Add expense
st.header("Add Expense")
col1, col2, col3 = st.columns(3)
with col1:
    exp_date = st.date_input("Date", value=date.today())
    amount = st.number_input("Amount ($)", min_value=0.0, step=0.01, format="%.2f")
with col2:
    category = st.text_input("Category", placeholder="e.g., Food, Rent")
with col3:
    status = st.selectbox("Status", ["Paid", "Pending"])

if st.button("Add Expense"):
    if category and amount:
        save_expense(exp_date, amount, category, status)
        st.success("Expense saved! Refresh to see the update.")
    else:
        st.error("Please enter both amount and category.")

# Overview
_, exp_df, _ = load_data()
st.subheader("Expenses Overview")
if exp_df.empty:
    st.info("No expenses recorded.")
else:
    st.dataframe(exp_df.sort_values('date', ascending=False), use_container_width=True)

    st.write("### Spending by Category (Paid)")
    paid_df = exp_df[exp_df['status']=="Paid"]
    if not paid_df.empty:
        chart = alt.Chart(paid_df).mark_bar().encode(
            x='sum(amount):Q',
            y=alt.Y('category:N', sort='-x')
        ).properties(width=700)
        st.altair_chart(chart, use_container_width=True)
