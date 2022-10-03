import shapes
from enum import IntEnum

Menu_Shapes = IntEnum('Menu_Shapes', 'Square, Rectangle, Triangle, Circle, Trapeze, Exit program')

while True:

    info = ("What do you want to do?\nCalculate the area (1-5) or exit (6)?")
    incorrect_choose = ("The option you selected does not exist. Try again")
    exit_message = ("See you soon...")

    print(info)
    action_choose = int(input(
"""
1 - Square
2 - Rectangle
3 - Triangle
4 - Circle
5 - Trapeze
6 - Exit program

Your choice: """))

    if (action_choose == Menu_Shapes.Square):
        a = float(input("Edge length: "))

        if a <= 0:
            print("The lenght must be > 0")
            
        elif a > 0:
            calculated_square_area = shapes.square_area(a)
            print("Square area = ", calculated_square_area)

    elif (action_choose == Menu_Shapes.Rectangle):
        a = float(input("First edge length: "))
        b = float(input("Second edge length: "))

        if a <= 0 or b <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and b > 0:
            calculated_rectangle_area = shapes.rectangle_area(a, b)
            print("Rectangle area = ", calculated_rectangle_area)

    elif (action_choose == Menu_Shapes.Triangle):
        a = float(input("Base length: "))
        h = float(input("Height: "))

        if a <= 0 or h <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and h > 0:
            calculated_triangle_area = shapes.triangle_area(a, h)
            print("Triangle area = ", calculated_triangle_area)

    elif (action_choose == Menu_Shapes.Circle):
        r = float(input("Radius: "))

        if r <= 0:
            print("The lenght must be > 0")
            
        elif r > 0:
            calculated_circle_area = shapes.circle_area(r)
            print ("Circle area = ", calculated_circle_area)

    elif (action_choose == Menu_Shapes.Trapeze):
        a = float(input("First edge length: "))
        b = float(input("Second edge length: "))
        h = float(input("Height: "))

        if a <= 0 or b <=0 or h <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and b > 0 and h > 0:
            calculated_trapeze_area = shapes.trapeze_area(a, b, h)
            print("Trapeze area = ", calculated_trapeze_area)
    
    elif (action_choose == Menu_Shapes.Exit):
        print(exit_message)
        break

    else:
        print(incorrect_choose)