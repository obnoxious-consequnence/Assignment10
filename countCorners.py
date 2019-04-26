import cv2 
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Corner Detector')
parser.add_argument('--input', help='Path to input image.')
args = parser.parse_args()

filename = args.input

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 27, 0.1, 10)

print(corners.shape[0], 'corners in ', filename)
