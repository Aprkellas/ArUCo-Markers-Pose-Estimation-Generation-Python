from flask import Flask
from detect_aruco_images_flask import *

app = Flask(__name__)


@app.route('/')
def homepage():
    return

@app.route('/image_selected')
def image_selected(image):
    image_decoded = detect(image)
    return image_decoded

if __name__ == '__main__':
    app.run()