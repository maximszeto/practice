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

    def add(self, num1, num2):
        print(num1 + num2)  


answer = Arithmetic(8,9)
answer.add(9,8)