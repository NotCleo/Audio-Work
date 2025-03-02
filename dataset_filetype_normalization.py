import mimetypes
import os
import sys
from google.colab import files
from pydub import AudioSegment
from PIL import Image
import cv2

uploaded = files.upload() 
file_path = list(uploaded.keys())[0] 

mime_type, _ = mimetypes.guess_type(file_path)

if mime_type:
    if mime_type.startswith('audio'):
        audio = AudioSegment.from_file(file_path)
        output_path = os.path.splitext(file_path)[0] + ".wav"
        audio.export(output_path, format="wav")
        print(f"Converted to WAV: {output_path}")

    elif mime_type.startswith('image'):
        img = Image.open(file_path)
        output_path = os.path.splitext(file_path)[0] + ".jpg"
        img.convert("RGB").save(output_path, "JPEG")
        print(f"Converted to JPG: {output_path}")

    elif mime_type.startswith('video'):
        cap = cv2.VideoCapture(file_path)
        output_path = os.path.splitext(file_path)[0] + ".mp4"
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            out.write(frame)

        cap.release()
        out.release()
        print(f" Converted to MP4: {output_path}")

    else:
        print("Unsupported file type!")

else:
    print("Could not determine file type!")
