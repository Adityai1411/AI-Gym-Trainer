import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox
from PyQt5.QtGui import QImage, QPixmap, QFont
from PyQt5.QtCore import Qt, QTimer
from src.core.pose_estimator import PoseEstimator
from src.core.rep_counter import RepCounter
from src.core.form_checker import FormChecker

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✨ Full Body AI Gym Trainer ✨")
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet("background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 #1e1e2f, stop:1 #2c2c54);")

        # Core modules
        self.pose = PoseEstimator()
        self.counter = RepCounter()
        self.form = FormChecker()

        # Camera
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        # Timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(30)

        self._build_ui()

    def _build_ui(self):
        root = QWidget()
        main_layout = QHBoxLayout(root)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Video display
        self.video_label = QLabel()
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setStyleSheet("""
            background: #000;
            border-radius: 12px;
            border: 3px solid #00ffcc;
        """)
        self.video_label.setMinimumSize(900, 500)

        # Side panel
        side_panel = QVBoxLayout()
        side_panel.setSpacing(20)

        # Dropdown for exercises
        self.exercise_dropdown = QComboBox()
        self.exercise_dropdown.addItems(["Squats", "Push-ups", "Lunges", "Jumping Jacks"])
        self.exercise_dropdown.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                color: #00ffcc;
                background-color: #1e1e2f;
                border: 2px solid #00ffcc;
                border-radius: 8px;
                padding: 4px;
            }
            QComboBox::drop-down {
                border-left: 1px solid #00ffcc;
            }
        """)

        # Info labels with glow
        self.lbl_reps = QLabel("Reps: 0")
        self.lbl_feedback = QLabel("Form: —")
        for lbl in (self.lbl_reps, self.lbl_feedback):
            lbl.setFont(QFont("Arial Black", 16))
            lbl.setStyleSheet("color: #00ffcc; text-shadow: 2px 2px 8px #00fff0;")

        side_panel.addWidget(self.exercise_dropdown)
        side_panel.addWidget(self.lbl_reps)
        side_panel.addWidget(self.lbl_feedback)
        side_panel.addStretch()

        main_layout.addWidget(self.video_label, stretch=3)
        main_layout.addLayout(side_panel, stretch=1)

        self.setCentralWidget(root)

    def update_frame(self):
        if not self.cap.isOpened():
            return

        ok, frame = self.cap.read()
        if not ok:
            return

        frame = cv2.flip(frame, 1)
        landmarks = self.pose.estimate(frame)

        exercise = self.exercise_dropdown.currentText()
        reps = self.counter.update(landmarks, exercise)
        feedback = self.form.check(landmarks, exercise)

        # Overlay
        cv2.putText(frame, f"Reps: {reps}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 255), 4, cv2.LINE_AA)
        cv2.putText(frame, f"Form: {feedback}", (30, 110),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 100, 0), 3, cv2.LINE_AA)

        # Convert to QImage
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        bytes_per_line = ch * w
        qimg = QImage(rgb.data, w, h, bytes_per_line, QImage.Format_RGB888)
        pix = QPixmap.fromImage(qimg).scaled(
            self.video_label.width(), self.video_label.height(),
            Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.video_label.setPixmap(pix)

        # Update side panel
        self.lbl_reps.setText(f"Reps: {reps}")
        self.lbl_feedback.setText(f"Form: {feedback}")

def run_app():
    app = QApplication([])
    win = MainWindow()
    win.show()
    app.exec_()
