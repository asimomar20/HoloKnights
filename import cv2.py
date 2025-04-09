import cv2
import mediapipe as mp
from ultralytics import YOLO

# تحميل النموذج المدرب من YOLO (يمكنك استخدام yolov8n.pt لأداء أسرع)
model = YOLO("yolov8n.pt")  # أو yolov8s.pt للدقة الأفضل

# فيديو
video_path = 'mixkit-2.mp4'
cap = cv2.VideoCapture(video_path)

# MediaPipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 1. تتبع اللاعب باستخدام MediaPipe
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)
    if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # 2. تتبع الكرة باستخدام YOLO
    results_yolo = model.predict(source=frame, conf=0.5, classes=[32], verbose=False)  # class 32 = sports ball

    for r in results_yolo:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
            cv2.putText(frame, "Ball", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,255), 2)

    # عرض
    cv2.imshow("Player + Ball Tracking", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
