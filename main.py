import pygame
import random
import math

# Initialize
pygame.init()
SCREEN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Mini Game: Reaction Test")

# Colors & Config
BG_COLOR = (30, 30, 30)
TARGET_COLOR = (255, 0, 0)
clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    # 1. Event Handling (Input)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Draw
    SCREEN.fill(BG_COLOR)
    radius = 30

    target_x = random.randint(radius, 800 - radius)
    target_y = random.randint(radius, 600 - radius)
    pygame.draw.circle(SCREEN, TARGET_COLOR, (target_x, target_y), radius)

    pygame.display.flip()
    clock.tick(60)
