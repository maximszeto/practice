userInput = input("Input text: ")

def calculate(text):
    characters = 0
    words = 1
    letterE = 0
    for char in text:
        if char == "e" or char == "E":
            letterE += 1

        elif char == " ":
            words += 1
        
        characters += 1

    if characters == 0:
        print("please input some text dude")
        return

    else:
        print(f"There are {characters} characters in that text")

    
    print(f"There are {words} words in that text")

    if letterE == 0:
        print("there are no E's in this text")
    
    elif letterE == 1:
        print(f"There is 1 e in that text")
    else:
        print(f"There are {letterE} e's in that text")

calculate(userInput)

def main():
    for i in range(21):
        print(f"{i}.")

main()