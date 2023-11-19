import cv2
from djitellopy import tello
from time import sleep

# Connect to Tello
tello = tello.Tello()
tello.connect()

tello.stream_on() # Start the video stream  

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Drone Footage", img)
    cv2.waitKey(1) # 1ms delay to prevent freezing