# Encapsulation in Python OOP

# Encapsulation is a fundamental concept in object-oriented programming that involves bundling data and methods together within a class.

# It aims to restrict access to the internal state of an object and provide controlled access through methods, promoting data hiding and abstraction.

# By encapsulating data, we can protect it from being modified directly and ensure that it is accessed and modified only through designated methods.

# Example 1: Encapsulation using access modifiers

class Person:
    def __init__(self, name, age):
        self._name = name  # Protected encapsulated attribute
        self._age = age  # Protected encapsulated attribute

    def get_name(self):
        # Getter method to access the encapsulated attribute
        return self._name

    def set_name(self, name):
        # Setter method to modify the encapsulated attribute
        self._name = name

    def get_age(self):
        # Getter method to access the encapsulated attribute
        return self._age

    def set_age(self, age):
        # Setter method to modify the encapsulated attribute
        self._age = age

# Create an instance of the Person class
person = Person("Alice", 25)

# Access and modify encapsulated attributes using getter and setter methods
print(person.get_name())  # Output: Alice
person.set_name("Bob")
print(person.get_name())  # Output: Bob

print(person.get_age())  # Output: 25
person.set_age(30)
print(person.get_age())  # Output: 30

# Example 2: Encapsulation with private attributes

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private encapsulated attribute
        self.__balance = balance  # Private encapsulated attribute

    def get_balance(self):
        # Getter method to access the encapsulated attribute
        return self.__balance

    def deposit(self, amount):
        # Method to deposit money and modify the encapsulated attribute
        self.__balance += amount

    def withdraw(self, amount):
        # Method to withdraw money and modify the encapsulated attribute
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

# Create an instance of the BankAccount class
account = BankAccount("1234567890", 1000)

# Access and modify encapsulated attribute using getter and method
print(account.get_balance())  # Output: 1000
account.deposit(500)
print(account.get_balance())  # Output: 1500

account.withdraw(200)
print(account.get_balance())  # Output: 1300

account.withdraw(2000)  # Output: Insufficient funds.

# Getters and Setters

# Getters and setters are methods that allow controlled access to encapsulated attributes.

# A getter is a method used to retrieve the value of an attribute.

# A setter is a method used to modify the value of an attribute.

# By using getters and setters, we can enforce rules, perform validation, or apply additional logic when accessing or modifying attributes.

# Example:

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        # Getter method to access the encapsulated attribute
        return self.__radius

    def set_radius(self, radius):
        # Setter method to modify the encapsulated attribute
        if radius > 0:
            self.__radius = radius
        else:
            print("Invalid radius value.")

# Create an instance of the Circle class
circle = Circle(5)

# Access the encapsulated attribute using a getter
print(circle.get_radius())  # Output: 5

# Modify the encapsulated attribute using a setter
circle.set_radius(10)
print(circle.get_radius())  # Output: 10

circle.set_radius(-2)  # Output: Invalid radius value.
print(circle.get_radius())  # Output: 10

