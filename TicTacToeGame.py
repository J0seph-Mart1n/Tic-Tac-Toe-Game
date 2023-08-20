def display_board(board):
    print("Your board")
    print(f"  {board[7]}   |    {board[8]}   |    {board[9]}")
    print("________________________")
    print(f"  {board[4]}   |    {board[5]}   |    {board[6]}")
    print("________________________")
    print(f"  {board[1]}   |    {board[2]}   |    {board[3]}")


def player_input():
    choice = ''
    acceptable_values = ['X', 'O']
    while choice not in acceptable_values:
        choice = input("Enter a choice (X or O): ")
        if choice not in acceptable_values:
            print("You have entered a wrong choice!!")

    if choice == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True
    else:
        return False

import random

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 2"
    else:
        return "Player 1"


def space_check(board, position):
    if board[position] == '':
        return True
    return False


def full_board_check(board):
    for position in range(1, 10):
        if space_check(board, position):
            return False
    return True


def player_choice(board):
    position = ''
    while position not in range(1, 10):
        position = int(input("Enter a position (1-9): "))
        if position not in range(1, 10):
            print("You have entered the wrong position!!")

    if space_check(board, position):
        return position


def replay():
    choice = ''
    while choice not in ['Y', 'N']:
        choice = input("Do you want to play again (Y or N): ")
        if choice not in ['Y', 'N']:
            print("Please enter Y or N!!")

    if choice == 'Y':
        return True
    return False


print('Welcome to Tic Tac Toe!')

while True:
    # Set the game up here
    # pass
    board = ['#', '', '', '', '', '', '', '', '', '']
    player_1_marker, player_2_marker = player_input()
    turn = choose_first()
    print(f"{turn} will go first")

    start = ''
    while start not in ['Y', 'N']:
        start = input("Do you want to play the game? (Y or N)")

    if start == 'Y':
        game_on = True
    elif start == 'N':
        game_on = False

    while game_on:
        # Player 1 Turn
        if turn == 'Player 1':

            display_board(board)
            position = player_choice(board)
            place_marker(board, player_1_marker, position)

            if win_check(board, player_1_marker):
                display_board(board)
                print("Congrats player 1 you have won!!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game has ended in draw")
                    break
                else:
                    turn = 'Player 2'
        else:
            # Player2's turn.

            display_board(board)
            position = player_choice(board)
            place_marker(board, player_2_marker, position)

            if win_check(board, player_2_marker):
                display_board(board)
                print("Congrats Player 2 you have won!!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game has ended in draw")
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break