import streamlit as st

st.set_page_config(page_title="My Dashboard", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")

pages = {
    "Home": "home",
    "Analytics": "analytics",
    "Reports": "reports",
    "Settings": "settings"
}

selection = st.sidebar.radio("Go to", list(pages.keys()))

# --- PAGE ROUTER ---
def home():
    st.title("🏠 Home")
    st.write("Welcome to your dashboard!")

def analytics():
    st.title("📊 Analytics")
    st.write("Your analytics content goes here.")

def reports():
    st.title("📄 Reports")
    st.write("Generate and view reports here.")

def settings():
    st.title("⚙️ Settings")
    st.write("Adjust your preferences here.")

# --- RENDER SELECTED PAGE ---
if selection == "Home":
    home()
elif selection == "Analytics":
    analytics()
elif selection == "Reports":
    reports()
elif selection == "Settings":
    settings()
