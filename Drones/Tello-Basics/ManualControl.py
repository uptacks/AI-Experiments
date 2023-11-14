import sys
import os
sys.path.append(os.path.join(sys.path[0],'Modules'))
import KeyPress as kp

kp.init()

while True:
    # Infinite loop lol sorry
    print(kp.getKey("LEFT"))

