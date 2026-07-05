import random
number = random.randint(1, 100)
 
while True:
    guess= int(input("Guess a number between 1 and 100:"))

    if guess < number:
        print("TOO LOW! Guess again.")
    elif guess > number:
        print("TOO HIGH ! Guess again.")
    else:
        print("CONGRATULATIONS! You guessed it right!")
        break

#complexity - O(n) where n is the number of guesses made by the user.