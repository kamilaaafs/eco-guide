import streamlit as st
from google import genai

st.title("🤖 Eco Guide AI Chatbot")

API_KEY = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=API_KEY)

try:

    with open(
        "database_chatbot.json",
        "r",
        encoding="utf-8"
    ) as file:

        data_eco = file.read()

except FileNotFoundError:

    data_eco = "Database unavailable."

instruksi_sistem = f"""

You are Eco Guide AI.

You are friendly and helpful.

Answer ONLY using this database:

{data_eco}

If the answer does not exist in the database,
say politely:

"Sorry, that information is not available in my database."
"""

if "riwayat_chat" not in st.session_state:

    st.session_state.riwayat_chat = [

        {
            "role": "assistant",
            "teks":
            "Hello! 🌱 Ask me anything about sustainability, eco tips, or greenwashing."
        }

    ]

for pesan in st.session_state.riwayat_chat:

    with st.chat_message(
        pesan["role"]
    ):

        st.markdown(
            pesan["teks"]
        )

pertanyaan = st.chat_input(
    "Ask your question..."
)

if pertanyaan:

    with st.chat_message("user"):

        st.markdown(
            pertanyaan
        )

    st.session_state.riwayat_chat.append(

        {
            "role": "user",
            "teks": pertanyaan
        }

    )

    konteks_obrolan = (
        instruksi_sistem
        +
        "\nChat History:\n"
    )

    for msg in st.session_state.riwayat_chat:

        konteks_obrolan += (
            f"{msg['role']}: {msg['teks']}\n"
        )

    with st.chat_message(
        "assistant"
    ):

        with st.spinner(
            "Thinking..."
        ):

            try:

                response = client.models.generate_content(

                    model="gemini-2.5-flash-lite",

                    contents=konteks_obrolan
                )

                jawaban = response.text

            except Exception as e:

                jawaban = f"Error: {e}"

            st.markdown(
                jawaban
            )

    st.session_state.riwayat_chat.append(

        {
            "role": "assistant",
            "teks": jawaban
        }

    )