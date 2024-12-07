# calarea.py
from settings import PI

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return PI * radius ** 2

def rectangle_area(length, width):
    return length * width