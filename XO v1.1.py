board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", ]


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f"{c}")
        else:
            print(f"{c}|", end="")

print_state(board)

win_comb = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]


def get_winner(state, combinations):
    for [x, y, z] in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == "X" or state[x] == "O"):
            return state[x]
    return ""


def play_game(board):
    current_sign = "X"
    counter = 0
    while (get_winner(board, win_comb)==""):
        index = int(input(f"Введите № индекса ячейки, от 0 до 8. Игрок: {current_sign}"))
        board[index] = current_sign
        counter+=1
        print_state(board)
        winner_sign = get_winner(board, win_comb)

        if winner_sign != "":
            print(f"У нас есть победитель! Игрок: {winner_sign}")
        current_sign = "X" if current_sign == "O" else "O"

        if counter ==9:
            print("Ничья!")
            break

play_game(board)

