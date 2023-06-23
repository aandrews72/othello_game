import pygame
from othello.constants import *

WIDTH, HEIGHT = 1000, 800
ROWS, COLUMNS = 8, 8
SPOT_SIZE = WIDTH//COLUMNS

GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Othello")

def main():
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    
    pygame.quit()

if __name__ == "__main__":
    main()
