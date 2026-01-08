




import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Accessibility Dashboard", layout="wide")

# --- SIDEBAR NAVIGATION ---
page = st.sidebar.radio(
    "Navigation",
    ["Home", "Overview", "Visualisations", "About"]
)

# --- HOME PAGE ---
if page == "Home":
    st.title("🏠 Home")
    st.write("Welcome to the accessibility dashboard.")

    df = pd.DataFrame({
        "University": ["UCL", "Bristol", "UWE", "Cardiff"],
        "Score": [78, 65, 72, 81]
    })

    chart = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="University",
            y="Score",
            color="University"
        )
    )

    st.altair_chart(chart, use_container_width=True)

# --- OTHER PAGES ---
elif page == "Overview":
    st.title("📊 Overview")
    st.write("Summary statistics here.")

elif page == "Visualisations":
    st.title("📈 Visualisations")
    st.write("More charts here.")

elif page == "About":
    st.title("ℹ️ About")
    st.write("Project details here.")