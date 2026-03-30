import whisper
import os

# 加载模型（base 模型，速度快）
model = whisper.load_model("base")

# 你的音频路径（保持不变）
audio_path = r"C:\Users\1\Desktop\3月30日.mp3"

# 开始识别（去掉 language="zh"，让模型自动检测）
result = model.transcribe(audio_path)

# 输出结果
print("===== 语音识别结果 =====")
print(result["text"])

# 保存到文件
with open("result.txt", "w", encoding="utf-8") as f:
    f.write(result["text"])
