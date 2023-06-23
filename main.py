import pygame
from othello.constants import *
from othello.board import Board


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello")

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(60) # 60 FPS frame rate
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        board.draw_board(WINDOW)
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()
