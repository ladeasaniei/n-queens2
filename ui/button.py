import pygame
from constants import BUTTON_COLOR, BUTTON_HOVER, TEXT_COLOR, OUTLINE_COLOR, BUTTON_FONT

def draw_text_outline(surface, text, font, text_color, outline_color, center):
    base = font.render(text, True, text_color)
    x, y = center
    for dx, dy in [(-2,0), (2,0), (0,-2), (0,2), (-2,-2), (-2,2), (2,-2), (2,2)]:
        pos = base.get_rect(center=(x+dx, y+dy))
        surface.blit(font.render(text, True, outline_color), pos)
    base_rect = base.get_rect(center=center)
    surface.blit(base, base_rect)

class Button:
    def __init__(self, rect, text):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.font = BUTTON_FONT
        self.color = BUTTON_COLOR
        self.hover_color = BUTTON_HOVER

    def draw(self, surface):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(surface, color, self.rect, border_radius=8)
        draw_text_outline(surface, self.text, self.font, TEXT_COLOR, OUTLINE_COLOR, self.rect.center)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.rect.collidepoint(event.pos)
