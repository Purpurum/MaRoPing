import base64
from flask import Flask, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
from ultralytics import YOLO
import pandas as pd
import cv2
import io
YOLO_VERBOSE=False

import easyocr

from modules.processor import process_image

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/api/button', methods=['POST'])
def button_action():
    data = request.json  # Получаем данные из запроса
    # Обработка данных
    response_data = {"status": "success", "received_data": data}
    return jsonify(response_data)

@app.route('/api/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({"status": "error", "message": "No file part"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"status": "error", "message": "No selected file"}), 400

    filename = secure_filename(file.filename)
    original_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(original_path)

    text_data, processed_image_io  = process_image(original_path, detector_code=detector_code, detector_art=detector_art, reader=reader, articules=articules)
    _, processed_img_encoded = cv2.imencode('.jpg', processed_image_io)
    processed_img_io = io.BytesIO(processed_img_encoded.tobytes())

    _, processed_img_encoded = cv2.imencode('.jpg', processed_image_io)
    processed_img_io = io.BytesIO(processed_img_encoded.tobytes())

    img = base64.b64encode(processed_img_io.read()).decode('utf-8')

    response_data = {
        "status": "success",
        "filename": filename,
        "text_data": text_data,
        "img": img 
    }

    return jsonify(response_data)

reader = easyocr.Reader(lang_list=['ru'],
                        model_storage_directory="modules/models",
                        user_network_directory="modules/models",
                        recog_network='custom_ocr',
                        detector=False,
                        gpu=False,
                        )
detector_code = YOLO("modules/models/yolo11_code_nano.pt")
detector_art = YOLO("mmodules/odels/yolo11_art_nano.pt")

db_path = "ДеталиПоПлануДляРазрешенныхЗаказов.xlsx"
df = pd.read_excel(db_path, engine='openpyxl')

articules = df["ДетальАртикул"].dropna().unique()

if __name__ == '__main__':
    app.run(host='192.168.0.4',port=9871) #Это локальный IP и порт