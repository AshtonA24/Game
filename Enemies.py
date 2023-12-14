import pygame, math, Player, Projectiles
from random import randint

class Mage(pygame.sprite.Sprite):
    def __init__(self, left_spawn):
        super().__init__()
        self.walk1 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/1.png'),(0.2))
        self.walk2 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/2.png'),(0.2))
        self.walk3 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/3.png'),(0.2))
        self.walk4 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/4.png'),(0.2))
        self.walk5 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/5.png'),(0.2))
        self.walk6 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/6.png'),(0.2))
        self.walk7 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/7.png'),(0.2))
        self.walk8 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/8.png'),(0.2))
        self.walk9 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/9.png'),(0.2))
        self.walk10 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/10.png'),(0.2))
        self.walk11 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/11.png'),(0.2))
        self.walk12 = pygame.transform.scale_by(pygame.image.load('graphics/mage/walk/12.png'),(0.2))

        self.attack1 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/1.png'),(0.2))
        self.attack2 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/2.png'),(0.2))
        self.attack3 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/3.png'),(0.2))
        self.attack4 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/4.png'),(0.2))
        self.attack5 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/5.png'),(0.2))
        self.attack6 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/6.png'),(0.2))
        self.attack7 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/7.png'),(0.2))
        self.attack8 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/8.png'),(0.2))
        self.attack9 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/9.png'),(0.2))
        self.attack10 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/10.png'),(0.2))
        self.attack11 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/11.png'),(0.2))
        self.attack12 = pygame.transform.scale_by(pygame.image.load('graphics/mage/attack/12.png'),(0.2))
        

        self.frames_walk = [self.walk1, self.walk2, self.walk3, self.walk4, self.walk5, self.walk6, self.walk7, self.walk8, self.walk9, self.walk10, self.walk11, self.walk12]
        self.frames_attack = [self.attack1, self.attack2, self.attack3, self.attack4, self.attack5, self.attack6, self.attack7, self.attack8]
        self.attack_timer = 0
        self.index_attack = 0
        self.index_walk = 0
        self.image = self.frames_walk[self.index_walk]
        self.left = False
        self.max_health = 125
        self.health = self.max_health
        self.left_spawn = left_spawn
        if self.left_spawn: self.x = -100
        else: self.x = 1500
        self.dead = False
        self.type = 'mage'
        self.attack_rect = pygame.Rect(0,0,0,0)
        
        # self.rect = self.image.get_rect(center = (randint(0,1400),randint(400,700)))
        self.rect = self.image.get_rect(midleft = (self.x, randint(300,700)))
        self.left = False
        self.left_side_click = False
        self.speed = 2
        self.moving = True
        self.attacking = False
        self.i_frame = False
        self.i_frame_timer = 0
        self.radius = 400
    
    def check_attack(self):
        distance = math.hypot(Player.player.rect.center[0] - self.rect.center[0], Player.player.rect.center[1] - self.rect.center[1])
        if abs(distance) < self.radius:
            self.attacking = True
    
    def shoot_ball(self):
        speed = 10
        angle = math.atan2(Player.player.rect.center[1]-self.rect.center[1], Player.player.rect.center[0]-self.rect.center[0])
        dx = math.cos(angle)
        dy = math.sin(angle)
        Projectiles.projectile_group.add(Projectiles.MageBall(self.rect.center, dx, dy))
    
    def check_health(self):
        if self.health <= 0:
            enemy_group.remove(self)
            

    def draw_health_bar(self):
        self.white_rect = pygame.Rect(0,0, 50, 5)
        self.green_rect = pygame.Rect(0,0, 50 * (self.health/self.max_health), 5)
        self.white_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        self.green_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)

    def animation(self):
        if self.moving:
            self.index_walk += 0.15
            if self.index_walk >= len(self.frames_walk):
                self.index_walk = 0
            self.image = self.frames_walk[int(self.index_walk)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)

        if self.attacking and self.attack_timer <= 0:
            self.index_attack += 0.15
            
            if self.index_attack >= len(self.frames_attack):
                self.index_attack = 0
                self.shoot_ball()
                self.attack_timer = 85
                self.attacking = False
                if self.attack_rect.colliderect(Player.player.rect):
                    Player.player.dead = True
            self.image = self.frames_attack[int(self.index_attack)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)

        self.attack_timer -= 1


    def update(self):
        if not Player.player.dead:
            self.draw_health_bar()
            self.animation()
            self.check_attack()
            self.check_health()
            self.i_frame_timer -= 1

