# Polymorphism in Python OOP

# Polymorphism is a fundamental concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass.

# It enables flexibility and extensibility by providing a consistent interface for objects with different implementations.

# Example 1: Polymorphism with method overriding

# Define the base class "Shape"
class Shape:
    def area(self):
        # Base implementation of the area method
        print("Calculating area")

# Define the derived class "Rectangle" inheriting from "Shape"
class Rectangle(Shape):
    def area(self):
        # Overriding the area method in the base class
        print("Calculating area of a rectangle")

# Define the derived class "Circle" inheriting from "Shape"
class Circle(Shape):
    def area(self):
        # Overriding the area method in the base class
        print("Calculating area of a circle")

# Create instances of the derived classes
rectangle = Rectangle()
circle = Circle()

# Call the area method on the objects
rectangle.area()  # Output: Calculating area of a rectangle
circle.area()  # Output: Calculating area of a circle


# Example 2: Polymorphism with different polymorphic functions

# Define a polymorphic function that accepts a Shape object
def calculate_area(shape):
    shape.area()  # Call the area method on the passed object

# Call the calculate_area function with different objects
calculate_area(rectangle)  # Output: Calculating area of a rectangle
calculate_area(circle)  # Output: Calculating area of a circle


# Example 3: Polymorphism with inheritance and method overriding

# Define the base class "Animal"
class Animal:
    def make_sound(self):
        # Base implementation of the make_sound method
        print("Generic animal sound")

# Define the derived classes "Dog" and "Cat" inheriting from "Animal"
class Dog(Animal):
    def make_sound(self):
        # Overriding the make_sound method in the base class
        print("Bark!")

class Cat(Animal):
    def make_sound(self):
        # Overriding the make_sound method in the base class
        print("Meow!")

# Create instances of the derived classes
dog = Dog()
cat = Cat()

# Call the make_sound method on the objects
dog.make_sound()  # Output: Bark!
cat.make_sound()  # Output: Meow!
