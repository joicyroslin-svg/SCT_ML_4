# SCT_ML_4 - Hand Gesture Recognition

## 📌 Project Overview

This project is developed as part of the Machine Learning Internship at SkillCraft Technologies.

The goal of this project is to build a real-time hand gesture recognition system that can detect and classify different hand gestures using webcam input. The system uses computer vision techniques to identify hand landmarks and classify gestures such as Open Palm, Fist, Victory, Pointing, Thumbs Up, Pinky, and L Shape.

---

## 🎯 Objective

To develop a hand gesture recognition model that can accurately identify and classify hand gestures from image or video data, enabling gesture-based human-computer interaction.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 🤖 Methodology

This project uses MediaPipe Hands to detect hand landmarks in real time. Based on the position of fingers and landmarks, the system identifies whether fingers are open or closed and classifies the gesture accordingly.

---

## ✋ Gestures Recognized

* Open Palm
* Fist
* Victory
* Pointing
* Thumbs Up
* Pinky
* L Shape
* Unknown Gesture

---

## 🚀 Project Workflow

1. Capture live video using webcam
2. Detect hand landmarks using MediaPipe
3. Track finger positions
4. Count raised fingers
5. Classify hand gesture
6. Display the recognized gesture on the video frame

---

## 📂 Project Structure

```text
SCT_ML_4/
│── main.py
│── README.md
│── requirements.txt
│── screenshots/
```

---

## ⚙️ Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

Required dependencies:

```text
mediapipe==0.10.21
opencv-python
numpy
```

---

## ▶️ How to Run

Run the project using:

```bash
python main.py
```

The webcam will open and start detecting hand gestures.

Press `q` to close the webcam window.

---

## 📈 Output

The system detects a hand in real time and displays:

* Hand landmarks
* Finger status
* Recognized gesture name

---

## ✅ Result

Successfully developed a real-time hand gesture recognition system using OpenCV and MediaPipe. The system can classify multiple hand gestures and display the result directly on the webcam feed.

---

## 📚 Learning Outcomes

Through this project, I learned:

* Basics of Computer Vision
* Real-time video processing
* Hand landmark detection
* Gesture classification logic
* OpenCV and MediaPipe implementation
* Human-computer interaction concepts

---

## 🔗 Internship

This project was completed as part of the Machine Learning Internship at SkillCraft Technologies.

---

## 📌 Repository Name

```text
SCT_ML_4
```
