from gtts import gTTS

text = "xin jiang! Xin jiang. Here we come. Get Ready Now. don't miss the chance"
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("Voice generated!")
