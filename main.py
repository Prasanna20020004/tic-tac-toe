game_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
player_1 = input("Enter first player name: ")
player_2 = input("Enter second player name: ")

player_choice = {
    player_1: "X",
    player_2: "O"
}


def show_board(values):
    for j in range(2):
        if j == 0:
            b = 0
        else:
            b = 3
        print(f" {values[b]}  | {values[b + 1]}  | {values[b + 2]} ")
        print("____|____|____")
    print(f" {values[-3]}  | {values[-2]}  | {values[-1]} ")
    print("    |    |    ")


def play(player):
    while True:
        choice = int(input("Enter your choice(1-9): "))
        if game_values[choice - 1] == "X" or game_values[choice - 1] == "O":
            print("Not a valid choice choose again.")
        else:
            game_values[choice - 1] = player
            break


def check(values, player_move):
    if (values[0] == player_move and values[1] == player_move and values[2] == player_move) or (
            values[0] == player_move and values[3] == player_move and values[6] == player_move) or (
            values[0] == player_move and values[4] == player_move and values[8] == player_move) or (
            values[1] == player_move and values[4] == player_move and values[7] == player_move) or (
            values[2] == player_move and values[5] == player_move and values[8] == player_move) or (
            values[2] == player_move and values[4] == player_move and values[6] == player_move) or (
            values[3] == player_move and values[4] == player_move and values[5] == player_move) or (
            values[6] == player_move and values[7] == player_move and values[8] == player_move):
        return True
    else:
        return False


i = 1
flag = 0
while i < 10:
    print(f"Player {player_1} is assigned: {player_choice[player_1]}")
    print(f"Player {player_2} is assigned: {player_choice[player_2]}")

    if i % 2 == 0:
        player_to_play = player_1
    else:
        player_to_play = player_2

    show_board(game_values)
    print(f"{player_to_play} choose.")
    play(player_choice[player_to_play])
    move = check(game_values, player_choice[player_to_play])

    if move:
        flag = 1
        print(f"Player {player_to_play} won.")
        break

    i += 1

show_board(game_values)
if flag == 0:
    print("Match Draw.")
