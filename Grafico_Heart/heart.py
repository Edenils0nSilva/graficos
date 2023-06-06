#pip install turtle
#pip install math

import math
from turtle import *

def hearta(k):
    return 12*math.sin(k)**3
def heatb(k):
    return 12*math.cos(k)-5*\
    math.cos(2*k)-2*\
                math.cos(3*k)-\
                math.cos(4*k)

    speed(20)
bgcolor("purple")
for i in range(1000):
        goto(hearta(i)*20, heatb(i)*20)
        for j in range(5):
            
            color("black")
        goto(0,0)
        done