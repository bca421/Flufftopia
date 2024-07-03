import pygame
import sys

# Initialize Pygame
pygame.init()  # Initialize Pygame modules

# Set up the display
screen_width = 800  # Width of the game window
screen_height = 600  # Height of the game window
screen = pygame.display.set_mode((screen_width, screen_height))  # Create a window of the specified size
pygame.display.set_caption("Multiple Obstacles and Interactivity")  # Set the title of the game window

# Load spritesheet
spritesheet = pygame.image.load("img/player.png").convert_alpha()  # Load the player spritesheet

# Update frame parameters
frame_width = 64  # Width of each frame in the spritesheet
frame_height = 64  # Height of each frame in the spritesheet
num_frames = 9  # Number of frames for each animation direction (left, right, up, down)
scale_factor = 2  # Scaling factor for the frames

# Function to extract frames from the spritesheet and scale them
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
        frame = sheet.subsurface(pygame.Rect(start_x + i * frame_width, start_y, frame_width, frame_height))  # Extract a frame from the spritesheet
        scaled_frame = pygame.transform.scale(frame, (int(frame_width * scale_factor), int(frame_height * scale_factor)))  # Scale the frame
        frames.append(scaled_frame)  # Add the scaled frame to the list
    return frames

# Player frames dictionary
player_frames = {
    'walking': {
        'left': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 64),  # Frames for walking left
        'right': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 192),  # Frames for walking right
        'up': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 0),  # Frames for walking up
        'down': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 128),  # Frames for walking down
    },
    'idle': {
        'left': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 64),  # Frames for idle left
        'right': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 192),  # Frames for idle right
        'up': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 0),  # Frames for idle up
        'down': get_frames(spritesheet, frame_width, frame_height, num_frames, scale_factor, 0, 192),  # Frames for idle down
    },
    # Add more actions/animations as needed
}

# Define player properties
player_x = screen_width // 2  # Initial x-coordinate of the player
player_y = screen_height // 2  # Initial y-coordinate of the player
player_animation = 'idle'  # Initial player animation state
player_direction = 'down'  # Initial player facing direction
player_frame = 0  # Current frame index for animation
player_speed = 5  # Movement speed of the player

# Define a list of obstacle rectangles with their properties
obstacles = [
    {"x": 100, "y": 100, "width": 100, "height": 100, "color": (0, 255, 0)},  # First obstacle
    {"x": 300, "y": 200, "width": 100, "height": 100, "color": (0, 255, 0)},  # Second obstacle
    {"x": 500, "y": 300, "width": 100, "height": 100, "color": (0, 255, 0)}   # Third obstacle
]

# Main game loop
running = True  # Flag to keep the game running
while running:  # Main game loop
    for event in pygame.event.get():  # Check for events (like key presses, mouse movements, etc.)
        if event.type == pygame.QUIT:  # If the event is a quit event (like clicking the close button)
            running = False  # Set the flag to False to exit the loop
    
    # Update player position based on input keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:  # Check if left arrow key is pressed and player is not at the left edge
        player_x -= player_speed  # Move the player left
        player_animation = 'walking'  # Switch to walking animation
        player_direction = 'left'  # Set player direction to left
    elif keys[pygame.K_RIGHT] and player_x < screen_width - frame_width * scale_factor:  # Check if right arrow key is pressed and player is not at the right edge
        player_x += player_speed  # Move the player right
        player_animation = 'walking'  # Switch to walking animation
        player_direction = 'right'  # Set player direction to right
    elif keys[pygame.K_UP] and player_y > 0:  # Check if up arrow key is pressed and player is not at the top edge
        player_y -= player_speed  # Move the player up
        player_animation = 'walking'  # Switch to walking animation
        player_direction = 'up'  # Set player direction to up
    elif keys[pygame.K_DOWN] and player_y < screen_height - frame_height * scale_factor:  # Check if down arrow key is pressed and player is not at the bottom edge
        player_y += player_speed  # Move the player down
        player_animation = 'walking'  # Switch to walking animation
        player_direction = 'down'  # Set player direction to down
    else:
        player_animation = 'idle'  # If no movement keys are pressed, switch to idle animation

    # Check for collision with any obstacle
    player_rect = pygame.Rect(player_x, player_y, frame_width * scale_factor, frame_height * scale_factor)  # Create a rectangle for the player
    collision = False  # Variable to track collision
    for obstacle in obstacles:
        obstacle_rect = pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"])  # Create a rectangle for each obstacle
        if player_rect.colliderect(obstacle_rect):  # If player collides with an obstacle
            collision = True  # Set collision flag to True
            break  # Exit loop on first collision

    # Update player frame
    if player_animation == 'walking':
        player_frame = (player_frame + 1) % num_frames  # Cycle through frames for walking animation
    else:
        player_frame = 0  # Reset frame index for idle animation

    # Draw everything
    screen.fill((0, 0, 0))  # Fill the screen with black
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle["color"], pygame.Rect(obstacle["x"], obstacle["y"], obstacle["width"], obstacle["height"]))  # Draw each obstacle

    # Draw the player based on current animation and direction
    screen.blit(player_frames[player_animation][player_direction][player_frame], (player_x, player_y))

    pygame.display.flip()  # Update the display to show the new screen contents

# Clean up and close the game
pygame.quit()  # Uninitialize all Pygame modules
sys.exit()  # Exit the program cleanly
