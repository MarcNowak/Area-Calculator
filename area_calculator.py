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

while True:

    info = ("What do you want to do?\nCalculate the area (1-5) or exit (6)?")
    incorrect_choose = ("The option you selected does not exist. Try again")
    exit_message = ("See you soon...")

    print(info)
    action_choose = input(
        """1 - Square\n2 - Rectangle\n3 - Triangle\n4 - Circle\n5 - Trapeze\n6 - Exit program\nYour choice: """)

    if action_choose == "1":
        a = float(input("Edge length: "))

        if a <= 0:
            print("The lenght must be > 0")
            
        elif a > 0:
            calculated_square_area = square_area(a)
            print("Square area = ", calculated_square_area)

    elif action_choose == "2":
        a = float(input("First edge length: "))
        b = float(input("Second edge length: "))

        if a <= 0 or b <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and b > 0:
            calculated_rectangle_area = rectangle_area(a, b)
            print("Rectangle area = ", calculated_rectangle_area)

    elif action_choose == "3":
        a = float(input("Base length: "))
        h = float(input("Height: "))

        if a <= 0 or h <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and h > 0:
            calculated_triangle_area = triangle_area(a, h)
            print("Triangle area = ", calculated_triangle_area)

    elif action_choose == "4":
        r = float(input("Radius: "))

        if r <= 0:
            print("The lenght must be > 0")
            
        elif r > 0:
            calculated_circle_area = circle_area(r)
            print ("Circle area = ", calculated_circle_area)

    elif action_choose == "5":
        a = float(input("First edge length: "))
        b = float(input("Second edge length: "))
        h = float(input("Height: "))

        if a <= 0 or b <=0 or h <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and b > 0 and h > 0:
            calculated_trapeze_area = trapeze_area(a, b, h)
            print("Trapeze area = ", calculated_trapeze_area)
    
    elif action_choose == "6":
        print(exit_message)
        break

    else:
        print(incorrect_choose)