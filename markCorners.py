import cv2 
import numpy as np
import argparse

parser = argparse.ArgumentParser(description='Corner Detector')
parser.add_argument('-i', '--input', help='Path to input image.')
parser.add_argument('-fname', '--filename', help='The name of the new file, with counted corners')
args = parser.parse_args()

image = args.input
filename = args.filename

img = cv2.imread(image)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 27, 0.1, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 5, (0, 0, 225), -1)

cv2.imshow('img', img)
cv2.imwrite('./data/' + filename + '.png', img)
cv2.waitKey(0)
cv2.destroyAllWindows()