import pygame, math
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk1 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk1.png'),(0.1))
        self.player_walk2 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk2.png'),(0.1))
        self.player_walk3 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk3.png'),(0.1))
        self.player_walk4 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk4.png'),(0.1))
        self.dead1 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead1.png'),(0.1))
        self.dead2 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead2.png'),(0.1))
        self.dead3 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead3.png'),(0.1))
        self.dead4 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead4.png'),(0.1))
        self.dead5 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead5.png'),(0.1))
        self.dead6 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead6.png'),(0.1))
        self.dead7 = pygame.transform.scale_by(pygame.image.load('graphics/player/dead/dead7.png'),(0.1))

        #for player animation
        self.frames_walk = [self.player_walk1, self.player_walk2, self.player_walk3, self.player_walk4]
        self.frames_dead = [self.dead1, self.dead2, self.dead3, self.dead4, self.dead5, self.dead6, 
        self.dead7, self.dead7, self.dead7, self.dead7, self.dead7,self.dead7, self.dead7, self.dead7, self.dead7]
        self.index = 0
        self.max_health = 40
        self.health = self.max_health
        self.image = self.frames_walk[self.index]
        
        self.rect = self.image.get_rect(center = (700,500))
        self.boundries_rect = pygame.Rect(-20,260,1440,500)
        self.left = False
        self.left_side_click = False
        self.speed = 4
        self.moving = False
        self.dead = False
        self.full_dead= False
        self.swipe_timer = 0

    def player_input(self):
        # keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: 
            self.rect.y -= self.speed
        if keys[pygame.K_a]: 
            self.rect.x -= self.speed
            self.left = True
        if keys[pygame.K_s]: 
            self.rect.y += self.speed
        if keys[pygame.K_d]: 
            self.rect.x += self.speed
            self.left = False
        if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]: self.moving = False
        else:self.moving = True
        
    def animation(self):
        if self.moving and not self.dead:
            self.index += 0.1
            if self.index > len(self.frames_walk):
                self.index = 0
            self.image = self.frames_walk[int(self.index)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)
     
        if self.dead:
            self.index += 0.17
            if self.index >= len(self.frames_dead):
                self.index = 0
                self.full_dead = True
            self.image = self.frames_dead[int(self.index)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)
        
    def get_pos(self):
        return (self.rect.midtop)
    
    def collisions(self):
        if self.rect.top <= self.boundries_rect.top: self.rect.top = self.boundries_rect.top
        if self.rect.bottom >= self.boundries_rect.bottom: self.rect.bottom = self.boundries_rect.bottom
        if self.rect.left <= self.boundries_rect.left: self.rect.left = self.boundries_rect.left
        if self.rect.right >= self.boundries_rect.right: self.rect.right = self.boundries_rect.right

        # if pygame.sprite.spritecollide(self, projectile_group, True): self.dead = True

    def update(self):
        if not self.dead:
            self.player_input()
            self.collisions()
        self.animation()
        self.swipe_timer -= 1
player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)



class Heart(pygame.sprite.Sprite):
    def __init__(self, heart_num):
        super().__init__()
        self.heart_full = pygame.transform.scale_by(pygame.image.load('graphics/player/hearts/full.png'),(0.6))
        self.heart_half = pygame.transform.scale_by(pygame.image.load('graphics/player/hearts/half.png'),(0.6))
        self.heart_empty = pygame.transform.scale_by(pygame.image.load('graphics/player/hearts/empty.png'),(0.6))
        self.image = self.heart_full
        self.heart_num = heart_num
        self.rect = self.image.get_rect(center = (35 * self.heart_num , 25))

    def check_hearts(self):
        if player.health/10 < self.heart_num:
            self.image = self.heart_empty

    def update(self):
        self.check_hearts()

heart_group = pygame.sprite.Group()