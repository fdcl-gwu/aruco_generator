import cv2
import numpy as np
import matplotlib.pyplot as plt

import cv2.aruco as aruco

# Select type of aruco marker (size)
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_1000)
print(aruco_dict)
# second param is ID number
# last param is total image size

# Create an image from the marker
for ii in range(4):
    img = aruco.drawMarker(aruco_dict, ii+1, 700)

    # create the image in matplotlib
    fig = plt.figure(frameon=False)
    fig.set_size_inches(6,6)

    # make content fill whole figure
    ax = plt.Axes(fig, [0, 0, 1, 1]) 
    ax.set_axis_off()
    fig.add_axes(ax)

    ax.imshow(img, cmap='Greys_r')
    plt.savefig('aruco' + str(ii+1) + '.pdf')

plt.show()
# Display the image to us
#cv2.imshow('frame', img)
# Exit on any key
# cv2.waitKey(0)
# cv2.destroyAllWindows()
