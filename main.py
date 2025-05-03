import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, QTimer, QRect

# Game Constants
WIDTH, HEIGHT = 400, 500
PLAYER_SIZE = 30
LASER_WIDTH, LASER_HEIGHT = 20, 40
LASER_SPEED = 5
LASER_INTERVAL = 1000  # New laser every 1000ms

class LaserDodger(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Laser Dodger")
        self.setFixedSize(WIDTH, HEIGHT)
        self.setStyleSheet("background-color: black;")
        self.player_x = WIDTH // 2 - PLAYER_SIZE // 2
        self.player_y = HEIGHT - 60
        self.lasers = []
        self.game_over_label = QLabel("GAME OVER", self)
        self.game_over_label.setStyleSheet("color: white; font-size: 24px; font-weight: bold;")
        self.game_over_label.setGeometry(WIDTH // 2 - 70, HEIGHT // 2 - 20, 140, 40)
        self.game_over_label.setVisible(False)
        self.laser_timer = QTimer(self)
        self.laser_timer.timeout.connect(self.spawn_laser)
        self.laser_timer.start(LASER_INTERVAL)



