import json
import streamlit as st

st.title("🌍 Greenwashing Awareness")

st.write(
    "Learn how companies can appear eco-friendly without real environmental action."
)

with open(
    "database_chatbot.json",
    "r",
    encoding="utf-8"
) as f:

    db = json.load(f)

data = db.get(
    "eco_guide",
    {}
).get(
    "greenwashing",
    []
)

if not data:

    st.info("No data available.")

else:

    for item in data:

        judul = item.get(
            "judul",
            "Topic"
        )

        isi = item.get(
            "isi",
            "-"
        )

        st.subheader(judul)

        st.write(isi)

        st.divider()