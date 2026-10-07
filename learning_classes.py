class Jump:
    def __init__(self, height, time, date,):
        self.height = height
        self.time = time
        self.date = date
"""
JumpHeight = input("How high did you jump?: ")
JumpTime = input("When did this jump happen?: ")
JumpDate = input("What day did this jump occur on?: ")


jump1 = Jump(JumpHeight, JumpTime, JumpDate)

print(f"You jumped {jump1.height} at {jump1.time} olock on {jump1.date}")
"""

class Arithmetic:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __eq__(self, other):
        return self.num1 == other.num1 and self.num2 == other.num2

    def __str__(self):
        sum = self.num1 + self.num2
        return f"{self.num1} + {self.num2} = {sum}"

    def add(self):
        self.num1 = self.num1 ** 2
        print(self.num1 + self.num2)  


answer = Arithmetic(4,2)
answer2 = Arithmetic(4,12)

print(answer)
print(answer2)
"""
if answer == answer2:
    print("same")
else:
    print("false")
"""

    