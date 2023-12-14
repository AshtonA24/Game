import pygame, math
from random import randint

pygame.init()
screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
waves_complete = 0
game_run = False
text_font = pygame.font.Font('graphics/fonts/old.ttf',70)

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

        if pygame.sprite.spritecollide(self, projectile_group, True): self.dead = True

    def update(self):
        if not self.dead:
            self.player_input()
            self.collisions()
        self.animation()
        self.swipe_timer -= 1

class SwordSwipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.blank = pygame.image.load('graphics/sword/Empty2.png')
        self.swipe1 = pygame.transform.scale_by(pygame.image.load('graphics/sword/1 - copy.png'),(0.3))
        self.swipe2 = pygame.transform.scale_by(pygame.image.load('graphics/sword/2 - copy.png'),(0.3))
        self.swipe3 = pygame.transform.scale_by(pygame.image.load('graphics/sword/3 - copy.png'),(0.3))
        self.swipe4 = pygame.transform.scale_by(pygame.image.load('graphics/sword/4 - copy.png'),(0.3))
        self.swipe5 = pygame.transform.scale_by(pygame.image.load('graphics/sword/5 - copy.png'),(0.3))
        self.swipe6 = pygame.transform.scale_by(pygame.image.load('graphics/sword/6 - copy.png'),(0.3))
        self.swipe7 = pygame.transform.scale_by(pygame.image.load('graphics/sword/7 - copy.png'),(0.3))
        self.swipe8 = pygame.transform.scale_by(pygame.image.load('graphics/sword/8 - copy.png'),(0.3))
        self.frames = [self.blank, self.swipe1, self.swipe2, self.swipe3, self.swipe4, self.swipe5, self.swipe6, self.swipe7, self.swipe8]
        self.index = 0
        self.image = self.blank
        self.rect = self.image.get_rect(center = (player.rect.center[0],player.rect.center[1]))
        self.is_swipe = False
        self.left = False
        self.timer = 0

        self.woosh = pygame.mixer.Sound("sounds/sword/woosh.mp3")
        
    def user_input(self):
        if pygame.mouse.get_pressed()[0] and self.timer < 0:
            print('yuh')
            self.timer = 30
            self.is_swipe = True
            if pygame.mouse.get_pos()[0] < self.rect.center[0]:       
                self.left = True
                self.left_side_click = True
            else:
                self.left = False
                self.left_side_click = False

    def animation(self):
        if self.is_swipe:
            if self.index == 0: self.woosh.play()
            self.index += 1
            if self.index >= len(self.frames): 
                self.index = 0
                self.is_swipe = False
            self.image = self.frames[int(self.index)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)
    
    
        
    def update(self):
        self.user_input()
        self.animation()
        self.timer -= 1
    

            


def show_hitboxes(show):
    if show:
        pygame.draw.rect(screen, (0,0,255), player.rect, 1) 
        pygame.draw.rect(screen, (0,255,0), sword_swipe.rect, 1)

def check_move_sword():
        if sword_swipe.left:
            sword_swipe.rect.midright = (player.rect.midleft[0], player.rect.center[1])
        else:
            sword_swipe.rect.midleft = (player.rect.midright[0], player.rect.center[1])

#blackground
rescale = 800/2160
background = pygame.transform.scale_by(pygame.image.load('graphics/background/game_background_4.png').convert_alpha(),rescale)
background_rocks = pygame.transform.scale_by(pygame.image.load('graphics/background/front_decor.png').convert_alpha(),rescale)

#initializing classes

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)
enemy_group = pygame.sprite.Group()
projectile_group = pygame.sprite.Group()







sword_swipe = SwordSwipe()
sword_swipe_group = pygame.sprite.GroupSingle()
sword_swipe_group.add(sword_swipe)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
        
    
    screen.blit(background,(0,0))
    check_move_sword()
    sword_swipe_group.update()
    sword_swipe_group.draw(screen)
    player_group.update()
    player_group.draw(screen)
    show_hitboxes(True)

    
        
    pygame.display.update()
    clock.tick(60)
        
        
    
