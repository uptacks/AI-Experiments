import sys
import os
sys.path.append(os.path.join(sys.path[0],'Modules'))
import KeyPress as kp
import djitellopy as tello
import time

kp.init()
tello = tello.Tello()

tello.connect()

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

    if kp.getKey("Q"): kp.quit(); tello.end() 

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    time.sleep(0.05)

