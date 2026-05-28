import json
import streamlit as st

st.title("♻️ Eco Tips")

st.write(
    "Simple habits that can help protect the environment."
)

with open(
    "database_chatbot.json",
    "r",
    encoding="utf-8"
) as f:

    db = json.load(f)

tips = db.get(
    "eco_guide",
    {}
).get(
    "eco_tips",
    []
)

if not tips:

    st.info("No eco tips available.")

else:

    for tip in tips:

        judul = tip.get(
            "judul",
            "Tip"
        )

        isi = tip.get(
            "isi",
            "-"
        )

        st.subheader(judul)

        st.write(isi)

        st.divider()