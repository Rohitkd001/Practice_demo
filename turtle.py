import random
import pyautogui as pg
import time
animal=('jaan','pagal','sravs')
time.sleep(10)
for i in range(100):
    a= random.choice(animal)
    pg.write("you are my "+a)
    pg.press("enter")
