import cv2
import numpy as np


img = cv2.imread("image.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

size_y = img.shape[0]
size_x = img.shape[1]

flattened = img.reshape([size_x*size_y])

from matplotlib import pyplot as plt
rhist,_ ,_ = plt.hist(flattened, bins=256)
plt.show()

rhist,_ ,_ = plt.hist(flattened, bins=32)
plt.show()
rhist,_ ,_ = plt.hist(flattened, bins=8)
plt.show()