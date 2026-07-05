import random
choices = ["rock", "scissors", "paper"]

player_score = 0
computer_score = 0

while True:
    player_choice = input("Enter your choice : Rock, Paper, Scissors (or Quit to stop): ").lower()

    if player_choice == "quit":
        break

    if player_choice not in choices:
        print("Invalid choice, please choose Rock, Paper or Scissors,")
        continue

    computer_choice = random.choice(choices)
    print("Computer's choice:", computer_choice)

    if (player_choice == computer_choice):
        print(" It's a tie !")

    elif(player_choice =="rock" and computer_choice == "scissors")or\
        (player_choice == "scissors" and computer_choice == "paper")or\
        (player_choice == "paper" and computer_choice == "rock"):
        print("You Win !")
        player_score +=1

    else:
        print("Computer wins !")
        computer_score +=1
    
    print("Score:")
    print("Player's score:", player_score)
    print("Computer's score:", computer_score)

print("Final Score:")
print("Player Score:", player_score)
print("Computer Score:", computer_score)
print(" Thanks for playing !")

