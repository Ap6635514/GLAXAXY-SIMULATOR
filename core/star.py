import numpy as np
import random
from config import WIDTH, HEIGHT, G
from core.physics import calculate_force
from utils.helpers import distance, normalize

class Star:
    def __init__(self):
        angle = random.uniform(0, 2 * np.pi)
        radius = random.uniform(50, 300)

        self.x = WIDTH / 2 + radius * np.cos(angle)
        self.y = HEIGHT / 2 + radius * np.sin(angle)

        speed = np.sqrt(G * 1000 / radius)

        self.vx = -speed * np.sin(angle)
        self.vy = speed * np.cos(angle)

        self.mass = random.uniform(1, 3)

    def update(self, stars, black_hole):
        fx, fy = 0, 0

        # Interaction with other stars
        for other in stars:
            if other != self:
                dfx, dfy = calculate_force(
                    self.x, self.y,
                    other.x, other.y,
                    self.mass, other.mass, G
                )
                fx += dfx
                fy += dfy

        # Interaction with black hole
        dfx, dfy = calculate_force(
            self.x, self.y,
            black_hole.x, black_hole.y,
            self.mass, black_hole.mass, G
        )
        fx += dfx
        fy += dfy

        # Update velocity
        self.vx += fx / self.mass
        self.vy += fy / self.mass

        # Update position
        self.x += self.vx
        self.y += self.vy

    def draw(self, screen):
        import pygame
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), 2)
