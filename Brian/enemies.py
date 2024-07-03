# enemies.py
import pygame
from settings import *
from utils import get_frames

class Skeleton:
    def __init__(self, spritesheet):
        self.x = SCREEN_WIDTH // 9
        self.y = SCREEN_HEIGHT // 9
        self.animation = 'walking'
        self.direction = 'down'
        self.frame = 0
        self.speed = SKELETON_SPEED
        self.start_y = self.y
        self.end_y = self.y + 200  # Patrol range (200 pixels)

        # Load skeleton frames
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

    def update(self):
        # Move skeleton back and forth
        if self.direction == 'down':
            self.y += self.speed
            if self.y >= self.end_y:
                self.direction = 'up'
        elif self.direction == 'up':
            self.y -= self.speed
            if self.y <= self.start_y:
                self.direction = 'down'

        # Update animation frame
        self.frame = (self.frame + 1) % NUM_FRAMES

    def draw(self, screen):
        screen.blit(self.frames['walking'][self.direction][self.frame], (self.x, self.y))
