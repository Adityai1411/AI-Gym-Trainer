import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QPalette, QColor
from PyQt5.QtCore import Qt
from .main_window import MainWindow

RES_DIR = os.path.join(os.path.dirname(__file__), "resources")

def run_app():
    app = QApplication(sys.argv)
    app.setApplicationName("AI Gym Trainer")

    win = QWidget()
    win.setWindowTitle("AI Gym Trainer – Welcome")
    win.resize(960, 540)

    layout = QVBoxLayout()
    layout.setContentsMargins(40, 40, 40, 40)
    layout.setSpacing(20)

    banner = QLabel()
    banner.setAlignment(Qt.AlignCenter)
    banner_path = os.path.join(RES_DIR, "bg_gym.jpg")
    if os.path.exists(banner_path):
        pix = QPixmap(banner_path)
        banner.setPixmap(pix.scaled(880, 320, Qt.KeepAspectRatio, Qt.SmoothTransformation))
    else:
        pal = QPalette()
        pal.setColor(QPalette.Window, QColor("#222"))
        banner.setAutoFillBackground(True)
        banner.setPalette(pal)
        banner.setText("AI Gym Trainer")
        banner.setStyleSheet("color:white; font-size:28px;")

    title = QLabel("AI Gym Trainer")
    title.setAlignment(Qt.AlignCenter)
    title.setFont(QFont("Arial", 24, QFont.Bold))

    btn = QPushButton("Start")
    btn.setFixedHeight(44)
    btn.setStyleSheet("""
        QPushButton {
            background-color: #1abc9c; color: white; border: none; 
            border-radius: 8px; font-size: 16px; padding: 8px 16px;
        }
        QPushButton:hover { background-color: #17a589; }
    """)

    def go_main():
        main = MainWindow()
        main.show()
        win.close()

    btn.clicked.connect(go_main)

    layout.addWidget(banner)
    layout.addWidget(title)
    layout.addWidget(btn, alignment=Qt.AlignCenter)

    win.setLayout(layout)
    win.show()
    sys.exit(app.exec_())
