#pip install turtle
#pip install math

import math
from turtle import *

color('red', 'green')
begin_fill()
while True:
    forward(200)
    left(170)
    #right(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
