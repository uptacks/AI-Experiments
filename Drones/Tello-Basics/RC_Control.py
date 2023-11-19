from djitellopy import tello
from time import sleep
tello = tello.Tello()
tello.connect()

tello.takeoff()
# tello.send_rc_control(0, 0, 50, 0) # Forward 50cm
sleep(0.1)
tello.send_rc_control(0, 0, 0, 0) # Stop
sleep(0.5)
tello.send_rc_control(0, 0, 0, 100) # Turn 90 deg to the right
sleep(2)
tello.send_rc_control(0, 0, 0, 0) # Stop
# sleep(2)
tello.land()