# player.py
import pygame
from settings import *
from utils import get_frames

class Player:
    def __init__(self, spritesheet):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.animation = 'idle'
        self.direction = 'down'
        self.frame = 0
        self.speed = PLAYER_SPEED

        # Load player frames
        self.frames = {
            'walking': {
                'left': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 64),
                'right': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 192),
                'up': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 0),
                'down': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 128),
            },
            'idle': {
                'left': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 64),
                'right': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 192),
                'up': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 0),
                'down': get_frames(spritesheet, FRAME_WIDTH, FRAME_HEIGHT, NUM_FRAMES, SCALE_FACTOR, 0, 128),
            },
        }

    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
            self.animation = 'walking'
            self.direction = 'left'
        elif keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - FRAME_WIDTH * SCALE_FACTOR:
            self.x += self.speed
            self.animation = 'walking'
            self.direction = 'right'
        elif keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
            self.animation = 'walking'
            self.direction = 'up'
        elif keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - FRAME_HEIGHT * SCALE_FACTOR:
            self.y += self.speed
            self.animation = 'walking'
            self.direction = 'down'
        else:
            self.animation = 'idle'

        if self.animation == 'walking':
            self.frame = (self.frame + 1) % NUM_FRAMES
        else:
            self.frame = 0

    def draw(self, screen):
        screen.blit(self.frames[self.animation][self.direction][self.frame], (self.x, self.y))
