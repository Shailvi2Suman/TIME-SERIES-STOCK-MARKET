import streamlit as st
import os

# 🎯 Page Config
st.set_page_config(
    page_title="📈 Stock Market Forecasting",
    layout="wide"
)

# 📌 Title
st.title("📊 Stock Forecasting Dashboard – EDA | ARIMA | SARIMA | LSTM")

# 📁 Sidebar Navigation
section = st.sidebar.radio("Navigate to:", [
    "EDA (Python Script)",
    "Data Cleaning Notebook",
    "ARIMA",
    "SARIMA",
    "LSTM",
    "Dashboards (HTML)"
])

# 🔍 Show code from .py file
def show_script_code(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()
        st.code(code, language='python')
    else:
        st.error(f"❌ File not found: {file_path}")

# 🌐 Display exported HTML dashboard
def show_html_dashboard(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r", encoding='utf-8') as file:
            html = file.read()
        st.components.v1.html(html, height=800, scrolling=True)
    else:
        st.error(f"❌ Dashboard not found: {file_path}")

# 📂 Section Logic
if section == "EDA (Python Script)":
    st.subheader("📌 Exploratory Data Analysis")
    show_script_code("eda.py")

elif section == "Data Cleaning Notebook":
    st.subheader("🧹 Data Cleaning Code")
    show_script_code("data_cleaning.py")  # If this is in .py format, else convert first

elif section == "ARIMA":
    st.subheader("🔮 ARIMA Forecasting Model")
    show_script_code("arima.py")

elif section == "SARIMA":
    st.subheader("📆 SARIMA Forecasting Model")
    show_script_code("sarima.py")

elif section == "LSTM":
    st.subheader("🧠 LSTM Deep Learning Forecast")
    show_script_code("lstm_model.py")

elif section == "Dashboards (HTML)":
    st.subheader("🌐 Interactive Dashboards")
    dashboard_choice = st.selectbox("Select dashboard:", [
        "eda_dashboard.html",
        "simple_dashboard.html",
        "sarima_dashboard.html",
        "lstm_dashboard.html"
    ])
    show_html_dashboard(dashboard_choice)

