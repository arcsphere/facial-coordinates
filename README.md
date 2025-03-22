# 🧠 Facial Landmark Detection Microservice

## 📌 Submission by: Arjun Shrivatsan

---

## 📖 Introduction

This microservice exposes a facial landmark detection API using the MediaPipe Face Mesh model. Users can upload a face image, and the service returns precise facial landmark coordinates along with key measurements such as forehead width, eye gap, and chin width. This service demonstrates how computer vision models can be productized and made available via simple API calls.

---

## 🧰 Tech Stack

| Component          | Technology                            |
|-------------------|----------------------------------------|
| Language           | Python 3.10                            |
| Framework          | Flask                                  |
| Facial Detection   | MediaPipe Face Mesh                    |
| Image Processing   | OpenCV, Pillow                         |
| Containerization   | Docker                                 |
| Deployment         | Render.com                             |
| API Testing        | cURL                                   |

---

## ⚙️ How This Was Built

- We used Flask to build a lightweight microservice that receives image uploads via HTTP POST.
- Images are converted to NumPy arrays and processed using OpenCV and MediaPipe's Face Mesh model.
- The app extracts key facial landmarks and computes measurement values between specific landmark indices.
- The service returns a JSON response containing all landmarks and derived metrics.

---

## DOCUMENTS 

Are in the docs folder 



## 🛠️ Installation Instructions

You will need a render.com acocount, a github account and gitbub private access key. 

```bash
# 1. Clone the repo
git clone https://github.com/arcsphere/facial-coordinates.git
cd eai6010-render-ready

# 2. (Optional) Set up virtual environment
pyenv activate mp-env

# 3. Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Running Instructions

### 🔬 Local Development

```bash
python app.py
```

This will start a Flask development server on `http://127.0.0.1:5000`.

### 🌐 Test API Using curl

```bash
curl -X POST -F "image=@/path/to/image.jpg" https://facial-coordinates.onrender.com/face-coordinates
```

Example with real path:

```bash
curl -X POST -F "image=@/Users/arjunshrivatsan/Downloads/Study/NEU/EAI\ 6010\ -\ Applications\ of\ AI\ -\ Sergiy/eai6010-render-ready/dataset/test/000015.jpg" https://facial-coordinates.onrender.com/face-coordinates
```

---

## 🧩 Additional Notes

- Model used: MediaPipe Face Mesh (Google Developers, 2023)
- Dataset tested: CelebA dataset for real-world facial variations.
- Deployment target: [Render.com](https://render.com)
- Keep service alive by pinging it periodically.

---

## ✅ Assignment Checklist

| Assignment Requirement                               | Your Work                                                                 |
|------------------------------------------------------|---------------------------------------------------------------------------|
| Create and deploy a microservice                     | ✅ Flask microservice deployed on Render.com                              |
| Use a previously built or known model                | ✅ MediaPipe Face Mesh from previous work                                 |
| Document input/output                                | ✅ Image input, JSON output with facial landmarks and measurements        |
| Specific input/output example                        | ✅ Curl POST request + JSON response documented                           |
| Accessible service URL                               | ✅ [https://facial-coordinates.onrender.com](https://facial-coordinates.onrender.com) |
| Keep the service live for grading                    | ✅ Hosted on Render; can be kept live with periodic access or "Always On" |

---

## 🔧 Useful Commands

```bash
# Activate environment
pyenv activate mp-env

# Navigate to project
cd ~/Downloads/Study/NEU/EAI\ 6010\ -\ Applications\ of\ AI\ -\ Sergiy/eai6010-render-ready

# Install dependencies
pip3 install -r requirements.txt

# Run Flask app
python3 app.py

# Git push
git add .
git commit -m "Initial deploy"
git push origin main

# Test API
curl -X POST -F "image=@/path/to/image.jpg" https://facial-coordinates.onrender.com/face-coordinates
```

---

© 2025 — Facial Landmark Detection Microservice