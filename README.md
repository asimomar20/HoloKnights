1- you have to download This model "Version 1.0" of SMPL-X.
2 - run extract_landmarks.py
3- run fit_smplxTEST.py



# 3D Juggle & Motion Fitting Pipeline



---

## 🔍 Overview

1. **Detect & Count Juggles**  
   - Uses YOLOv8 + MediaPipe to count total juggles, attempts, average, best/worst, and preferred foot.  
2. **Extract 3D Landmarks**  
   - Runs MediaPipe Pose to capture 33 body landmarks per frame → saved as `landmarks3d.npy`.  
3. **Fit SMPL-X (SMPLify-X)**  
   - Optimizes SMPL-X pose & shape to match each frame’s 3D landmarks, exports per-frame OBJ meshes.  
4. **Visualize in Unity & Blender**  
   - Unity C# helper to load OBJ sequence as real-time animation.  
   - Blender import script for high-quality offline render.

---









```text

├── models/  
│   └── smplx_v1_1/          # ملفات NPZ/PKL الخاصة بـ SMPL-X
├── scripts/
│   ├── detect_juggles.py    # YOLOv8 + MediaPipe: عدّ الـ juggles + القدم المفضّلة
│   ├── extract_landmarks.py # استخراج numpy / .npy للـ 33 وجه جسمي ثلاثي الأبعاد
│   ├── fit_smplifyx.py      # SMPLify-X fitting loop، يصدر ملفات OBJ
│   └── unity_import.cs      # C# script لعرض الـ OBJ sequence كـ animation
├── sample.mp4               # مثال فيديو للاعب
├── landmarks3d.npy          # ناتج extract_landmarks.py
├── LICENSE
└── README.md



