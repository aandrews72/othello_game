import pygame
from othello.constants import *
from othello.board import Board



WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello")

def main():
    run = True
    board = Board()
    current_piece = None

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = pos[0] // SPOT_SIZE, pos[1] // SPOT_SIZE
                if current_piece:
                    if current_piece.make_move(row, col, board.board):
                        current_piece = None
                else:
                    current_piece = board.board[row][col]

        board.draw_board(WINDOW)
        if current_piece:
            moves = current_piece.possible_moves(board.board)
            for move in moves:
                pygame.draw.circle(WINDOW, BLUE, 
                                   (move[0]*SPOT_SIZE+SPOT_SIZE//2, move[1]*SPOT_SIZE+SPOT_SIZE//2), 25)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()

