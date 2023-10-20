from random import randint


def game():
    lives = 0
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    number = randint(1, 100)
    #print(f"Psst, the correct answer is {number}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard'.")
    if difficulty == "easy":
        lives = 10
    elif difficulty == "hard":
        lives = 5
    print(f"You have {lives} attempt to guess the number.")
    guessed = False
    while not guessed and lives > 0:
        guess = int(input("Make a guess: "))
        if guess > number:
            print("Too high.\nGuess again.")
            print(f"You have {lives - 1} attempts remaining to guess the number.")
            lives -= 1
        elif guess < number:
            print("Too low.\nGuess again.")
            print(f"You have {lives - 1} attempts remaining to guess the number.")
            lives -= 1
        elif guess == number:
            print(f"You got it! The answer was {number}.")
            guessed = True
        if lives == 0:
            print("You've run out of lives. You lose!")


game()
