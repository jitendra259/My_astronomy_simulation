import pygame
import numpy as np
import math

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Hole Merger Simulation")

clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (80, 180, 255)
PURPLE = (180, 80, 255)
GLOW = (255, 180, 0)

# Create gravitational-wave chirp sound
def create_chirp_sound():

    sample_rate = 44100
    duration = 3

    t = np.linspace(
        0,
        duration,
        int(sample_rate * duration)
    )

    # Increasing frequency
    frequency = np.linspace(
        100,
        1200,
        len(t)
    )

    wave = np.sin(
        2 * np.pi * frequency * t
    )

    # Smooth fade effect
    envelope = np.linspace(
        0,
        1,
        len(t)
    )

    wave = wave * envelope

    audio = np.int16(wave * 32767)

    stereo = np.column_stack((audio, audio))

    return pygame.sndarray.make_sound(stereo)

chirp_sound = create_chirp_sound()

# Generate background stars
stars = []

for _ in range(200):

    x = np.random.randint(0, WIDTH)

    y = np.random.randint(0, HEIGHT)

    stars.append((x, y))

# Initial orbit values
angle = 0
radius = 220

merged = False
sound_played = False
merge_timer = 0

running = True

# Main loop
while running:

    screen.fill(BLACK)

    # Exit event
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

    # Draw stars
    for star in stars:
        pygame.draw.circle(screen, WHITE, star, 1)

    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    # Before merger
    if not merged:

        # Black hole positions
        x1 = center_x + math.cos(angle) * radius
        y1 = center_y + math.sin(angle) * radius

        x2 = center_x + math.cos(angle + math.pi) * radius
        y2 = center_y + math.sin(angle + math.pi) * radius

        # Glow effect
        pygame.draw.circle(
            screen,
            BLUE,
            (int(x1), int(y1)),
            45
        )

        pygame.draw.circle(
            screen,
            PURPLE,
            (int(x2), int(y2)),
            45
        )

        # Black hole cores
        pygame.draw.circle(
            screen,
            BLACK,
            (int(x1), int(y1)),
            30
        )

        pygame.draw.circle(
            screen,
            BLACK,
            (int(x2), int(y2)),
            30
        )

        # Orbit path
        pygame.draw.circle(
            screen,
            (50, 50, 50),
            (center_x, center_y),
            int(radius),
            1
        )

        # Motion update
        angle += 0.02
        radius -= 0.25

        # Merger condition
        if radius <= 20:
            merged = True

    # After merger
    else:

        # Play merger sound once
        if not sound_played:

            chirp_sound.play()

            sound_played = True

        merge_timer += 1

        # Pulsing glow effect
        glow_size = 70 + int(
            10 * math.sin(merge_timer * 0.2)
        )

        pygame.draw.circle(
            screen,
            GLOW,
            (center_x, center_y),
            glow_size
        )

        # Final black hole
        pygame.draw.circle(
            screen,
            BLACK,
            (center_x, center_y),
            55
        )

        # Accretion ring
        pygame.draw.circle(
            screen,
            (255, 120, 0),
            (center_x, center_y),
            80,
            4
        )

    # Title text
    font = pygame.font.SysFont("Arial", 28)

    text = font.render(
        "Black Hole Merger Simulation",
        True,
        WHITE
    )

    screen.blit(text, (20, 20))

    pygame.display.update()

    clock.tick(60)

pygame.quit()
