
def findDivibleNumbers(num1, num2):
    divibleNumbers = []
    for i in range(1, 1601):
        if i % num1 == 0 and i % num2 == 0:
            divibleNumbers.append(i)
    return divibleNumbers  # Resultatet returneras som en lista

def guessTheNumberGame():
    import random
    number = random.randint(1,60)

    while True:
        guess = int(input("Guess a number between 1 - 60: "))
        if guess > number:
            print("Wrong number! Too High")
        elif guess < number:
            print("Wrong Number! Too Low")
        else:
            print("You got it right!")
            break






