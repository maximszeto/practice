class Jump:
    def __init__(self, jumpHeight, date, time, pb): 
        self.jumpHeight = jumpHeight
        self.date = date
        self.time = time
        self.pb = pb


jump_height = input("how high did you jump: ")
date_of_jump = input("when did this happen?: ")
time_of_jump = input("what time did this jump happen?: ")
aPB = input("was this a pb? ")

jump1 = Jump(jump_height, date_of_jump, time_of_jump, aPB)

print(jump1.pb)