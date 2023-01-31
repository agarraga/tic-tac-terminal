# TIC-TAC-TERMINAL
# An interactive, graphical, terminal tic-tac-toe written in Python
#
# > The `board` variable refers to a 9 character string that describes a board
# state with `X`s `O`s and ` `(space)'s from top left to bottom right row-wise.
# e.g. 'OX  OX X ' would be:
#
#   |O|X| |
#   | |O|X|
#   | |X| |
#
# > The `token` or `player` variable denotes either `X` or `O`.import os

import os
from texts import text

EMPTY_BOARD = 9 * ' '


def get_human_move(board: str, token: str) -> str:
    move = ''
    while True:
        move = input('Move: ')
        if move == 'q':
            exit(0)
        if not move.isdigit():
            print('Must enter a digit :_')
            continue
        move = int(move)
        if not 1 <= move <= 9:
            print('Must enter a number between 1 and 9 ;)')
            continue
        move -= 1
        if board[move] != ' ':
            print('Must select an empty cell >:')
            continue
        break
    board = board[:move] + token + board[move + 1:]
    return board


def draw_board(board: str):
    board_formatted = text['set-up-board']
    for i, cell in enumerate(board):
        board_formatted = board_formatted.replace(str(i), cell, 1)
    print(board_formatted)


def draw_get_human_move(board: str, token: str):
    draw_board(board)
    print(text['play-prompt'].format(token))


def draw_header():
    os.system('csl||clear')
    print(text['title'])


def draw_game_over(board: str, condition: int):
    # 1 -> X won, 2 -> O won, 3 -> Draw
    draw_header()
    draw_board(board)
    if condition == 1:
        print('Great X!!! You\'re eXcelent!')
    elif condition == 2:
        print('OMG O!!! You absolutley rOck!!')
    elif condition == 3:
        print('EVERYBODY LOOSES! YEY! <3')


def is_over(board: str) -> int:
    # 0 -> Not over, 1 -> X won, 2 -> O won, 3 -> Draw
    candidates = []
    candidates.append(board[0:3])
    candidates.append(board[3:6])
    candidates.append(board[6:9])
    candidates.append(board[0:7:3])
    candidates.append(board[1:8:3])
    candidates.append(board[2:9:3])
    candidates.append(board[0:9:4])
    candidates.append(board[2:7:2])
    # B&W footage voice-over: "There has to be a better way!"
    # TODO: Make lazier, i.e. make condition jump on first `True`.
    condition = 0
    if any(map(lambda candidate: candidate == 'XXX', candidates)):
        condition = 1
    elif any(map(lambda candidate: candidate == 'OOO', candidates)):
        condition = 2
    elif ' ' not in board:
        condition = 3
    return condition


def hvh_loop():
    board = EMPTY_BOARD
    current_player = 'X'
    while True:
        over = is_over(board)
        # Don't like it, tsk tsk tsk TODO: like it
        if over:
            draw_game_over(board, over)
            input('Press Enter to continue')
            break
        draw_header()
        draw_get_human_move(board, current_player)
        board = get_human_move(board, current_player)
        current_player = 'X' if current_player == 'O' else 'O'


def hvc_loop():
    pass


def cvc_loop():
    pass


def main():
    while True:
        draw_header()
        draw_board('XOXOXOXOX')
        print(text['initial-menu'])
        selection = input('Make a selection: ')
        if selection == '1':
            hvh_loop()
        elif selection == '2':
            hvc_loop()
        elif selection == '3':
            cvc_loop()
        elif selection == 'q':
            break
        else:
            print('Please make a valid selection')


if __name__ == "__main__":
    main()
