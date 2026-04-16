import pygame
import numpy as np
import random

# Init
pygame.init()

WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galaxy Simulator - Ultimate")

clock = pygame.time.Clock()

G = 0.1
NUM_STARS = 150
BLACK_HOLE_MASS = 1000


# 🎨 LOAD ASSETS (SAFE)
try:
    bg = pygame.image.load("assets/images/galaxy_bg.png")
    bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
except:
    bg = None

try:
    star_img = pygame.image.load("assets/images/star.png")
    star_img = pygame.transform.scale(star_img, (4, 4))
except:
    star_img = None

try:
    pygame.mixer.init()
    pygame.mixer.music.load("assets/sounds/ambient.wav")
    pygame.mixer.music.play(-1)
except:
    pass

try:
    font = pygame.font.Font("assets/fonts/space_font.ttf", 18)
except:
    font = None


# 🕳️ Black Hole (with glow)
class BlackHole:
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.mass = BLACK_HOLE_MASS

    def draw(self):
        for r in range(20, 0, -1):
            alpha = int(200 * (r / 20))
            glow_surface = pygame.Surface((r*2, r*2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, (255, 80, 80, alpha), (r, r), r)
            screen.blit(glow_surface, (int(self.x - r), int(self.y - r)))


# 🌟 Star
class Star:
    def __init__(self):
        angle = random.uniform(0, 2 * np.pi)
        radius = random.uniform(50, 300) ** 0.9

        spiral_factor = 0.3
        angle += radius * spiral_factor / 300

        self.x = WIDTH / 2 + radius * np.cos(angle)
        self.y = HEIGHT / 2 + radius * np.sin(angle)

        base_speed = np.sqrt(G * BLACK_HOLE_MASS / radius) * 0.8
        speed = base_speed * random.uniform(0.9, 1.1)

        self.vx = -speed * np.sin(angle)
        self.vy = speed * np.cos(angle)

        self.mass = random.uniform(1, 3)

    def update(self, stars, black_hole):
        fx, fy = 0, 0

        for other in stars:
            if other != self:
                dx = other.x - self.x
                dy = other.y - self.y
                dist = np.sqrt(dx**2 + dy**2 + 25)

                force = G * self.mass * other.mass / dist**2 * 0.05

                fx += force * dx / dist
                fy += force * dy / dist

        dx = black_hole.x - self.x
        dy = black_hole.y - self.y
        dist = np.sqrt(dx**2 + dy**2 + 25)

        force = G * self.mass * black_hole.mass / dist**2

        fx += force * dx / dist
        fy += force * dy / dist

        self.vx += fx / self.mass
        self.vy += fy / self.mass

        max_speed = 5
        speed = (self.vx**2 + self.vy**2)**0.5

        if speed > max_speed:
            self.vx = (self.vx / speed) * max_speed
            self.vy = (self.vy / speed) * max_speed

        self.x += self.vx
        self.y += self.vy

    def draw(self):
        dx = self.x - WIDTH / 2
        dy = self.y - HEIGHT / 2
        dist = (dx**2 + dy**2)**0.5

        brightness = max(100, 255 - int(dist * 0.5))
        color = (brightness, brightness, 255)

        size = int(self.mass)

        if star_img:
            screen.blit(star_img, (int(self.x), int(self.y)))
        else:
            pygame.draw.circle(screen, color, (int(self.x), int(self.y)), size)


# Create objects
stars = [Star() for _ in range(NUM_STARS)]
black_hole = BlackHole()


# Game loop
running = True
while running:
    # Background or trail
    if bg:
        screen.blit(bg, (0, 0))
    else:
        fade_surface = pygame.Surface((WIDTH, HEIGHT))
        fade_surface.set_alpha(10)
        fade_surface.fill((0, 0, 10))
        screen.blit(fade_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for star in stars:
        star.update(stars, black_hole)
        star.draw()

    black_hole.draw()

    # UI text
    if font:
        text = font.render("Galaxy Simulator", True, (255, 255, 255))
        screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()