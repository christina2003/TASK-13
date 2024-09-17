# Real-Time Tic-Tac-Toe Game

## Overview
This project develops a real-time Tic-Tac-Toe game using computer vision. The game utilizes the YOLOv8 model to recognize hand gestures for player moves on a 3x3 grid.

## Requirements
- **Real-Time Tic-Tac-Toe Game**: Uses YOLO for gesture recognition.
- **Gestures Detected**: 
  - "X" Gesture
  - "O" Gesture
- **Grid Layout**: 3x3 Tic-Tac-Toe grid.
- **Dataset**: Custom collected and annotated dataset.

## Team Contributions
- **Hazem Essam**: 
  - Labeled and modified dataset.
  - Added gestures like 👍 (Like) and 👎 (Dislike).
- **Zeyad Ayman**:
  - Implemented Game GUI.
  - Integrated game rules and added menu navigation.
- **Ahmed Reda**:
  - Provided initial dataset.
  - Created frame extraction script and integrated webcam for gameplay.

## Model
- **YOLOv8s**: Chosen for its balance between speed and accuracy.

## Challenges and Solutions
- **Gesture Recognition**: Improved model accuracy for recognizing the "Like" gesture by adding more training data.
- **Integration**: Resolved issues with frame processing and model predictions in `main.py`.

## Dataset
- **Split**: 85% Training, 15% Validation.
- **Additional Data**: Collected photos with different lighting and positions, and added new gestures.

## Running the Game
1. Ensure all dependencies are installed.
2. Run `main.py` to start the game.
3. Use hand gestures to make moves on the grid.
4. use q to exit

## Acknowledgments
- YOLOv8 for object detection.
- OpenCV for computer vision functionalities.
- PyAutoGUI for game automation.
