from djitellopy import tello
from time import sleep

# Connect to Tello
tello = tello.Tello()
tello.connect()

print(tello.get_battery())