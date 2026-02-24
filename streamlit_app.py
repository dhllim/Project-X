import streamlit as st
from gtts import gTTS
import os
import uuid

st.title("Text-to-Speech Generator with gTTS")

user_text = st.text_area(
    "Enter text to generate voice:",
    "xin jiang! Xin jiang. Here we come. Get Ready Now. don't miss the chance"
)

lang = st.selectbox("Select language:", ["en", "zh-cn", "fr", "es"], index=0)

if st.button("Generate Voice"):
    if not user_text.strip():
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Generating voice..."):
            # Unique filename
            os.makedirs("output", exist_ok=True)
            unique_name = f"{uuid.uuid4()}.mp3"
            voice_file = os.path.join("output", unique_name)

            tts = gTTS(text=user_text, lang=lang)
            tts.save(voice_file)

        st.success("Voice generated!")

        # Proper file handling
        with open(voice_file, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/mp3")

        # Optional download button
        st.download_button(
            label="Download Audio",
            data=audio_bytes,
            file_name="voice.mp3",
            mime="audio/mp3"
        )
