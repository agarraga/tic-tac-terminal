# Here are all the functions that draw stuff on the terminal
# they *should* not have returns, only print()

import os
from texts import text
from state import State


def draw_board(state: State):
    '''Draw a pretty board. '''
    board_formatted = text['set-up-board']
    for i, cell in enumerate(state.board):
        board_formatted = board_formatted.replace(str(i), cell, 1)
    print(board_formatted)


def draw_header():
    '''Clear the screen and draw a pretty header'''
    os.system('csl||clear')
    print(text['title'])


def draw_get_human_move(state: State):
    '''Draw the prompt for a human player to move. '''
    draw_header()
    draw_board(state)
    print(text['play-prompt'].format(state.turn()))


def draw_game_over(state: State):
    '''Draw the game over screen. '''
    draw_header()
    draw_board(state)
    condition = state.is_over()
    if condition == 1:
        print('Great X!!! You\'re eXcelent!')
    elif condition == 2:
        print('OMG O!!! You absolutley rOck!!')
    elif condition == 3:
        print('EVERYBODY LOOSES! YEY! <3')
