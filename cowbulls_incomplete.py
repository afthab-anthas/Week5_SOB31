import random

def compare_numbers(number, user_guess):
    cows = 0
    bulls = 0
    for i in range(len(number)):
        if user_guess[i] == number[i]:
            bulls += 1  # Correct digit in correct position
        elif user_guess[i] in number:
            cows += 1  # Correct digit in incorrect position
    return cows, bulls


playing = True
number = str(random.randint(1000, 9999))
guesses = 0
print(number)  # You might want to hide this in the final version for gameplay!

print("Let's play a game of Cowbull!")  # Explanation
print("I will generate a number, and you have to guess the numbers one digit at a time.")
print("For every digit that exists in the sequence but is in the wrong place, you get a cow. "
      "For every digit in the correct place, you get a bull.")
print("The game ends when you get 4 bulls!")
print("Type 'exit' at any prompt to exit.")

while playing:
    user_guess = input("Give me your best guess: ")
    if user_guess.lower() == "exit":
        break

    if len(user_guess) != 4 or not user_guess.isdigit():
        print("Invalid input. Please enter a 4-digit number.")
        continue

    cowbullcount = compare_numbers(number, user_guess)
    guesses += 1

    print("You have " + str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")

    if cowbullcount[1] == 4:
        print("You win the game after " + str(guesses) + " guesses! The number was " + str(number))
        break  # Stop the game
    else:
        print("Your guess isn't quite right, try again.")