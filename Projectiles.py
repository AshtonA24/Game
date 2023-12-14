import pygame

class MageBall(pygame.sprite.Sprite):
    def __init__(self, start, dx, dy):
        super().__init__()

        self.orb = pygame.image.load('graphics/projectiles/mage/orb.png')
        self.image = self.orb
        self.rect = self.image.get_rect(center = start)
        self.dx = dx
        self.dy = dy
        self.speed = 15
        self.rotate_int = 0
        self.boundries_rect = pygame.Rect(-50,-50,1500,900)

    def move(self):
        self.rect.x += self.dx * self.speed
        self.rect.y += self.dy * self.speed
    
    def rotate(self):
        self.image = pygame.transform.rotate(self.orb,self.rotate_int)
        self.rotate_int += 10

    def check_collisions(self):
        if self.rect.top <= self.boundries_rect.top: self.kill()
        if self.rect.bottom >= self.boundries_rect.bottom: self.kill()
        if self.rect.left <= self.boundries_rect.left: self.kill()
        if self.rect.right >= self.boundries_rect.right: self.kill()


    def update(self):
        self.move()
        self.rotate()
        self.check_collisions()

projectile_group = pygame.sprite.Group()