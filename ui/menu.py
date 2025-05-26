import sys

import pygame
from constants import WIDTH, HEIGHT, CREAM, TEXT_COLOR, OUTLINE_COLOR, TITLE_FONT, INSTRUCTION_FONT
from ui.button import Button, draw_text_outline

def menu_loop(screen, queen_img_menu):
    backtracking_btn = Button((WIDTH//2 - 150, 200, 300, 60), "Backtracking")
    genetic_btn = Button((WIDTH//2 - 150, 300, 300, 60), "Genetic Algorithm")

    while True:
        screen.fill(CREAM)
        draw_text_outline(screen, "N-Queens Solver", TITLE_FONT, TEXT_COLOR, OUTLINE_COLOR, (WIDTH//2, 80))

        backtracking_btn.draw(screen)
        genetic_btn.draw(screen)

        instr = [
            "Select an algorithm to solve the 8-Queens puzzle.",
            "Click on a button below to start."
        ]
        for i, line in enumerate(instr):
            draw_text_outline(screen, line, INSTRUCTION_FONT, TEXT_COLOR, OUTLINE_COLOR, (WIDTH//2, 140 + i*30))

        screen.blit(queen_img_menu, (WIDTH//2 - queen_img_menu.get_width()//2, HEIGHT - queen_img_menu.get_height() - 20))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if backtracking_btn.is_clicked(event):
                return "backtracking"
            if genetic_btn.is_clicked(event):
                return "genetic"
