import pygame
import sys
import math

pygame.init()

# Reel size
WIDTH, HEIGHT = 1080, 1920
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breathing Plant")

clock = pygame.time.Clock()

# Center
cx, cy = WIDTH // 2, HEIGHT // 2 + 200

t = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((12, 14, 20))  # night background

    t += 0.04

    # Breathing + floating
    breathe = math.sin(t) * 6
    floaty = math.sin(t / 2) * 12

    # Colors
    stem_color = (120, 180, 140)
    leaf_color = (140, 210, 160)
    face_color = (230, 235, 240)
    eye_color = (40, 40, 60)

    # Stem
    pygame.draw.rect(
        screen,
        stem_color,
        (cx - 20, cy - 220 + floaty, 40, 220 + breathe),
        border_radius=20
    )

    # Leaves (left & right)
    pygame.draw.ellipse(
        screen,
        leaf_color,
        (cx - 130, cy - 170 + floaty, 120, 60 + breathe)
    )
    pygame.draw.ellipse(
        screen,
        leaf_color,
        (cx + 10, cy - 170 + floaty, 120, 60 + breathe)
    )

    # Face (flower head)
    head_y = cy - 240 + floaty
    pygame.draw.circle(
        screen,
        face_color,
        (cx, int(head_y)),
        int(65 + breathe / 2)
    )

    # 👀 Eyes (blink)
    blink = abs(math.sin(t * 2))
    eye_height = max(4, int(14 * blink))

    pygame.draw.ellipse(
        screen,
        eye_color,
        (cx - 25, head_y - 10, 12, eye_height)
    )
    pygame.draw.ellipse(
        screen,
        eye_color,
        (cx + 13, head_y - 10, 12, eye_height)
    )

    # 👄 Mouth (soft expression)
    mouth_width = 28
    mouth_curve = math.sin(t) * 6  # emotion

    pygame.draw.arc(
        screen,
        eye_color,
        (cx - mouth_width//2, head_y + 10, mouth_width, 20),
        math.pi,
        math.pi * 2 + mouth_curve * 0.05,
        2
    )

    pygame.display.flip()
    clock.tick(60)
