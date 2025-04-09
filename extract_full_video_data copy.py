import cv2
import pandas as pd
import mediapipe as mp
from ultralytics import YOLO
import math

# تحميل الفيديو
video_path = 'mixkit-2.mp4'
cap = cv2.VideoCapture(video_path)

# إعدادات
pose = mp.solutions.pose.Pose()
model = YOLO('yolov8n.pt')

# تخزين البيانات
data = []
frame_num = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # انتهى الفيديو

    h, w, _ = frame.shape

    # --- تتبع اللاعب (MediaPipe) ---
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    x_head = y_head = x_foot = y_foot = None
    if results.pose_landmarks:
        lm = results.pose_landmarks.landmark
        x_head = int(lm[0].x * w)
        y_head = int(lm[0].y * h)
        x_foot = int(lm[mp.solutions.pose.PoseLandmark.RIGHT_FOOT_INDEX].x * w)
        y_foot = int(lm[mp.solutions.pose.PoseLandmark.RIGHT_FOOT_INDEX].y * h)

    # --- تتبع الكرة (YOLO) ---
    result = model.predict(source=frame, classes=[32], conf=0.4, verbose=False)
    x_ball = y_ball = None
    for r in result:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            x_ball = (x1 + x2) // 2
            y_ball = (y1 + y2) // 2

    # --- حساب المسافة ---
    def distance(x1, y1, x2, y2):
        if None in (x1, y1, x2, y2):
            return float('inf')
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    dist = distance(x_foot, y_foot, x_ball, y_ball)

    # --- التصنيف التلقائي ---
    if dist < 50:
        label = 'kick'
    else:
        label = 'stand'

    # --- إضافة البيانات ---
    data.append([frame_num, x_head, y_head, x_foot, y_foot, x_ball, y_ball, label])
    frame_num += 1

cap.release()

# حفظ البيانات في ملف CSV
df = pd.DataFrame(data, columns=['frame', 'x_head', 'y_head', 'x_foot', 'y_foot', 'x_ball', 'y_ball', 'label'])
df.dropna(inplace=True)  # إزالة أي صف ناقص
df.to_csv('labeled_player_ball_tracking_full2.csv', index=False)

print("✅ تم حفظ البيانات الكاملة من الفيديو في: labeled_player_ball_tracking_full.csv")
