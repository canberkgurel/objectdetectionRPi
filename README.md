# objectdetectionRPi
Detect the red ball using a Raspberry Pi and PiCam

For details, please visit: https://hackaday.io/project/9629/logs

# Part 1:

Download the OpenCVTest_1.py from the files.

This program opens the file in the same directory names "cam.jpg" and displays the original image and a Canny edges of the original image.

Just like we've done in the previous log, create a file called OpenCVTest1.py using the following command:
```
nano OpenCVTest1.py
```
Then copy/paste in OpenCVTest1.py and press CTRL+O and CTRL+X

(Now you should be back in the command line, if you're unsure about this stage, examine the log 6)

And execute the code using the following command.
```
python OpenCVTest1.py
```
P.s. the Pi camera comes with a protective cover on its lens, make sure that you've removed it otherwise you'd probably get a complete black picture instead of a canny edges of the original image.

# Part 2:

Download the OpenCVTest_2.1.py from the files.

This program opens a picam stream, attempts to change to 320x240 resolution, and shows the original image of each frame and also a Canny edges of each frame.

Now repeat the same process as the Part 1, create a file called OpenCVTest2.py using the following command:
```
nano OpenCVTest2.py
```
Then copy/paste in OpenCVTest2.py and press CTRL+O and CTRL+X

(Now you should be back in the command line, if you're unsure about this stage, examine the log 6)

And execute the code using the following command.
```
python OpenCVTest2.py
```
# Part 3:

Download the OpenCVTest_3.1.py from the files.

This program tracks a red ball and outputs its location in terms of coordinates.

Now repeat the same process as the Part 1, create a file called OpenCVTest3.py using the following command:
```
nano OpenCVTest3.py
```
Then copy/paste in OpenCVTest3.py and press CTRL+O and CTRL+X

(Now you should be back in the command line, if you're unsure about this stage, examine the log 6)

And execute the code using the following command.
```
python OpenCVTest3.py
```
