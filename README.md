# 👤 Face Recognition System

A real-time face recognition system built using **Python**, **OpenCV**, and the **face_recognition** library.
This project detects and identifies faces from a live webcam feed efficiently and accurately.

---

## 🚀 Features

* 🎯 Real-time face detection using webcam
* 🧠 Face recognition using stored images
* 🏷️ Displays names of recognized individuals
* ⚡ Lightweight and fast execution

---

## 🛠️ Tech Stack

* Python
* OpenCV
* face_recognition
* NumPy

---

## 📂 Project Structure

```
face-recognition-system/
│── main.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── known_faces/
│   ├── person1.jpg
│   ├── person2.jpg
│
├── screenshots/
│   └── output.png
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/face-recognition-system.git
cd face-recognition-system
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add Known Faces

* Place images inside `known_faces/`
* File name should be the person's name

Example:

```
john.jpg → John
```

---

## ▶️ Run the Project

```
python main.py
```

---

## 📸 Output

![Output](screenshots/output.png)

* Webcam opens
* Detects faces
* Displays names in real-time

---

## ⚠️ Notes

* Ensure proper lighting for better accuracy
* Use clear front-facing images
* Avoid low-quality or blurred images

---

## 📌 Future Improvements

* Add graphical user interface (GUI)
* Store data using a database
* Improve recognition accuracy with advanced models
* Deploy as a web-based system

---

## 👨‍💻 Author

**Jatin Kumar**

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!
