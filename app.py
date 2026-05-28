import streamlit as st
import json

FILE_DB = "database_chatbot.json"

with open(FILE_DB, "r", encoding="utf-8") as f:
    json.load(f)

st.set_page_config(
    page_title="Eco Guide",
    page_icon="🌱"
)

def home_page():

    st.title("🌱 Eco Guide")

    st.subheader("Your Smart Assistant for Sustainable Living")

    st.write("""
Welcome!

This application helps users learn about:
- Eco-friendly habits
- Sustainable lifestyle tips
- Greenwashing awareness
- Environmental education
""")

    st.success("Use the sidebar to navigate through the pages.")

st.sidebar.title("🌿 Navigation Menu")

pages = [

    st.Page(home_page, title="Home", default=True),

    st.Page(
        "pages/eco_tips.py",
        title="Eco Tips"
    ),

    st.Page(
        "pages/greenwashing.py",
        title="Greenwashing"
    ),

    st.Page(
        "pages/chatbot.py",
        title="AI Chatbot"
    )
]

pg = st.navigation(pages)
pg.run()