# Object-Oriented Programming (OOP) in Python

# Classes: A class is a blueprint for creating objects. 
# It defines a set of attributes (data) and methods (functions) that the objects created from the class will possess.

# Objects: An object is an instance of a class. It represents a specific entity with its own unique set of attributes and behaviors.

# Encapsulation: Encapsulation is the practice of bundling data and methods together within a class, hiding the 
# internal details of the object and providing an interface to interact with it. It helps in achieving data abstraction and data protection.

# Inheritance: Inheritance is a mechanism that allows a class to inherit the attributes and methods of another class, known as the base or parent class. 
# The derived or child class can add or modify the inherited behavior.

# Polymorphism: Polymorphism refers to the ability of objects of different classes to be used interchangeably based on their common interface. 
# It allows objects to be treated as instances of their own class or any of their parent classes.

# Method Overriding: Method overriding is a feature of inheritance where a derived class provides its own implementation of a method defined in the base class. 
# It allows a subclass to modify the behavior of an inherited method.

# Method Overloading: Python does not support method overloading by default. However, you can achieve similar behavior by using default argument values or 
# using variable arguments.

# Example:

# Define a class called "Car"
class Car:
    # Define the constructor method with parameters "make" and "model"
    def __init__(self, make, model):
        # Set the "make" attribute of the object to the value of the "make" parameter
        self.make = make
        # Set the "model" attribute of the object to the value of the "model" parameter
        self.model = model

    # Define a method called "start_engine"
    def start_engine(self):
        # Print a message indicating that the engine has started
        print("Engine started.")

    # Define a method called "stop_engine"
    def stop_engine(self):
        # Print a message indicating that the engine has stopped
        print("Engine stopped.")

# Create an instance of the Car class with the make "Toyota" and model "Camry" and assign it to the variable "my_car"
my_car = Car("Toyota", "Camry")

# Print the value of the "make" attribute of the "my_car" object
print(my_car.make)  # Output: Toyota

# Call the "start_engine" method of the "my_car" object
my_car.start_engine()  # Output: Engine started.

# This example demonstrates the creation of a Car class with attributes make and model, and 
# methods start_engine() and stop_engine(). The __init__ method is the constructor that is automatically called when a new object is created.

# This is just a basic overview of OOP in Python. There is much more to learn and explore, such as class inheritance, method overriding,
# and advanced topics like abstract classes and interfaces.



# Alternatives to OOP:

# Procedural Programming: Procedural programming focuses on writing procedures or functions that perform specific tasks and manipulate data.
# It emphasizes the use of procedures, variables, and control structures to achieve the desired outcome.
# Procedural programming is typically used for tasks where the data and functions are closely related and does not emphasize the use of objects and their interactions like OOP does.

# Functional Programming: Functional programming treats computation as the evaluation of mathematical functions and avoids changing state and mutable data.
# It emphasizes the use of pure functions that do not have side effects and focuses on the transformation of data through function composition and recursion.
# Functional programming languages often provide higher-order functions, immutability, and referential transparency.

# Event-Driven Programming: Event-driven programming focuses on the flow of events and the responses triggered by those events.
# It typically involves creating event handlers and callbacks that respond to user actions or system events.
# This paradigm is commonly used in graphical user interfaces (GUIs) and other systems that require event handling, such as web applications.

# Aspect-Oriented Programming: Aspect-Oriented Programming (AOP) aims to modularize cross-cutting concerns that span multiple components or modules in a system.
# It introduces the concept of aspects, which encapsulate common functionalities that can be applied to multiple parts of the codebase.
# AOP enables separation of concerns and helps to manage code complexity.

# Declarative Programming: Declarative programming focuses on specifying what needs to be accomplished, rather than how to achieve it.
# It involves defining constraints, rules, or logic that describe the desired outcome, and a runtime system takes care of executing the code to satisfy those constraints.
# Examples of declarative programming include SQL (Structured Query Language) for database queries and Prolog for logical programming.

# These programming paradigms are not mutually exclusive, and many programming languages allow for a mix of different paradigms.
# Choosing the right paradigm depends on the nature of the problem, the requirements of the project, and personal preference.
# It's common for developers to use a combination of paradigms to address different aspects of their projects.

