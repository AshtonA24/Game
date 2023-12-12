import pygame
import sys

pygame.init()

# Set up the Pygame window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sword Swiping Animation")
sound = pygame.mixer.Sound("sound.mp3")

#
# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            sound.play()

    # Draw background and sprites
    screen.fill((0, 0, 0))


    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
