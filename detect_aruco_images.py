'''
Sample Command:-
python detect_aruco_images.py --image Images/test_image_1.png --type DICT_5X5_100
'''
# import numpy as np
from utils import ARUCO_DICT, aruco_display
import argparse
import cv2
import sys


def detect(image_path, type,):

	print("Loading image...")
	image = cv2.imread(image_path)
	h,w,_ = image.shape
	width=600
	height = int(width*(h/w))
	image = cv2.resize(image, (width, height), interpolation=cv2.INTER_CUBIC)


	# verify that the supplied ArUCo tag exists and is supported by OpenCV
	if ARUCO_DICT.get(type, None) is None:
		print(f"ArUCo tag type '{type}' is not supported")
		sys.exit(0)

	# load the ArUCo dictionary, grab the ArUCo parameters, and detect
	# the markers
	print("Detecting '{}' tags....".format(type))
	arucoDict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_100)
	arucoParams = cv2.aruco.DetectorParameters()
	detector = cv2.aruco.ArucoDetector(arucoDict, arucoParams)
	corners, ids, rejected = detector.detectMarkers(
				image)
	detected_markers = aruco_display(corners, ids, rejected, image)
	cv2.imshow("Image", detected_markers)

	# # Uncomment to save
	# cv2.imwrite("output_sample.png",detected_markers)

	cv2.waitKey(0)