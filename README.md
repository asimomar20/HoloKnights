1- you have to download This model "Version 1.0" of SMPL-X.
2 - run extract_landmarks.py
3- run fit_smplxTEST.py



# 3D Juggle & Motion Fitting Pipeline



This repository provides a full pipeline for:

1. **Counting football juggles** in a video using YOLOv8 and MediaPipe  
2. **Extracting 3D body landmarks** per frame into a NumPy array  
3. **Fitting a parametric SMPL-X model** to those 3D landmarks (pose & shape) via SMPLify-X  
4. **Exporting a frame-by-frame OBJ sequence** ready for rendering or real-time playback  
5. **Import helpers** for Unity and Blender to visualize the reconstructed motion





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



