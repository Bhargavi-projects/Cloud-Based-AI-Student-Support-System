import whisper
import os

audio_path = "audio/virtualization_lecture.wav"
output_path = "transcripts/lecture_text.txt"

# Create transcripts folder if not exists
os.makedirs("transcripts", exist_ok=True)

model = whisper.load_model("base")
result = model.transcribe(audio_path)

with open(output_path, "w") as f:
    f.write(result["text"])

print(" Transcription complete")