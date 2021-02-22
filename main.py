# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def Tic_Tac_Toe():
    global winner
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 0
    max_turns = len(board)

    found_winner = False
    show_board(board)
    while not found_winner and turn < max_turns:
        if turn % 2 == 0:
            board = do_human_turn(board)
        else:
            board = do_IA_turn(board, turn)
            # board = do_human_turn(board)

        turn += 1
        show_board(board)

        found_winner = is_there_winner(board)

    if not found_winner:
        print("Draw!")
    elif turn % 2 == 1:
        print("Winner is human!")
    elif turn % 2 == 0:
        print("Winner is AI!")
    else:
        print("Error!")


def is_there_winner(board):
    winning_state = board[0] == board[1] == board[2] != 0 or board[3] == board[4] == board[5] != 0 or \
                    board[6] == board[7] == board[8] != 0 or board[0] == board[3] == board[6] != 0 or \
                    board[1] == board[4] == board[7] != 0 or board[2] == board[5] == board[8] != 0 or \
                    board[0] == board[4] == board[8] != 0 or board[6] == board[4] == board[2] != 0

    return winning_state


def show_board(board):
    for i in range(3):
        r = ""
        for j in range(3):
            r = r + str(board[i * 3 + j]) + " "
        print(r)
    return


def do_human_turn(board):
    move_str = input("Pick move [1 - 9] -> ")
    move = int(move_str)-1
    while board[move] != 0:
        move_str = input("Pick again [1 - 9] -> ")
        move = int(move_str)-1

    board[move] = 1

    return board


def do_IA_turn(board, turn):
    print("Let me pick.....")
    move, _ = predict(board, turn)
    board[move] = 2

    return board


def predict(board, turn):
    possible_moves = []
    p_value = 0  # In case you don't know, you predict Draw
    p_move = 4  # In case you don't know, you predict Center

    n_possible_moves = board.count(0)
    game_ended = n_possible_moves == 0

    if is_there_winner(board):
        if turn % 2 == 0:
            # it's human turn, so get minimum
            p_value = -10
        else:
            # it's AI turn, so get max
            p_value = +10
    elif game_ended:
        p_value = 0
        #  print("I noticed a draw")
    else:
        ind_move = 0
        possible_moves = []
        possible_values = []
        for element in board:
            if element == 0:
                # if it's a possible move
                # Create copy, but not reference to the other array
                copy_board = board.copy()
                if turn % 2 == 0:
                    copy_board[ind_move] = 1  # Try what Human will do
                else:
                    copy_board[ind_move] = 2
                this_predicted_move, this_predicted_value = predict(copy_board, turn + 1)
                possible_moves.append(ind_move)
                possible_values.append(this_predicted_value)
            ind_move += 1

        if turn % 2 == 1:
            # it's human turn, so get minimum
            p_value = min(possible_values)
            p_move = possible_moves[possible_values.index(p_value)]
        else:
            # it's AI turn, so get max
            # print("Debug :")
            # print(possible_values)
            # print(possible_moves)

            p_value = max(possible_values)
            p_move = possible_moves[possible_values.index(p_value)]

    return p_move, p_value


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Tic_Tac_Toe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
