class Jump:
    def __init__(self, height, time, date,):
        self.height = height
        self.time = time
        self.date = date

while JumpHeight != "banana": 
    JumpHeight = input("How high did you jump?: ")
    JumpTime = input("When did this jump happen?: ")
    JumpDate = input("What day did this jump occur on?: ")

jump1 = Jump(JumpHeight, JumpTime, JumpDate)

print(f"You jumped {jump1.height} at {jump1.time} olock on {jump1.date}")
