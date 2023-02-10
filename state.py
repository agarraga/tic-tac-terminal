from texts import text


class State:
    def __init__(self, board: str = 9 * ' '):
        self._board = board

    @property
    def board(self) -> str:
        '''9 character string composed of [XO ]'''
        return self._board

    @board.setter
    def board(self, board: str):
        self._board = board

    def x_count(self) -> int:
        '''Number of X's on board'''
        return self.board.count('X')

    def o_count(self) -> int:
        '''Number of O's on board'''
        return self.board.count('O')

    def blank_count(self) -> int:
        '''Number of balnk spaces on board'''
        return self.board.count(' ')

    def turn(self) -> str:
        '''Figure out who's turn it is'''
        if self.x_count() > self.o_count():
            return 'O'
        if self.x_count() <= self.o_count():
            return 'X'

    def tiny_pretty_board(self) -> str:
        '''String representing a tiny pretty board'''
        s = text['tiny-board']
        for i, cell in enumerate(self.board):
            s = s.replace(str(i), cell, 1)
        return s

    def __str__(self):
        '''Small, concise sumary of the state'''
        return f"board:{self.tiny_pretty_board()}It's {self.turn()}'s turn"

    def is_valid(self) -> bool:
        '''Is this a valid board state?'''
        pass

    def make_move(self, move):
        '''Determines current player and makes a move.

        Key Argumentes
        move    -- Number between 0 and 8 inclusive.
        '''
        if not 0 <= move <= 8:
            raise ValueError('Must enter a number between 1 and 9 ;)')
        if self.board[move] != ' ':
            raise ValueError('Must select an empty cell >:')
        self.board = self.board[:move] + self.turn() + self.board[move + 1:]

    def is_over(self) -> int:
        '''Determines win/loose condition

        Returns:
        0   -- Game not over (No win/draw condition met)
        1   -- Game over and X won
        2   -- Game over and O won
        3   -- Game over and it's a draw
        '''

        board = self.board
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


if __name__ == '__main__':
    state = State()
    print(state)
    print(state.board)
    print(state.turn())
    print(state.x_count())
    print(state.o_count())
    print(state.blank_count())
    state.make_move(3)
    print(state)
    print(state.board)
    print(state.turn())
    print(state.x_count())
    print(state.o_count())
    print(state.blank_count())
    print(type(state.board))
    print(type(state.turn()))
    print(type(state.x_count()))
    print(type(state.o_count()))
    print(type(state.blank_count()))
