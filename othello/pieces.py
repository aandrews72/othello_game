from othello.constants import *


class Piece:
    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color

    def flip(self):
        if self.color == WHITE:
            self.color = BLACK
        else:
            self.color = WHITE

    def possible_moves(self, board):
        moves = []
        directions = [(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, -1), (-1, 0), (-1, 1)]
        
        for x, y, in directions:
            new_row, new_column = self.row + x, self.column + y

            if (0 <= new_row < ROWS and 0 <= new_column < COLUMNS and board[new_row][new_column] is not None and board[new_row][new_column].color != self.color):
                while True:
                    new_row, new_column = new_row + x, new_column + y
                    if (0 <= new_row < ROWS and 0 <= new_column < COLUMNS):
                        if board[new_row][new_column] is None:
                            moves.append((new_row, new_column))
                            break
                        elif board[new_row][new_column].color == self.color:
                            break
                    else: 
                        break

        return moves 
    
    def current_position(self):
        return self.row, self.column
    
    def make_move(self, row, column, board):
        if (row, column) in self.possible_moves(board):
            self.row = row
            self.column = column
            return True
        else:
            return False