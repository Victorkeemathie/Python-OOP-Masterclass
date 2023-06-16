# Data Abstraction in Python involves hiding the internal details and complexity of a class, and exposing only essential information to the outside world.

# Example: Creating an abstract base class
from abc import ABC, abstractmethod

# Define an abstract base class called Shape
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Create a class called Rectangle that inherits from Shape
class Rectangle(Shape):
    def area(self):
        # Calculate and return the area of the rectangle
        return self.width * self.height

# Create a class called Circle that inherits from Shape
class Circle(Shape):
    def area(self):
        # Calculate and return the area of the circle
        return 3.14 * self.radius ** 2

# Instantiate objects of the derived classes
rectangle = Rectangle()
circle = Circle()

# Call the area method on the objects
rectangle.area()  # Output: Area of the rectangle
circle.area()  # Output: Area of the circle
