import pygame
import sys

from constants import WIDTH, HEIGHT, CREAM, FONT, MSG_FONT
from solvers.backtracking import BacktrackingSolver
from solvers.genetic import GeneticSolver
from ui.board import draw_board, animate_solution
from ui.menu import menu_loop

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("N-Queens Solver")

queen_img = pygame.image.load("assets/queen.png")
from constants import SQUARE_SIZE
queen_img = pygame.transform.scale(queen_img, (SQUARE_SIZE - 10, SQUARE_SIZE - 10))
queen_img_menu = pygame.transform.scale(queen_img, (100, 100))

def main():
    while True:
        choice = menu_loop(screen, queen_img_menu)
        if choice == "backtracking":
            solver = BacktrackingSolver(8)
            solution = solver.solve()
        elif choice == "genetic":
            solver = GeneticSolver(8)
            solution = solver.solve()
        else:
            continue

        if solution:
            animate_solution(screen, solution, queen_img)
        else:
            screen.fill(CREAM)
            msg = MSG_FONT.render("No solution found!", True, (200, 0, 0))
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
            pygame.display.flip()
            pygame.time.delay(2000)

if __name__ == "__main__":
    main()
