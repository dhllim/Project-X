import os
import subprocess

IMAGE_PATH = "./input.jpg"   # your uploaded photo
AUDIO_PATH = "./voice.mp3"

SADTALKER_PATH = "./"

def run_sadtalker():
    cmd = f"""
    python inference.py \
        --driven_audio {AUDIO_PATH} \
        --source_image {IMAGE_PATH} \
        --result_dir ./results \
        --still \
        --enhancer gfpgan
    """
    subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    print("Generating talking smiling video...")
    run_sadtalker()
    print("Done! Check SadTalker/results/")

