import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

def getKey(keyName):
    ans = False
    for event in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    keyPressed = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[keyPressed]:
        ans = True
    pygame.display.update()
    return ans

if __name__ == "__main__":
    init()
    while True:
        pass