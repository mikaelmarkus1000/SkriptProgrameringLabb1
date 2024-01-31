import module

while True:
    print("1. Find Divisible Numbers")
    print("2. Guess the Number Game")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = module.findDivibleNumbers(num1, num2)
        print(f"Resultat: {result}")  # Skriv ut resultaten från funktionen
    elif choice == 2:
        module.guessTheNumberGame()
    elif choice == 3:
        break
    else:
        print("Invalid Choice")
        continue
