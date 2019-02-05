# OpenCVTest_2.py

# this program opens a picam stream, attempts to change to 320x240 resolution,
# and shows the original image of each frame and also a Canny edges of each frame

import cv2
import numpy as np
import os
import time
os.system('sudo modprobe bcm2835-v4l2')
###################################################################################################
def main():

    my_camera = cv2.VideoCapture(0)         # declare a VideoCapture object and associate to webcam, 0 => use 1st webcam

                                            # show original resolution
    print "default resolution = " + str(my_camera.get(3)) + "x" + str(my_camera.get(4))

    my_camera.set(3, 320.0)              # change resolution to 320x240 for faster processing
    my_camera.set(4, 240.0)

                                            # show updated resolution
    print "updated resolution = " + str(my_camera.get(3)) + "x" + str(my_camera.get(4))

    if my_camera.isOpened() == False:               # check if VideoCapture object was associated to webcam successfully
        print "error: my_camera not accessed successfully\n\n"      # if not, print error message to std out
        os.system("pause")                                          # pause until user presses a key so user can see error message
        return                                                      # and exit function (which exits program)
    # end if

    while cv2.waitKey(1) != 27 and my_camera.isOpened():            # until the Esc key is pressed or webcam connection is lost
        blnFrameReadSuccessfully, imgOriginal = my_camera.read()            # read next frame

        if not blnFrameReadSuccessfully or imgOriginal is None:     # if frame was not read successfully
            print "error: frame not read from webcam\n"             # print error message to std out
            os.system("pause")                                      # pause until user presses a key so user can see error message
            break                                                   # exit while loop (which exits program)
        # end if

        imgGrayscale = cv2.cvtColor(imgOriginal, cv2.COLOR_BGR2GRAY)    # convert to grayscale

        imgBlurred = cv2.GaussianBlur(imgGrayscale, (5, 5), 0)          # blur

        imgCanny = cv2.Canny(imgBlurred, 100, 200)                      # get Canny edges

        cv2.namedWindow("imgOriginal", cv2.WINDOW_AUTOSIZE)        # create windows, use WINDOW_AUTOSIZE for a fixed window size
        cv2.namedWindow("imgCanny", cv2.WINDOW_AUTOSIZE)           # or use WINDOW_NORMAL to allow window resizing

        cv2.imshow("imgOriginal", imgOriginal)         # show windows
        cv2.imshow("imgCanny", imgCanny)
    # end while

    cv2.destroyAllWindows()                 # remove windows from memory

    return

###################################################################################################
if __name__ == "__main__":
    main()

