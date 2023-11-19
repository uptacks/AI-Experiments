import sys
import os
sys.path.append(os.path.join(sys.path[0],'Modules'))
import KeyPress as kp
import djitellopy as tello
import time
import cv2

kp.init()
tello = tello.Tello()

global img

tello.connect()
tello.streamon()

print("Battery level is: {}", tello.get_battery())

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("q"): tello.land(); time.sleep(3)

    if kp.getKey("e"): tello.takeoff()

    if kp.getKey("x"): kp.quit(); tello.end() 

    if kp.getKey("z"):
        cv2.imwrite(f'Resources/Images/{time.time()}.jpg', img)
        time.sleep(0.3)

    return [lr, fb, ud, yv]

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    cv2.imshow("Drone Footage", img)
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(0.1)

