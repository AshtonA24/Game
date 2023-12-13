import pygame, math
from random import randint
from random import choice
pygame.init()
screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
is_swipe = False
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
        global is_swipe, sword_swipe_group, sword_swipe
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
        #mouse
        if pygame.mouse.get_pressed()[0] and self.swipe_timer < 0:
            is_swipe = True
            self.swipe_timer = 30
            if not sword_swipe_group:
                sword_swipe_group.add(sword_swipe)
            if pygame.mouse.get_pos()[0] < self.rect.center[0]:
                self.left = True
                self.left_side_click = True
            else:
                self.left = False
                self.left_side_click = False
        
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

        self.woosh = pygame.mixer.Sound("sounds/sword/woosh.mp3")

    def animation(self):
        global is_swipe, sword_swipe
        if is_swipe:
            if self.index == 0: self.woosh.play()
            self.index += 1
            if self.index >= len(self.frames): 
                self.index = 0
                is_swipe = False
                # sword_swipe_group.empty()
            self.image = self.frames[int(self.index)]
            if player.left_side_click:
                self.image = pygame.transform.flip(self.image, True, False)
    
    def check_move(self):
        global is_swipe
        if player.left_side_click:
            self.rect.midright = (player.rect.midleft[0], player.rect.center[1])
        else:
            self.rect.midleft = (player.rect.midright[0], player.rect.center[1])
        
    def update(self):
        self.check_move()
        self.animation()
    
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
        white_rect = pygame.Rect(0,0, 50, 5)
        green_rect = pygame.Rect(0,0, 50 * (self.health/self.max_health), 5)
        white_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        green_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        if self.left:
            white_rect.topleft = (self.rect.bottomleft[0] + 27, self.rect.bottomleft[1] + 5)
            green_rect.topleft = (self.rect.bottomleft[0] + 27, self.rect.bottomleft[1] + 5)
        pygame.draw.rect(screen, (255,255,255), white_rect)
        pygame.draw.rect(screen, (0,255,0), green_rect)

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
        
        
    def move(self):
        global enemy_group

        prev = self.rect.center 
        
        x = self.rect.center[0] - player.rect.center[0]
        y = self.rect.center[1] - player.rect.center[1]
        angle = math.atan2(y, x)
        speed = self.speed
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

    def check_melee(self):
        if self.rect.colliderect(player.rect):
            player.dead = True
    
    def check_attack(self):
        distance = math.hypot(player.rect.center[0] - self.rect.center[0], player.rect.center[1] - self.rect.center[1])
        if abs(distance) < self.radius:
            self.attacking = True
    
    def shoot_ball(self):
        global projectile_group
        speed = 10
        angle = math.atan2(player.rect.center[1]-self.rect.center[1], player.rect.center[0]-self.rect.center[0])
        dx = math.cos(angle)
        dy = math.sin(angle)
        projectile_group.add(MageBall(self.rect.center, dx, dy))
    
    def check_health(self):
        if self.health <= 0:
            self.dead = True
    
    def check_dead(self):
        if self.dead == True:
            enemy_group.remove(self)

    def draw_health_bar(self):
        white_rect = pygame.Rect(0,0, 50, 5)
        green_rect = pygame.Rect(0,0, 50 * (self.health/self.max_health), 5)
        white_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        green_rect.topleft = (self.rect.bottomleft[0], self.rect.bottomleft[1] + 5)
        pygame.draw.rect(screen, (255,255,255), white_rect)
        pygame.draw.rect(screen, (0,255,0), green_rect)

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
                if self.attack_rect.colliderect(player.rect):
                    player.dead = True
            self.image = self.frames_attack[int(self.index_attack)]
            if self.left:
                self.image = pygame.transform.flip(self.image, True, False)

        self.attack_timer -= 1


    def update(self):
        if not player.dead:
            self.draw_health_bar()
            self.move()
            self.animation()
            self.check_sword_hit()
            self.check_attack()
            self.check_health()
            self.check_melee()
            self.check_dead()

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
        if self.rect.top <= self.boundries_rect.top: projectile_group.remove(self)
        if self.rect.bottom >= self.boundries_rect.bottom: projectile_group.remove(self)
        if self.rect.left <= self.boundries_rect.left: projectile_group.remove(self)
        if self.rect.right >= self.boundries_rect.right: projectile_group.remove(self)


    def update(self):
        self.move()
        self.rotate()
        self.check_collisions()
            
def restart_game():
    global game_run, enemy_group
    game_run = True
    enemy_group.empty()

    player.rect.center = (700,500)
    player.dead = False
    player.full_dead = False
    # enemy_group.add(Ogre(True))
    enemy_group.add(Mage(False))
    # enemy_group.add(Ogre(False))
    enemy_group.add(Ogre(True))

def show_hitboxes(show):
    if show:
        for enemy in enemy_group:
            pygame.draw.rect(screen, (255,0,0), enemy.rect, 1)
            pygame.draw.rect(screen, (255,0,255), enemy.attack_rect, 1)
        for projectile in projectile_group:
            pygame.draw.rect(screen, (0,255,0), projectile.rect, 1)
        pygame.draw.rect(screen, (0,0,255), player.rect, 1) 
        pygame.draw.rect(screen, (0,255,0), sword_swipe.rect, 1)

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

#game over screen
main_menu_rect = pygame.Rect(0,0,700,400)
main_menu_rect.center = (700,400)
main_menu_rect_outline = pygame.Rect(0,0,720,420)
main_menu_rect_outline.center = (700,400)
main_menu_text = text_font.render('Main Menu', True, (0,0,0))
main_menu_text_rect = main_menu_text.get_rect(midtop = main_menu_rect.midtop)
text_font = pygame.font.Font('graphics/fonts/old.ttf',30)
replay_text = text_font.render('Press Space To play', True, (0,0,0))
replay_text_rect = replay_text.get_rect(midtop = main_menu_rect.center)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background,(0,0))
        
    if game_run:
        screen.blit(background,(0,0))
        
        enemy_group.draw(screen)
        enemy_group.update()
        player_group.draw(screen)
        player_group.update()
        projectile_group.update()
        projectile_group.draw(screen)
        sword_swipe_group.draw(screen)
        sword_swipe_group.update()
        screen.blit(background_rocks,(0,0))
        show_hitboxes(True)
        if player.full_dead: game_run = False
        if pygame.key.get_pressed()[pygame.K_SPACE]: restart_game()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]: game_run = False

    else:
        pygame.draw.rect(screen,(255,255,255), main_menu_rect_outline,20,20)
        pygame.draw.rect(screen,(110,127,128), main_menu_rect,10000,20)
        screen.blit(main_menu_text, main_menu_text_rect)
        screen.blit(replay_text, replay_text_rect)



        #restart game
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            restart_game()
        
    pygame.display.update()
    clock.tick(60)
        
        
    
