from flask import Flask, request, send_file, jsonify
import cv2
from io import BytesIO
from deepface import DeepFace as df
import numpy as np
import base64
import os

app = Flask(__name__)

@app.route('/emotion', methods=['GET'])
def get_emotion():
    response = []
    response.append(result['dominant_emotion'])
    print(response)
    return jsonify(response)

@app.route('/convert', methods=['POST'])
def convert_image():
    # Get the image data from the request
    file_storage = request.files['image']
    file_bytes = file_storage.read()

    # Decode the image data into a cv2 mat
    npimg = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)

    img = detectEmotion(img)

    # Convert the cv2 mat to a BytesIO object
    buffer = BytesIO()
    buffer.write(cv2.imencode('.jpg', img)[1].tobytes())

    # Send the BytesIO object to the client as a download
    buffer.seek(0)
    return send_file(buffer, mimetype='image/jpeg')

def detectEmotion(image):

    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    global result
    result = df.analyze(image, actions = ['emotion'], enforce_detection=False)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(image,
                str.upper(result['dominant_emotion']),
                (50,100),
                font, 3,
                (255, 255, 255),
                2,
                cv2.LINE_4)

    return image

if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)),host='0.0.0.0',debug=True)