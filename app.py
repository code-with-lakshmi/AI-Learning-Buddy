import os
import streamlit as st
from google import genai

st.set_page_config(
    page_title="AI Learning Buddy Lakshmi",
    page_icon="🎓"
)

api_key = st.secrets.get("GOOGLE_API_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found")
    st.stop()

client = genai.Client(api_key=api_key)

st.title("🎓 AI Learning Buddy Lakshmi")

topic = st.text_input("Enter a Topic")

option = st.selectbox(
    "Choose Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

if st.button("Generate"):
    if not topic:
        st.warning("Please enter a topic.")
    else:
        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple language for a beginner."
        elif option == "Real-Life Example":
            prompt = f"Give one simple real-life example of {topic}."
        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."
        else:
            prompt = topic

        try:
            with st.spinner("Generating..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt,
                )

            st.write(response.text)

        except Exception as e:
            st.exception(e)