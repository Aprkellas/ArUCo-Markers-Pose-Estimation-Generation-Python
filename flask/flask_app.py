from flask import Flask, render_template, request, Response
from detect_aruco_images_flask import *
import cv2
import numpy as np
import io


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/detect', methods=['POST'])
def image_selected():
    if request.method == 'POST':
        # Assuming the selected image is sent as a POST request
        uploaded_image = request.files['image']

        if uploaded_image:
            # Perform detection
            detected_image = detect(uploaded_image)

            # Convert the detected image to a response
            retval, buffer = cv2.imencode('.jpg', detected_image)
            response = Response(buffer.tobytes(), content_type="image/jpeg")
            return response
        
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)