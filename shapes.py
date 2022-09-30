import math

""" action_choose == 1 """
def square_area(a):
    return (a * a)

""" action_choose == 2 """
def rectangle_area(a, b):
    return (a * b)

""" action_choose == 3 """
def triangle_area(a, h):
    return (0.5 * a * h)

""" action_choose == 4 """
def circle_area(r):
    return (math.pi * (r ** 2))

""" action_choose == 5 """
def trapeze_area(a, b, h):
    return (a + b) / 2 * h