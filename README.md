**Laser Dodger** is a simple desktop arcade game built using Python and PyQt6. The objective of the game is to avoid falling lasers for as long as possible. The player controls a green circle using the arrow keys to dodge red lasers that descend from the top of the screen.

## Features

* Simple and clean UI using PyQt6
* Keyboard-controlled player movement
* Randomly spawning falling lasers
* Collision detection with game over screen
* Smooth animations using timers

## How to Play

* Use the **Left Arrow** and **Right Arrow** keys to move the player horizontally
* Avoid the falling red lasers
* The game ends when a laser touches the player

## Requirements

* Python 3.6 or later
* PyQt6

## Installation

1. Clone this repository or copy the source code.

2. Install PyQt6 if you haven't already:

   ```
   pip install PyQt6
   ```

3. Run the game:

   ```
   python laser_dodger.py
   ```

## Code Overview

* `LaserDodger` class handles game logic, rendering, and input.
* `paintEvent` draws the player and lasers.
* `keyPressEvent` manages player movement.
* `spawn_laser` randomly adds a new falling laser at regular intervals.
* `update_game` moves lasers and checks for collisions.
* `check_collision` detects intersection between the player and any laser.
* `game_over` stops the game and displays a "Game Over" message.

## License

This project is for educational and personal use. You are free to modify and extend it.

