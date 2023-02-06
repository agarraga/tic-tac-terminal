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

from texts import text
from draw import draw_board, draw_header, draw_game_over, draw_get_human_move

EMPTY_BOARD = 9 * ' '


def make_move(board: str, token: str, move: int) -> str:
    if not 0 <= move <= 8:
        raise ValueError('Must enter a number between 1 and 9 ;)')
    if board[move] != ' ':
        raise ValueError('Must select an empty cell >:')
    if token == 'X' and board.count('X') > board.count('O'):
        raise ValueError('It\'s Os turn! :O')
    if token == 'O' and board.count('X') <= board.count('O'):
        raise ValueError('It\'s Xs turn! XD')
    board = board[:move] + token + board[move + 1:]
    return board


def get_human_move(board: str, token: str) -> str:
    move = ''
    while True:
        move = input('Move: ')
        if move == 'q':
            exit(0)
        if not move.isdigit():
            ('Must enter a digit :_')
            continue
        move = int(move) - 1
        try:
            board = make_move(board, token, move)
            break
        except ValueError as ve:
            print(ve)
            continue
    return board


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
