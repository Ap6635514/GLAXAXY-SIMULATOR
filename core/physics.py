import numpy as np

def calculate_force(x1, y1, x2, y2, m1, m2, G):
    dx = x2 - x1
    dy = y2 - y1
    dist = np.sqrt(dx**2 + dy**2) + 0.1

    force = G * m1 * m2 / dist**2

    fx = force * dx / dist
    fy = force * dy / dist

    return fx, fy