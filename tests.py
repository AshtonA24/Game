import pygame
import sys

pygame.init()

# Set up the Pygame window
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sword Swiping Animation")

# Define colors
white = (255, 255, 255)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(white)
        self.rect = self.image.get_rect(center=(width // 2, height // 2))

# SwordSprite class
class SwordSprite(pygame.sprite.Sprite):
    def __init__(self, player_rect):
        super().__init__()
        self.image = pygame.Surface((50, 10))
        self.image.fill((255, 0, 0))  # Red for simplicity
        self.rect = self.image.get_rect()
        self.rect.center = (player_rect.right, player_rect.centery)
        self.lifespan = 20  # Number of frames the sword stays active

    def update(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            self.kill()  # Remove the sprite from all groups when lifespan is over
        else:
            # Implement animation logic (e.g., move the sword)
            pass

# Create player and sprite groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Active sword sprite variable
active_sword = None

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Trigger the sword animation
            if not active_sword:
                active_sword = SwordSprite(player.rect)
                all_sprites.add(active_sword)

    # Update sprites
    all_sprites.update()

    # Draw background and sprites
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
