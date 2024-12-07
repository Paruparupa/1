# calcircum.py
from settings import PI

def triangle_circum(a, b, c):
    return a + b + c

def circle_circum(radius):
    return 2 * PI * radius

def rectangle_circum(length, width):
    return 2 * (length + width)