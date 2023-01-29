import os
from texts import text

EMPTY_BOARD = 9 * ' '


def getPlayerMove(board: str, token: str) -> str:
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


def drawBoard(board: str) -> str:
    boardDraw = text['setUpBoard']
    for i, cell in enumerate(board):
        boardDraw = boardDraw.replace(str(i), cell)
    print(boardDraw)


def drawMakeMove(board: str, token: str):
    drawBoard(board)
    print(text['play-prompt'].format(token))


def drawHeader():
    os.system('csl||clear')
    print(text['title'])


def drawGameOver(board: str, condition: int):
    drawHeader()
    drawBoard(board)
    if condition == 1:
        print('Great X!!! You\'re eXcelent!')
    if condition == 2:
        print('OMG O!!! You absolutley rOck!!')
    if condition == 3:
        print('EVERYBODY LOOSES! YEY! <3')
    os.system('pause||read -p "Press any key to continue"')


def isOver(board: str) -> int:
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
    print(candidates)
    for i, player in enumerate(['X', 'O']):
        playerHasWon = False
        if playerHasWon:
            if i == 0:
                return 1
            elif i == 1:
                return 2
    if ' ' not in board:
        return 3
    return 0


def hvhloop():
    board = EMPTY_BOARD
    currentPlayer = 'X'
    while True:
        if isOver(board):
            # Don't like it, tsk tsk tsk TODO: like it
            drawGameOver(board, isOver(board))
            break
        drawHeader()
        drawMakeMove(board, currentPlayer)
        board = getPlayerMove(board, currentPlayer)
        currentPlayer = 'X' if currentPlayer == 'O' else 'O'


def hvcloop():
    pass


def cvcloop():
    pass


def main():
    while True:
        drawHeader()
        drawBoard('XOXOXOXOX')
        print(text['initial-menu'])
        selection = input('Make a selection: ')
        if selection == '1':
            hvhloop()
        elif selection == '2':
            hvcloop()
        elif selection == '3':
            cvcloop()
        elif selection == 'q':
            break
        else:
            print('Please make a valid selection')


if __name__ == "__main__":
    main()
