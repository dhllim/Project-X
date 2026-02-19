import cv2
import numpy as np
import dlib
import imageio

# ---------- SETTINGS ----------
INPUT_IMAGE = "input.jpg"
OUTPUT_VIDEO = "smiling_video.mp4"
FRAMES = 120
FPS = 24
LANDMARK_MODEL = "shape_predictor_68_face_landmarks.dat"

# ---------- LOAD MODELS ----------
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(LANDMARK_MODEL)

# ---------- LOAD IMAGE ----------
img = cv2.imread(INPUT_IMAGE)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
faces = detector(img_rgb)

if len(faces) == 0:
    raise Exception("No face detected. Humanity fails again.")

face = faces[0]
landmarks = predictor(img_rgb, face)

def get_points(indices):
    return np.array([[landmarks.part(i).x, landmarks.part(i).y] for i in indices])

mouth_pts = get_points(range(48, 68))
left_eye_pts = get_points(range(36, 42))
right_eye_pts = get_points(range(42, 48))

# ---------- ANIMATION FUNCTIONS ----------

def smile_warp(frame, strength):
    """Stretch mouth upward to fake smile"""
    pts = mouth_pts.copy()
    center = np.mean(pts, axis=0).astype(int)

    warped = frame.copy()
    for (x, y) in pts:
        dy = int(strength * 5)
        cv2.circle(warped, (x, y - dy), 2, (0,255,0), -1)

    return warped

def blink(frame, amount):
    """Draw eyelids"""
    frame_copy = frame.copy()
    for eye in [left_eye_pts, right_eye_pts]:
        center = np.mean(eye, axis=0).astype(int)
        w = int(np.linalg.norm(eye[0] - eye[3]))
        h = int(5 * amount)
        cv2.ellipse(frame_copy, tuple(center), (w//2, h), 0, 0, 360, (0,0,0), -1)
    return frame_copy

def head_bob(frame, frame_id):
    """Subtle vertical movement"""
    shift = int(3 * np.sin(frame_id / 10))
    M = np.float32([[1,0,0],[0,1,shift]])
    return cv2.warpAffine(frame, M, (frame.shape[1], frame.shape[0]))

# ---------- GENERATE FRAMES ----------
frames = []

for i in range(FRAMES):
    frame = img_rgb.copy()

    # head movement
    frame = head_bob(frame, i)

    # smile oscillation
    smile_strength = (np.sin(i/8) + 1) / 2
    frame = smile_warp(frame, smile_strength)

    # blink every 30 frames
    blink_strength = max(0, np.sin((i % 30)/30 * np.pi * 2))
    frame = blink(frame, blink_strength)

    frames.append(frame)

# ---------- SAVE VIDEO ----------
imageio.mimsave(OUTPUT_VIDEO, frames, fps=FPS)
print("Video saved:", OUTPUT_VIDEO)


