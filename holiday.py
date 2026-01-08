import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Accessibility Dashboard", layout="wide")

# --- CUSTOM CSS FOR BUTTON-LIKE RADIO ---
st.markdown("""
    <style>
        /* Hide default radio buttons */
        div.row-widget.stRadio > div{flex-direction: column;}
        div.stRadio > label {font-size: 0px;}

        /* Style each option like a button */
        div.stRadio > div > label {
            background-color: #f0f2f6;
            padding: 10px 15px;
            margin: 5px 0px;
            border-radius: 8px;
            border: 1px solid #d3d3d3;
            font-weight: 600;
            color: #333;
            cursor: pointer;
        }

        /* Highlight selected option */
        div.stRadio > div > label[data-baseweb="radio"] > div:first-child {
            display: none;
        }

        div.stRadio > div > label:hover {
            background-color: #e0e7ff;
            border-color: #a5b4fc;
        }

        /* Selected option styling */
        div.stRadio > div > label[data-selected="true"] {
            background-color: #4f46e5 !important;
            color: white !important;
            border-color: #4338ca !important;
        }
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "",
    ["Home", "Overview", "Visualisations", "About"],
    key="nav"
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

elif page == "Overview":
    st.title("📊 Overview")
    st.write("Summary statistics here.")

elif page == "Visualisations":
    st.title("📈 Visualisations")
    st.write("More charts here.")

elif page == "About":
    st.title("ℹ️ About")
    st.write("Project details here.")