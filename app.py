from flask import Flask, request, jsonify
import cv2
import numpy as np
from PIL import Image
import mediapipe as mp

app = Flask(__name__)
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

@app.route("/")
def home():
    return "Facial Coordinate Detection API is running!"

@app.route("/face-coordinates", methods=["POST"])
def face_coordinates():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    img = Image.open(file.stream).convert('RGB')
    img_np = np.array(img)
    img_bgr = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    results = face_mesh.process(cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB))
    h, w, _ = img_bgr.shape
    landmarks = []

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            for id, lm in enumerate(face_landmarks.landmark):
                x, y = int(lm.x * w), int(lm.y * h)
                landmarks.append({'id': id, 'x': x, 'y': y})
            break

    points = {idx: (lm['x'], lm['y']) for idx, lm in enumerate(landmarks)}
    forehead_width = abs(points.get(10, (0, 0))[0] - points.get(338, (0, 0))[0])
    eye_gap = abs(points.get(133, (0, 0))[0] - points.get(362, (0, 0))[0])
    chin_width = abs(points.get(152, (0, 0))[0] - points.get(377, (0, 0))[0])

    dimensions = {
        'forehead_width_px': forehead_width,
        'eye_gap_px': eye_gap,
        'chin_width_px': chin_width
    }

    return jsonify({'landmarks': landmarks, 'measurements': dimensions})