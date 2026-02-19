import streamlit as st
from gtts import gTTS
import os

st.title("Text-to-Speech Generator with gTTS")

# Text input from user
user_text = st.text_area("Enter text to generate voice:", 
                         "xin jiang! Xin jiang. Here we come. Get Ready Now. don't miss the chance")

# Language selection (optional)
lang = st.selectbox("Select language:", ["en", "zh-cn", "fr", "es"], index=0)

if st.button("Generate Voice"):
    if not user_text.strip():
        st.warning("Please enter some text first!")
    else:
        # Generate TTS
        tts = gTTS(text=user_text, lang=lang)
        os.makedirs("output", exist_ok=True)
        voice_file = os.path.join("output", "voice.mp3")
        tts.save(voice_file)

        st.success("Voice generated!")

        # Play voice
        audio_file = open(voice_file, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
