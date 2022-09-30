import math

print("The area of which figure you want to calculate:")
action_choose = input(
    """1 - Square, 2 - Rectangle, 3 - Triangle, 4 - Circle, 5 - Trapeze: """)

if action_choose == "1":
    a = int(input("Edge length: "))

    def square_area(a):
        return (a * a)

    print("Rectangle area = ", square_area(a))

elif action_choose == "2":
    a = int(input("First edge length: "))
    b = int(input("Second edge length: "))

    def rectangle_area(a, b):
        return (a * b)

    print("Square area = ", rectangle_area(a, b))

elif action_choose == "3":
    a = int(input("Base length: "))
    h = int(input("Height: "))

    def triangle_area(a, h):
        return (0.5 * a * h)
    
    print("Triangle area = ", triangle_area(a, h))

elif action_choose == "4":
    r = int(input("Radius: "))

    def circle_area(r):
        return (math.pi * (r ** 2))

    print ("Circle area = ", circle_area(r))

elif action_choose == "5":
    a = int(input("First edge length: "))
    b = int(input("Second edge length: "))
    h = int(input("Height: "))

    def trapeze_area(a, b, h):
        return (a + b) / 2 * h

    print("Trapeze area = ", trapeze_area(a, b, h))

else:
    print("Select correct option 1 - 5")