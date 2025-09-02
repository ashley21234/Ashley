# Ashely
#R246254H

#QUESTION 1
# Base class
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def start_engine(self):
        print(f"The engine of the {self.brand} vehicle starts with a generic rumble.")

# Subclass: Car
class Car(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} car's engine starts with a smooth purr and dashboard lights up.")

# Subclass: Bike
class Bike(Vehicle):
    def start_engine(self):
        print(f"The {self.brand} bike's engine starts with a loud roar and a twist of the throttle.")





#QUESTION 2
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def describe(self):
        return f"This is a vehicle made by {self.brand}, model {self.model}."


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def describe(self):
        return f"This is a car: {self.brand} {self.model} with {self.doors} doors."


class Bike(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def describe(self):
        return f"This is a {self.type_of_bike} bike: {self.brand} {self.model}."



#QUESTION 3
class Shape:
    def __init__(self):
        print("Shape initialized")

    def calculate_area(self):
        pass  # Base method does nothing

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()  # Call Shape's constructor
        self.width = width
        self.height = height

    def calculate_area(self):
        super().__init__()  # Demonstrating super() in method (though unusual here)
        return self.width * self.height

# Example usage
rect = Rectangle(5, 10)
print("Rectangle area:", rect.calculate_area())



#QUESTION 4
# Define the Dog class
class Dog:
    def make_sound(self):
        return "Woof!"

# Define the Cat class
class Cat:
    def make_sound(self):
        return "Meow!"

# Function that processes any object with a make_sound method
def process_sound(sound_object):
    print(sound_object.make_sound())

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call process_sound with both objects
process_sound(dog)  # Output: Woof!
process_sound(cat)  # Output: Meow!


#QUESTION 5
from abc import ABC, abstractmethod

class FileHandler(ABC):
    @abstractmethod
    def read(self, filepath):
        pass

    @abstractmethod
    def write(self, filepath, data):
        pass




