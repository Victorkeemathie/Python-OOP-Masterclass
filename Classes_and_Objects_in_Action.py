# 1. Classes
# A class is a user-defined data structure that serves as a blueprint for creating objects (instances) in Python.
# It defines the attributes (data) and methods (functions) that objects of the class will possess.
# Classes are defined using the "class" keyword followed by a descriptive name, typically starting with an uppercase letter.

# Example:
class Dog:
    # Class variable
    species = "Canine"

    # Constructor method
    def __init__(self, name):
        # Instance variable
        self.name = name

    # Method
    def bark(self):
        print("Woof!")

# 2. Instances
# Object instantiation refers to creating an object based on a class, also known as object construction.
# It allows you to create multiple objects (instances) from a single class.
# To create an instance, you call the class as if it were a function, and it returns a new object of that class.

# Example:
dog1 = Dog("Buddy")
dog2 = Dog("Max")

# 3. Attributes
# An attribute is a variable that defines the properties or characteristics of an object.
# There are two types of attributes: class attributes and instance attributes.
# Class attributes are shared by all objects of the class, while instance attributes are specific to each object.

# Example:
class Person:
    # Class attribute
    species = "Homo sapiens"  # Represents the species of all Person objects

    def __init__(self, name, age):
        # Instance attributes
        self.name = name  # Represents the name of each Person object
        self.age = age  # Represents the age of each Person object

# Create instances of the Person class
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Access and print the attributes of each instance
print(person1.name)  # Output: Alice
print(person2.age)  # Output: 30
print(Person.species)  # Output: Homo sapiens (accessing the class attribute)

# 4. Class Constructor
# The class constructor is a special method used to initialize the attributes of a class when creating objects.
# In Python, the constructor method is defined as __init__() and automatically called when creating a new instance.
# It takes the self parameter, which refers to the instance being created, along with any other desired parameters.

# Example:
class Rectangle:
    def __init__(self, width, height):
        # Instance attributes
        self.width = width  # Represents the width of each Rectangle object
        self.height = height  # Represents the height of each Rectangle object

# Create an instance of the Rectangle class
rectangle = Rectangle(5, 10)

# Access and print the attributes of the instance
print(rectangle.width)  # Output: 5
print(rectangle.height)  # Output: 10


# 5. Methods
# Methods are functions defined within a class that define the behaviors or actions of the objects.
# They can access and manipulate the object's attributes, perform calculations, or interact with other objects.

# Example:
class Circle:
    def __init__(self, radius):
        # Instance attribute
        self.radius = radius  # Represents the radius of each Circle object

    def calculate_area(self):
        # Method to calculate the area of the circle
        return 3.14 * self.radius * self.radius

# Create an instance of the Circle class
circle = Circle(5)

# Call the method on the instance to calculate the area
area = circle.calculate_area()

print(area)  # Output: 78.5


# 6. Multiple Objects
# In object-oriented programming, you can create multiple objects (instances) from a single class.
# Each object represents a separate instance of the class and has its own set of attribute values.

# Example:
class Book:
    def __init__(self, title, author):
        # Instance attributes
        self.title = title  # Represents the title of each Book object
        self.author = author  # Represents the author of each Book object

# Create multiple instances of the Book class
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")

# Access and print the attributes of each book
print(book1.title, "-", book1.author)  # Output: The Great Gatsby - F. Scott Fitzgerald
print(book2.title, "-", book2.author)  # Output: To Kill a Mockingbird - Harper Lee
