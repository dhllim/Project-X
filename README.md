Test to generate static photo to a video


amend the below script: generate_voice.py

from gtts import gTTS

text = "xin jiang! Xin jiang. Here we come. Get Ready Now. don't miss the chance"
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("Voice generated!")

1. Run below command to geberate a mp3 audio
python ../notebook/generate_voice.py


Then generate the video
python ../notebook/photo_to_talking_video.py