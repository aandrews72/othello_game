import pygame
from constants import *


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        
    def draw_cubes(self, window):
        window.fill(GREEN)

        for row in range(ROWS):
            pygame.draw.rect(window, GREEN, (WIDTH, HEIGHT))

        self.board[4][4] = WHITE
        self.board[5][5] = WHITE
        self.board[4][5] = BLACK
        self.board[5][4] = BLACK

        return self.board