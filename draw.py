# Here are all the functions that draw stuff on the terminal
# they *should* not have returns. Only print()

import os
from texts import text


def draw_board(board: str):
    '''Draw a pretty board.

    Keyword arguments:
    board -- 9 character string composed of [XO ]
    '''
    board_formatted = text['set-up-board']
    for i, cell in enumerate(board):
        board_formatted = board_formatted.replace(str(i), cell, 1)
    print(board_formatted)


def draw_header():
    '''Draw a pretty header'''
    os.system('csl||clear')
    print(text['title'])


def draw_get_human_move(board: str, token: str):
    '''Prompt a human player to move.

    Keyword arguments:
    board -- 9 character string composed of [XO ]
    token -- 'X' or 'O'
    '''
    draw_header()
    draw_board(board)
    print(text['play-prompt'].format(token))


def draw_game_over(board: str, condition: int):
    '''Draw the game over screen.

    Keyword arguments:
    board     -- 9 character string composed of [XO ]
    condotion -- 1, 2, or 3 (X win, O win, or Draw)
    '''
    draw_header()
    draw_board(board)
    if condition == 1:
        print('Great X!!! You\'re eXcelent!')
    elif condition == 2:
        print('OMG O!!! You absolutley rOck!!')
    elif condition == 3:
        print('EVERYBODY LOOSES! YEY! <3')
