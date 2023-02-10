# TIC-TAC-TERMINAL
# An interactive, graphical, terminal tic-tac-toe written in Python

from texts import text
from draw import draw_board, draw_header, draw_game_over, draw_get_human_move
from state import State


def get_human_move(state: State):
    move = ''
    while True:
        move = input('Move: ')
        if move == 'q':
            exit(0)
        if not move.isdigit():
            print('Must enter a digit :_')
            continue
        move = int(move) - 1
        try:
            state.make_move(move)
            break
        except ValueError as ve:
            print(ve)
            continue


def hvh_loop():
    state = State()
    while True:
        if state.is_over():
            draw_game_over(state)
            input('Press Enter to continue')
            break
        draw_header()
        draw_get_human_move(state)
        get_human_move(state)


def hvc_loop():
    pass


def cvc_loop():
    pass


def main():
    while True:
        draw_header()
        welcome_board = State('XOXOXOXOX')
        draw_board(welcome_board)
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
