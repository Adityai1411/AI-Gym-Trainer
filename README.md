
# 🏋️ AI Gym Trainer  

An **AI-powered desktop fitness assistant** built with **PyQt5** that helps users track workouts, correct exercise form, and count repetitions using **computer vision** and **pose estimation models**.  

---

## 📌 Features  
- 🎥 **Real-time Pose Detection** – Detects human body landmarks from webcam feed.  
- ✅ **Form Correction** – Provides instant feedback on whether an exercise is performed correctly.  
- 🔢 **Repetition Counter** – Automatically counts push-ups, squats, curls, etc.  
- 📊 **Progress Tracking** – Visualizes workout history with charts.  
- 🎨 **Interactive PyQt5 GUI** – User-friendly interface with a welcome screen & main dashboard.  

---

## 📂 Project Structure  
```

AI-Gym-Trainer/
│── data/               # sample videos/images (empty initially)
│── models/             # pretrained pose detection models
│── notebooks/          # Jupyter notebooks for experiments
│── src/
│   ├── core/           # backend logic
│   │   ├── form\_checker.py
│   │   ├── pose\_estimator.py
│   │   ├── rep\_counter.py
│   │   └── trainer.py
│   ├── ui/             # PyQt5 GUI
│   │   ├── resources/
│   │   ├── main\_window\.py
│   │   └── welcome\_screen.py
│   └── app.py          # entry point
│── requirements.txt    # dependencies
│── README.md           # project documentation

````

---

## 🚀 Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/AI-Gym-Trainer.git
   cd AI-Gym-Trainer

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```


## ▶️ Usage

1. Run the application:

   ```bash
   python src/app.py
   ```

2. Select a workout from the **welcome screen**.

3. Start exercise → The camera will track your pose.

4. The app provides:

   * Real-time feedback
   * Rep counting
   * Progress stats

---

## 🧠 Tech Stack

* **Frontend (UI):** PyQt5
* **Computer Vision:** OpenCV, Mediapipe / MoveNet
* **Backend:** Python (NumPy, Matplotlib)
* **ML Support:** TensorFlow / PyTorch (optional)

---

## 🔮 Future Enhancements

* 🎙️ Voice-based workout feedback
* 🏃‍♂️ More exercise categories
* ☁️ Cloud integration for progress tracking
* 📱 Mobile app extension

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.

```
