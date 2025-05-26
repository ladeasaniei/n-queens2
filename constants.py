import pygame

WIDTH, HEIGHT = 600, 680
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

CREAM = (240, 230, 210)
BROWN = (170, 120, 60)
BUTTON_COLOR = (100, 70, 40)
BUTTON_HOVER = (140, 100, 60)
TEXT_COLOR = CREAM
OUTLINE_COLOR = (30, 20, 10)

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)
TITLE_FONT = pygame.font.SysFont("Arial", 48, bold=True)
BUTTON_FONT = pygame.font.SysFont("Arial", 28)
INSTRUCTION_FONT = pygame.font.SysFont("Arial", 20)
MSG_FONT = pygame.font.SysFont("Arial", 30)
MSG_FONT_SMALL = pygame.font.SysFont("Arial", 25)
