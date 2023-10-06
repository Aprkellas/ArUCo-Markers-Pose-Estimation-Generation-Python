'''
Sample Command:-
python detect_aruco_images.py --image Images/test_image_1.png --type DICT_5X5_100
'''
# import numpy as np
from utils import ARUCO_DICT, aruco_display
import argparse
import cv2
import sys


def detect(image_path):
    print("Loading image...")
    image = cv2.imread(image_path)
    h, w, _ = image.shape
    width = 600
    height = int(width * (h / w))
    image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)
    detected = False
    detected_markers = None  # Initialize to None

    for tag_type, aruco_dict_value in ARUCO_DICT.items():
        if not detected:
            try:
                # Load the ArUco dictionary, grab the ArUco parameters, and detect the markers
                print(f"Detecting '{tag_type}' tags...")
                arucoDict = cv2.aruco.getPredefinedDictionary(aruco_dict_value)
                arucoParams = cv2.aruco.DetectorParameters()
                corners, ids, rejected = cv2.aruco.detectMarkers(image, arucoDict, parameters=arucoParams)

                if len(corners) > 0:
                    detected_markers, detected = aruco_display(corners, ids, rejected, image)

            except Exception as e:
                print(f"Error detecting '{tag_type}' tags: {e}")

    return detected_markers