import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Astro Jumper")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)

# Player settings
player_width = 50
player_height = 50
player_x = screen_width // 2 - player_width // 2
player_y = screen_height - player_height
player_speed = 5

# Platform settings
platform_width = 200
platform_height = 20
platform_x = random.randint(0, screen_width - platform_width)
platform_y = screen_height - platform_height - 50
platform_speed = 3

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    screen.fill(black)

    # Draw the player
    pygame.draw.rect(screen, white, (player_x, player_y, player_width, player_height))

    # Draw the platform
    pygame.draw.rect(screen, white, (platform_x, platform_y, platform_width, platform_height))

    # Update platform position
    platform_x += platform_speed
    if platform_x <= 0 or platform_x >= screen_width - platform_width:
        platform_speed *= -1

    # Check for collision
    if (player_y + player_height >= platform_y and player_y + player_height <= platform_y + platform_height) and (
            player_x + player_width >= platform_x and player_x <= platform_x + platform_width):
        # Collision occurred
        print("Collision!")

    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
