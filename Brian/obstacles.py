# obstacles.py
import pygame
from settings import OBSTACLES

class Obstacles:
    def __init__(self):
        self.obstacles = OBSTACLES

    def check_collision(self, player_rect):
        for obstacle in self.obstacles:
            obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"])
            if player_rect.colliderect(obstacle_rect):
                return True
        return False

    def draw(self, screen):
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, obstacle["color"], pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))
