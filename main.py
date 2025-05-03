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

