Initially, the files included three videos.

I tracked the player and the ball.

In each video, I analyzed the data frame by frame using the MediaPipe library to track the player, then analyzed this data and converted it into coordinates.

I focused on kicking and standing each time the player played.

The model was trained based on the coordinates and given an accuracy rate.

The higher the video quality, the higher the accuracy rate.

Libraries used in Python:

cv2
pandas
mediapipe

from ultralytics import YOLO

import math

sklearn
