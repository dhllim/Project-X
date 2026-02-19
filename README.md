Test to generate static photo to a video


(1) amend the below script: generate_voice.py

from gtts import gTTS

text = "xin jiang! Xin jiang. Here we come. Get Ready Now. don't miss the chance"
tts = gTTS(text=text, lang="en")
tts.save("voice.mp3")

print("Voice generated!")

1. Run below command to geberate a mp3 audio
python ../notebook/generate_voice.py


(2) 
 dhllim@dhllimt14g3:~/Project-X/SadTalker$ conda activate danielvideo
(danielvideo) dhllim@dhllimt14g3:~/Project-X/SadTalker$ pwd
/home/dhllim/Project-X/SadTalker
(danielvideo) dhllim@dhllimt14g3:~/Project-X/SadTalker$ python ../notebook/generate_voice.py
Voice generated!

(3) play this mp3 to verify
/home/dhllim/Project-X/SadTalker/voice.mp3

(4) start executing this command line:
dhllim@dhllimt14g3:~/Project-X/SadTalker$ python ../notebook/photo_to_talking_video.py
Generating talking smiling video...
face enhancer....
Face Enhancer:: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 184/184 [27:04<00:00,  8.83s/it]
:
:
:
The generated video is named ./results/2026_02_18_18.10.01/input##voice_enhanced.mp4
The generated video is named: ./results/2026_02_18_18.10.01.mp4
Done! Check SadTalker/results/
(danielvideo) dhllim@dhllimt14g3:~/Project-X/SadTalker$ 

(5) then play the output mp4 file at the below folder
\\wsl.localhost\Ubuntu\home\dhllim\Project-X\SadTalker\results
