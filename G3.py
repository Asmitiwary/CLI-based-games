board = [" " for i in range(9)]


def display_board():
    print()
    print(" ", board[0], "|", board[1], "|", board[2])
    print("----+---+----")
    print(" ", board[3], "|", board[4], "|", board[5])
    print("----+---+----")
    print(" ", board[6], "|", board[7], "|", board[8])
    print()


def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


print("Position Guide")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 ")

player = "X"

while True:

    display_board()

    position = int(input(f"Player {player}, Enter position (1-9): "))

    if position < 1 or position > 9:
        print("Invalid Position!")
        continue

    if board[position - 1] != " ":
        print("Position already occupied!")
        continue

    board[position - 1] = player

    if check_winner(player):
        display_board()
        print(f"🎉 Player {player} Wins!")
        break

    if " " not in board:
        display_board()
        print("It's a Draw!")
        break

    if player == "X":
        player = "O"
    else:
        player = "X"