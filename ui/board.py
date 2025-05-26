import pygame
from constants import ROWS, COLS, SQUARE_SIZE, CREAM, BROWN
from ui.button import draw_text_outline
from constants import TEXT_COLOR, OUTLINE_COLOR
from pygame import time

def draw_board(screen):
    for row in range(ROWS):
        for col in range(COLS):
            color = CREAM if (row + col) % 2 == 0 else BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def animate_solution(screen, solution, queen_img):
    positions = [-1] * len(solution)
    for row, col in enumerate(solution):
        positions[row] = col
        draw_board(screen)
        for r, c in enumerate(positions):
            if c != -1:
                screen.blit(queen_img, (c * SQUARE_SIZE + 5, r * SQUARE_SIZE + 5))
        pygame.display.flip()
        time.delay(500)

    waiting = True
    msg_font = pygame.font.SysFont("Arial", 25)
    msg = msg_font.render("Press [X] to close the window.", True, (0, 0, 0))
    screen.blit(msg, (20, screen.get_height() - 40))
    pygame.display.flip()

    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
