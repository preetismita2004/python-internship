import math

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def get_circumference(self):
        return self.get_perimeter()

#taking input
x_input = float(input("Enter x-coordinate of the circle's center: "))
y_input = float(input("Enter y-coordinate of the circle's center: "))
radius_input = float(input("Enter the radius of the circle: "))

my_circle = Circle(x_input, y_input, radius_input)
print(f"Area of the circle: {my_circle.get_area()}")
print(f"Perimeter of the circle: {my_circle.get_perimeter()}")
print(f"Circumference of the circle: {my_circle.get_circumference()}")
