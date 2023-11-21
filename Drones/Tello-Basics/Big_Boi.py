import sys
import os
import djitellopy as tello
import time
import cv2
import logging
import pygame


tello = tello.Tello()
pygame.init()

tello.LOGGER.setLevel(logging.WARNING)

global img

tello.connect()
tello.streamon()

traj = [0,0,0,0]

screen = pygame.display.set_mode((320,320))
pygame.display.set_caption("Press for movement")

print("Battery level is: {}", tello.get_battery())

def keyPress(event, key_direction):
    # Up is 0 and down is 1
    if event.key == pygame.K_e:
        tello.takeoff()
    if event.key == pygame.K_x:
        tello.land()
    if event.key == pygame.K_w:
        traj[1] = 30*key_direction
    if event.key == pygame.K_a:
        traj[0] = 30*key_direction
    if event.key == pygame.K_s:
        traj[1] = 30*key_direction
    if event.key == pygame.K_d:
        traj[0] = 30*key_direction
    if event.key == pygame.K_j:
        traj[2] = 30*key_direction
    if event.key == pygame.K_k:
        traj[2] = 30*key_direction
    if event.key == pygame.K_q:
        pygame.quit()
        tello.end()
        exit

while True:
    img = tello.get_frame_read().frame
    img = cv2.resize(img, (360, 240))

    cv2.imshow("Drone Footage", img)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keyPress(event, 1)
        elif event.type == pygame.KEYUP:
            keyPress(event, 0)

    print(f"Trajectory is {traj}")
    tello.send_rc_control(traj[0], traj[1], traj[2], traj[3])
    time.sleep(0.1)

    

