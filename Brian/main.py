import pygame
import sys
from settings import *
from player import Player
from obstacles import Obstacles
from enemies import Skeleton
from map import MapManager

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(TITLE)

# Initialize map manager and load the first map
map_manager = MapManager()
map_manager.load_map('img/map.tmx')

# Load spritesheet
spritesheet = pygame.image.load("img/player.png").convert_alpha()
spritesheet1 = pygame.image.load("img/enemies.png").convert_alpha()

# Create player, skeleton, and obstacles instances
player = Player(spritesheet)
skeleton = Skeleton(spritesheet1)
obstacles = Obstacles()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player and skeleton
    keys = pygame.key.get_pressed()
    player.update(keys)
    skeleton.update()

    # Check for collision between player and obstacles
    player_rect = pygame.Rect(player.x, player.y, FRAME_WIDTH * SCALE_FACTOR, FRAME_HEIGHT * SCALE_FACTOR)
    if obstacles.check_collision(player_rect):
        print("Collision detected!")

    # Draw everything
    screen.fill((0, 0, 0))  # Clear the screen
    map_manager.render_map(screen)  # Draw the current map
    obstacles.draw(screen)  # Draw obstacles
    player.draw(screen)  # Draw player
    skeleton.draw(screen)  # Draw skeleton

    pygame.display.flip()  # Update the display

# Clean up and close the game
pygame.quit()
sys.exit()