class Ogre(pygame.sprite.Sprite):
    def __init__(self, left_spawn):
        super().__init__()
        self.stand = pygame.transform.scale_by(pygame.image.load('graphics/ogre/stand.png'),(0.2))
        self.walk1 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/walk1.png'),(0.2))
        self.walk2 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/walk2.png'),(0.2))
        self.walk3 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/walk3.png'),(0.2))
        self.attack1 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack1.png'),(0.2))
        self.attack2 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack2.png'),(0.2))
        self.attack3 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack3.png'),(0.2))
        self.attack4 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack4.png'),(0.2))
        self.attack5 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack5.png'),(0.2))
        self.attack6 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack6.png'),(0.2))
        self.attack7 = pygame.transform.scale_by(pygame.image.load('graphics/ogre/attack7.png'),(0.2))

        self.frames_walk = [self.walk1, self.walk2, self.walk3]
        self.frames_attack = [self.attack1, self.attack2, self.attack3, self.attack4, self.attack5, self.attack6, self.attack7]
        self.index_attack = 0
        self.index_walk = 0
        self.image = self.frames_walk[self.index_walk]
        self.left = False
        self.max_health = 200
        self.health = self.max_health
        self.left_spawn = left_spawn
        if self.left_spawn: self.x = -100
        else: self.x = 1500
        self.dead = False
        self.type = 'ogre'
        self.attack_rect = pygame.Rect(0,0,0,0)
     
        
        # self.rect = self.image.get_rect(center = (randint(0,1400),randint(400,700)))
        self.rect = self.image.get_rect(midleft = (self.x, randint(300,700)))
        self.left = False
        self.left_side_click = False
        self.speed = 5
        self.moving = True
        self.attacking = False
        self.i_frame = False
        self.i_frame_timer = 0
    
    def check_attack(self):
        if pygame.sprite.spritecollide(self, Player.player_group, False):
            self.attacking = True
        
    def check_health(self):
        if self.health <= 0:
            enemy_group.remove(self)
            
    def draw_health_bar(self):
        self.white_rect = pygame.Rect(0,0, 50, 5)
        self.green_rect = pygame.Rect(0,0, 50 * (self.health/self.max_health), 5)
        self.white_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        self.green_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        if self.left:
            self.white_rect.topleft = (self.rect.bottomleft[0] + 27, self.rect.bottomleft[1] + 5)
            self.green_rect.topleft = (self.rect.bottomleft[0] + 27, self.rect.bottomleft[1] + 5)

    def attack_hitbox_rect(self):
        self.attack_rect = pygame.Rect(0,0,150,100)
        self.attack_rect.center = self.rect.center


    def animation(self):
        if self.moving:
            self.index_walk += 0.1
            if self.index_walk >= len(self.frames_walk):
                self.index_walk = 0
            self.image = self.frames_walk[int(self.index_walk)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)

        if self.attacking:
            self.index_attack += 0.35
            if self.index_attack >= len(self.frames_attack):
                self.index_attack = 0
                self.attacking = False
                if self.attack_rect.colliderect(Player.player.rect):
                    Player.player.dead = True
            self.image = self.frames_attack[int(self.index_attack)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)


    def update(self):
        if not Player.player.dead:
            self.draw_health_bar()
            self.attack_hitbox_rect()
            self.animation()
            self.check_attack()
            self.check_health()
            self.i_frame_timer -= 1

enemy_group = pygame.sprite.Group()