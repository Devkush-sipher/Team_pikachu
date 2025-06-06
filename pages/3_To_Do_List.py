
import streamlit as st
import pandas as pd
from datetime import date
from utils import load_data, save_task

st.title("✅ To‑Do List")

# Add task
st.header("Add Task")
task_date = st.date_input("Date", value=date.today())
task_text = st.text_input("Task description")
if st.button("Add Task"):
    if task_text:
        save_task(task_date, task_text, False)
        st.success("Task added!")
    else:
        st.error("Please write a task description.")

# View / update tasks
_, _, todo_df = load_data()
st.subheader("Tasks")
if todo_df.empty:
    st.info("No tasks yet.")
else:
    for idx, row in todo_df.sort_values('date').iterrows():
        checked = st.checkbox(
            f"{row['date'].date()} ‑ {row['task']}",
            value=row['done'],
            key=str(idx)
        )
        if checked != row['done']:
            todo_df.at[idx, 'done'] = checked
    # Save any changes
    todo_df.to_csv("data/todo.csv", index=False)
