import pandas as pd

# استخدام الأسماء الفعلية للملفات الموجودة في مجلدك
df1 = pd.read_csv("labeled_player_ball_tracking_full.csv")
df2 = pd.read_csv("labeled_player_ball_tracking_full2.csv")

df_all = pd.concat([df1, df2], ignore_index=True)
df_all.to_csv("labeled_combined.csv", index=False)

print("✅ تم دمج الملفات بنجاح في labeled_combined.csv")
