
# My Life Dashboard

A lightweight **Streamlit** multipage app to help you track the essentials of everyday life: sleep, spending, and tasks.

## Features
* **Sleep Tracker** – log bed & wake times, see a histogram of sleep duration.
* **Expense Tracker** – record expenses with paid / pending status and custom categories, view category‑wise breakdown.
* **To‑Do List** – create daily tasks with checkboxes and see them at a glance.
* **Dashboard Home** – calendar‑style overview plus quick KPIs.

## Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Launch the app
streamlit run streamlit_app.py
```

All data is stored locally as CSV files inside the **data/** folder so you can inspect or back them up easily.
