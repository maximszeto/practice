"""
class Jump:
    def __init__(self, height, time, date,):
        self.height = height
        self.time = time
        self.date = date
JumpHeight = input("How high did you jump?: ")
JumpTime = input("When did this jump happen?: ")
JumpDate = input("What day did this jump occur on?: ")


jump1 = Jump(JumpHeight, JumpTime, JumpDate)

print(f"You jumped {jump1.height} at {jump1.time} olock on {jump1.date}")

class Arithmetic:
    def __init__(self, num1, num2, sign):
        self.num1 = num1
        self.num2 = num2
        self.sign = sign

    def __eq__(self, other):
        return self.num1 == other.num1 and self.num2 == other.num2

    def __str__(self):
        if self.sign == "+":
            answer = self.add() 
            return f"{self.num1} + {self.num2} = {answer}"
        
        elif self.sign == "-":
            answer = self.subtract()
            return f"{self.num1} - {self.num2} = {answer}"

        elif self.sign == "*":
            answer = self.multiply() 
            return f"{self.num1} * {self.num2} = {answer}"

        elif self.sign == "/":
            answer = self.divide() 
            return f"{self.num1} / {self.num2} = {answer}"

        else:
            return f"{self.sign} is not a sign"

    def add(self):
        return self.num1 + self.num2 
    
    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2

answer = Arithmetic(4,2, "+")
answer2 = Arithmetic(1,5, "+")

print(answer)
print(answer2)

if answer == answer2:
    print("same")
else:
    print("false")
"""
"""
import pet

# Here, we create an instance (an object) of the Pet class
my_dog = pet.Pet("Douglass", "Dog")
my_cat = pet.Pet("Mr. Pickles", "cat")

# Let's print out its attributes
print(f"My pet's name is {my_dog.name} and he is a {my_dog.species}.")
print(f"Starting energy: {my_dog.energy}")
print(f"My cat's name is {my_cat.name} and he is a {my_cat.species}")
print(f"Starting energy: {my_cat.energy}")
# Make the pet do something
for i in range(10):
    my_dog.feed()

for i in range(4):
    my_cat.feed()

"""

import someClasses
