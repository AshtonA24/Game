import pygame,math
from random import randint
from Main import Player,is_swipe,sword_swipe,player_group,sword_swipe_group

enemy_group = pygame.sprite.Group()

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
        self.attack_rect = pygame.Rect(0,0,0,0)
        
        # self.rect = self.image.get_rect(center = (randint(0,1400),randint(400,700)))
        self.rect = self.image.get_rect(midleft = (self.x, randint(300,700)))
        self.left = False
        self.left_side_click = False
        self.speed = 20
        self.moving = True
        self.attacking = False
        self.i_frame = False
        self.i_frame_timer = 0
        
        
    def move(self):
        global enemy_group

        prev = self.rect.center 
        
        x = self.rect.center[0] - player.rect.center[0]
        y = self.rect.center[1] - player.rect.center[1]
        angle = math.atan2(y, x)
        speed = 3
        move_x = speed * math.cos(angle)
        move_y = speed * math.sin(angle)

        #checks direction for later
        if x < 0: self.left = False
        else: self.left = True

        if self.attacking: self.moving = False
        else: self.moving = True


        # Calculate the new position based on the angle and speed
        if self.moving:
            self.rect.x -= move_x
            self.rect.y -= move_y

        for enemy in enemy_group:
            if pygame.sprite.collide_rect(self, enemy) and enemy != self:
                self.rect.center = prev
    
    def check_sword_hit(self):
        global sword_swipe, enemy_group, is_swipe
        if is_swipe and pygame.sprite.spritecollide(self, sword_swipe_group, False) and not self.i_frame:
            self.health -= 25
            self.i_frame_timer = 30

        self.i_frame_timer -= 1
        if self.i_frame_timer < 0: self.i_frame = False
        else: self.i_frame = True
    
    def check_attack(self):
        if pygame.sprite.spritecollide(self, player_group, False):
            self.attacking = True
        
    
    def check_health(self):
        if self.health <= 0:
            self.dead = True
    
    def check_dead(self):
        if self.dead == True:
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
                if self.attack_rect.colliderect(player.rect):
                    player.dead = True
            self.image = self.frames_attack[int(self.index_attack)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)


    def update(self):
        if not player.dead:
            self.draw_health_bar()
            self.move()
            self.attack_hitbox_rect()
            self.animation()
            self.check_sword_hit()
            self.check_attack()
            self.check_health()
            self.check_dead()