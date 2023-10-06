'''
Sample Command:-
python detect_aruco_images.py --image Images/test_image_1.png --type DICT_5X5_100
'''
# import numpy as np
from utils import ARUCO_DICT, aruco_display
import argparse
import cv2
import sys
import tempfile
import os


def detect(uploaded_image):
    try:
        # Create a temporary directory to store the uploaded image
        with tempfile.TemporaryDirectory() as temp_dir:
            # Generate a temporary file path
            temp_image_path = os.path.join(temp_dir, "uploaded_image.jpg")

            # Save the uploaded image to the temporary file
            uploaded_image.save(temp_image_path)

            # Read the image using cv2.imread
            image = cv2.imread(temp_image_path)

            if image is not None:
                print("Loading image...")
                h, w, _ = image.shape
                width = 600
                height = int(width * (h / w))
                image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
                detected = False
                detected_markers = None

            for tag_type, aruco_dict_value in ARUCO_DICT.items():
                if not detected:
                    try:
                        # Load the ArUco dictionary, grab the ArUco parameters, and detect the markers
                        print(f"Detecting '{tag_type}' tags...")
                        arucoDict = cv2.aruco.getPredefinedDictionary(aruco_dict_value)
                        arucoParams = cv2.aruco.DetectorParameters()
                        detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
                        corners, ids, rejected =  detector.detectMarkers(
                        image)

                        if len(corners) > 0:
                            detected_markers, detected = aruco_display(corners, ids, rejected, image)

                    except Exception as e:
                        print(f"Error detecting '{tag_type}' tags: {e}")

            return detected_markers
        
    except Exception as e:
        print(f"error: {e}")
        return None