import pygame
from othello.constants import *


class Board:
    def __init__(self):
        self.board = [[None for row in range(ROWS)] for col in range(COLUMNS)]
        self.selected_piece = None
        
    def draw_board(self, window):
        window.fill(LIGHT_GREEN)
        for row in range(ROWS):
            for col in range(COLUMNS):
                pygame.draw.rect(window, GREEN, (row*SPOT_SIZE+SPOT_SIZE//20, col*SPOT_SIZE+SPOT_SIZE//20, SPOT_SIZE - SPOT_SIZE//10, SPOT_SIZE - SPOT_SIZE//10))

        self.board[3][3] = WHITE
        self.board[4][4] = WHITE
        self.board[3][4] = BLACK
        self.board[4][3] = BLACK

        for row in range(ROWS):
            for col in range(COLUMNS):
                if self.board[row][col] is not None:
                    pygame.draw.circle(window, self.board[row][col], (row*SPOT_SIZE+SPOT_SIZE//2, col*SPOT_SIZE+SPOT_SIZE//2), SPOT_SIZE//2-SPOT_SIZE//5)

        return self.board