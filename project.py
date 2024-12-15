import pygame
import random


# Initialize pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Rectangular Sprite Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Sprite dimensions
SPRITE_WIDTH = 50
SPRITE_HEIGHT = 50

# Sprite positions
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

random_sprite_x = random.randint(0, SCREEN_WIDTH - SPRITE_WIDTH)
random_sprite_y = random.randint(0, SCREEN_HEIGHT - SPRITE_HEIGHT)

# Sprite movement speed
PLAYER_SPEED = 5

# Game loop flag
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Player controls
    if keys[pygame.K_UP]:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player_y += PLAYER_SPEED
    if keys[pygame.K_LEFT]:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player_x += PLAYER_SPEED

    # Keep the player within the screen bounds
    player_x = max(0, min(SCREEN_WIDTH - SPRITE_WIDTH, player_x))
    player_y = max(0, min(SCREEN_HEIGHT - SPRITE_HEIGHT, player_y))

    # Random movement for the second sprite
    random_direction = random.choice(['UP', 'DOWN', 'LEFT', 'RIGHT'])
    if random_direction == 'UP':
        random_sprite_y -= PLAYER_SPEED
    elif random_direction == 'DOWN':
        random_sprite_y += PLAYER_SPEED
    elif random_direction == 'LEFT':
        random_sprite_x -= PLAYER_SPEED
    elif random_direction == 'RIGHT':
        random_sprite_x += PLAYER_SPEED

    # Keep the random sprite within the screen bounds
    random_sprite_x = max(0, min(SCREEN_WIDTH - SPRITE_WIDTH, random_sprite_x))
    random_sprite_y = max(0, min(SCREEN_HEIGHT - SPRITE_HEIGHT, random_sprite_y))

    # Clear screen
    screen.fill(WHITE)

    # Draw the sprites
    pygame.draw.rect(screen, RED, (player_x, player_y, SPRITE_WIDTH, SPRITE_HEIGHT))
    pygame.draw.rect(screen, BLUE, (random_sprite_x, random_sprite_y, SPRITE_WIDTH, SPRITE_HEIGHT))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    clock.tick(30)

# Quit pygame
pygame.quit()
