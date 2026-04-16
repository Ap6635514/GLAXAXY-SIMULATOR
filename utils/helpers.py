import numpy as np
import random

# 📏 Distance between two points
def distance(x1, y1, x2, y2):
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)


# 🧭 Normalize a vector (direction)
def normalize(dx, dy):
    dist = np.sqrt(dx**2 + dy**2) + 1e-5
    return dx / dist, dy / dist


# 🎯 Clamp value (used for velocity limits)
def clamp(value, max_value):
    if value > max_value:
        return max_value
    if value < -max_value:
        return -max_value
    return value


# 🎲 Random float in range
def rand_range(a, b):
    return random.uniform(a, b)


# 🌌 Generate spiral position
def spiral_position(center_x, center_y, radius, angle):
    x = center_x + radius * np.cos(angle)
    y = center_y + radius * np.sin(angle)
    return x, y