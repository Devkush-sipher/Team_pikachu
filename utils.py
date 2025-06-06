
import pandas as pd
import os

DATA_DIR = "data"
SLEEP_FILE = os.path.join(DATA_DIR, "sleep.csv")
EXP_FILE = os.path.join(DATA_DIR, "expenses.csv")
TODO_FILE = os.path.join(DATA_DIR, "todo.csv")

# Ensure files exist
os.makedirs(DATA_DIR, exist_ok=True)
for f in [SLEEP_FILE, EXP_FILE, TODO_FILE]:
    if not os.path.exists(f):
        pd.DataFrame().to_csv(f, index=False)

def load_data():
    sleep_df = (
        pd.read_csv(SLEEP_FILE, parse_dates=['date', 'start', 'end'])
        if os.path.getsize(SLEEP_FILE) else
        pd.DataFrame(columns=['date', 'start', 'end', 'duration'])
    )
    exp_df = (
        pd.read_csv(EXP_FILE, parse_dates=['date'])
        if os.path.getsize(EXP_FILE) else
        pd.DataFrame(columns=['date', 'amount', 'category', 'status'])
    )
    todo_df = (
        pd.read_csv(TODO_FILE, parse_dates=['date'])
        if os.path.getsize(TODO_FILE) else
        pd.DataFrame(columns=['date', 'task', 'done'])
    )
    return sleep_df, exp_df, todo_df

def save_sleep(start_dt, end_dt):
    sleep_df, _, _ = load_data()
    new = {
        'date': start_dt.date(),
        'start': start_dt,
        'end': end_dt,
        'duration': (end_dt - start_dt).seconds / 3600
    }
    sleep_df = pd.concat([sleep_df, pd.DataFrame([new])], ignore_index=True)
    sleep_df.to_csv(SLEEP_FILE, index=False)

def save_expense(exp_date, amount, category, status):
    _, exp_df, _ = load_data()
    new = {
        'date': exp_date,
        'amount': amount,
        'category': category,
        'status': status
    }
    exp_df = pd.concat([exp_df, pd.DataFrame([new])], ignore_index=True)
    exp_df.to_csv(EXP_FILE, index=False)

def save_task(task_date, task_text, done):
    _, _, todo_df = load_data()
    new = {'date': task_date, 'task': task_text, 'done': done}
    todo_df = pd.concat([todo_df, pd.DataFrame([new])], ignore_index=True)
    todo_df.to_csv(TODO_FILE, index=False)
