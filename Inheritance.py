# Inheritance in Python OOP

# Inheritance is a fundamental concept in object-oriented programming that allows a class to inherit attributes and methods from another class.

# The class that inherits is called the "derived class" or "subclass," while the class being inherited from is called the "base class" or "superclass."

# In Python, there are different types of inheritance:

# 1. Single Inheritance: In this type, a derived class inherits from a single base class.

# Example:
# Define the base class "Vehicle"
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print("The engine starts.")

# Define the derived class "Car" inheriting from "Vehicle"
class Car(Vehicle):
    def __init__(self, brand, color):
        super().__init__(brand)
        self.color = color

    def drive(self):
        print(f"The {self.color} car drives.")

    def honk(self):
        print("The car honks.")

# Create an instance of the "Car" class
car = Car("Toyota", "Red")

# Access and utilize the inherited attributes and methods from the base class
print(car.brand)  # Output: Toyota
car.start_engine()  # Output: The engine starts.

# Call the method specific to the derived class
car.drive()  # Output: The Red car drives.


# 2. Multiple Inheritance: In this type, a derived class can inherit from multiple base classes.

# Example:
# Define the base classes
class Engine:
    def start(self):
        print("The engine starts.")

class Doors:
    def open(self):
        print("The doors open.")

# Define the derived class "SedanCar" inheriting from both "Engine" and "Doors"
class SedanCar(Engine, Doors):
    def __init__(self, brand):
        self.brand = brand

# Create an instance of the "SedanCar" class
sedan = SedanCar("Honda")

# Access and utilize the inherited attributes and methods from the base classes
sedan.start()  # Output: The engine starts.
sedan.open()  # Output: The doors open.


# 3. Multilevel Inheritance: In this type, a derived class inherits from another derived class.

# Example:
# Define the base class "Shape"
class Shape:
    def draw(self):
        print("The shape is drawn.")

# Define the derived class "Rectangle" inheriting from "Shape"
class Rectangle(Shape):
    def area(self):
        print("The area of the rectangle is calculated.")

# Define the derived class "Square" inheriting from "Rectangle"
class Square(Rectangle):
    def perimeter(self):
        print("The perimeter of the square is calculated.")

# Create an instance of the "Square" class
square = Square()

# Access and utilize the inherited attributes and methods from the base classes
square.draw()  # Output: The shape is drawn.
square.area()  # Output: The area of the rectangle is calculated.
square.perimeter()  # Output: The perimeter of the square is calculated.


# These examples demonstrate different types of inheritance in Python OOP. Inheritance allows for code reuse, modularity, and extensibility, enabling efficient and organized development in object-oriented programming.
