import pygame

def init():
    
    pygame.init()
    screen = pygame.display.set_mode((320,320))
    pygame.display.set_caption("Press for movement")


def getKey(pressed_key):
    pressed = False

    for event in pygame.event.get():
        # identifier = pygame.key.key_code(f"{pressed_key}")
        if event.type == pygame.KEYDOWN:
            print("A key was pressed")
            keys = pygame.key.get_pressed()
            print(f"The registered key in pygame is {pygame.key.name(event.key)}")
            if pygame.key.name(event.key) == pressed_key:
                print("And they are the same...")
                pressed = True



    return pressed

