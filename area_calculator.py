import math

while True:

    info = ("What do you want to do? Calculate the area (1-5) or exit (6)?")
    incorrect_choose = ("The option you selected does not exist. Try again")
    exit_message = ("See you soon...")

    print(info)
    action_choose = input(
        """1 - Square, 2 - Rectangle, 3 - Triangle, 4 - Circle, 5 - Trapeze, 6 - Exit program: """)

    if action_choose == "1":
        a = int(input("Edge length: "))

        if a <= 0:
            print("The lenght must be > 0")
            
        elif a > 0:
            def square_area(a):
                return (a * a)
            
            calculated_square_area = square_area(a)

            print("Rectangle area = ", calculated_square_area)

    elif action_choose == "2":
        a = int(input("First edge length: "))
        b = int(input("Second edge length: "))

        if a <= 0 or b <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and b > 0:
            def rectangle_area(a, b):
                return (a * b)
            
            calculated_rectangle_area = rectangle_area(a, b)

            print("Square area = ", calculated_rectangle_area)

    elif action_choose == "3":
        a = int(input("Base length: "))
        h = int(input("Height: "))

        if a <= 0 or h <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and h > 0:
            def triangle_area(a, h):
                return (0.5 * a * h)
            
            calculated_triangle_area = triangle_area(a, h)
            
            print("Triangle area = ", calculated_triangle_area)

    elif action_choose == "4":
        r = int(input("Radius: "))

        if r <= 0:
            print("The lenght must be > 0")
            
        elif r > 0:
            def circle_area(r):
                return (math.pi * (r ** 2))

            calculated_circle_area = circle_area(r)

            print ("Circle area = ", calculated_circle_area)

    elif action_choose == "5":
        a = int(input("First edge length: "))
        b = int(input("Second edge length: "))
        h = int(input("Height: "))

        if a <= 0 or b <=0 or h <=0:
            print("The lenght must be > 0")
            
        elif a > 0 and b > 0 and h > 0:
            def trapeze_area(a, b, h):
                return (a + b) / 2 * h
            
            calculated_trapeze_area = trapeze_area(a, b, h)

            print("Trapeze area = ", calculated_trapeze_area)
    
    elif action_choose == "6":
        print(exit_message)
        break

    else:
        print(incorrect_choose)