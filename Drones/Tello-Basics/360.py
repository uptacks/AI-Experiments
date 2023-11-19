from djitellopy import tello
from time import sleep
tello = tello.Tello()
tello.connect()

tello.takeoff()
sleep(1.5)
tello.flip_right()
sleep(1.5)

# sleep(2)
tello.land()