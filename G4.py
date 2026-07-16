import random

words = [
    "python",
    "computer",
    "keyboard",
    "developer",
    "function",
    "internet",
    "variable",
    "programming"
]

word = random.choice(words)

guessed_letters = []

lives = 6

while lives > 0:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!")
    else:
        lives -= 1
        print("Wrong!")
        print("Lives Left:", lives)

else:
    print("\nGame Over!")
    print("The word was:", word)