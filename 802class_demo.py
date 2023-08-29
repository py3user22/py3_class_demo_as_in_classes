#!/bin/python3


"""New Class demo  """


class Dog:
    # simple class attributes/variable
    animal = "dog"
    attr1 = "mammal"
    attr2 = "dog"

    # sample method
    def fun(self):
        print("Im a", self.attr2)       # Im a dog
        print("{}s are {}s".format(self.attr2, self.attr1))
# create a object
Pepper = Dog()

print(Pepper.attr2)         # dog
Pepper.fun()                # Im a dog    # dogs are mammals

# --------------------

class JGG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    # used to define how a class object should be represented as a string
    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."

    # sample method with a print
#    def show(self):
#         print("\nHello my name is " + self.name + " and I work in " + self.company + ".")

# obj = Class( name, company)
obj1 = JGG("Jesus", "Daulmage")
print(obj1)
# obj1.show()

# ---------------------------

class Person:

    # init method aka constructor
    def __init__(self, name):
        self.name = name

    # simple method
    def say_hi(self):
        print("Hello, my name is", self.name)

p = Person("Jesus")
p.say_hi()

# -----------------------

"""__str__(). that is used to define how a class object should be represented as a string.
"""


