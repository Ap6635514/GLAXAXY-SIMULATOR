from config import WIDTH, HEIGHT, BLACK_HOLE_MASS

class BlackHole:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.mass = BLACK_HOLE_MASS

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, (255, 0, 0), (int(self.x), int(self.y)), 5)