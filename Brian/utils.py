# utils.py
import pygame

def get_frames(sheet, frame_width, frame_height, num_frames, scale_factor, start_x, start_y):
    """
    Extracts frames from a spritesheet and scales them.

    Args:
    - sheet: Pygame surface containing the spritesheet.
    - frame_width: Width of each frame in pixels.
    - frame_height: Height of each frame in pixels.
    - num_frames: Number of frames to extract.
    - scale_factor: Scaling factor for the frames.
    - start_x: Starting x-coordinate of the frames on the spritesheet.
    - start_y: Starting y-coordinate of the frames on the spritesheet.

    Returns:
    - List of Pygame surfaces, each representing a scaled frame.
    """
    frames = []
    for i in range(num_frames):
        frame = sheet.subsurface(pygame.Rect(start_x + i * frame_width, start_y, frame_width, frame_height))
        scaled_frame = pygame.transform.scale(frame, (int(frame_width * scale_factor), int(frame_height * scale_factor)))
        frames.append(scaled_frame)
    return frames
