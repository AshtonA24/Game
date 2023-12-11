import pygame
pygame.init()
screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
is_swipe = False

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.player_walk1 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk1.png'),(0.1))
        self.player_walk2 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk2.png'),(0.1))
        self.player_walk3 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk3.png'),(0.1))
        self.player_walk4 = pygame.transform.scale_by(pygame.image.load('graphics/player/Walking/walk4.png'),(0.1))

        #for player animation
        self.frames = [self.player_walk1, self.player_walk2, self.player_walk3, self.player_walk4]
        self.index = 0
        self.image = self.frames[self.index]

        self.rect = self.image.get_rect(center = (700,400))
        self.boundries_rect = pygame.Rect(-20,260,1440,500)
        self.left = False
        self.left_side_click = False
        self.speed = 6
        self.moving = False

    def player_input(self):
        global is_swipe, sword_swipe_group, sword_swipe
        # keyboard
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: self.rect.y -= self.speed
        if keys[pygame.K_a]: 
            self.rect.x -= self.speed
            self.left = True
        if keys[pygame.K_s]: 
            self.rect.y += self.speed
        if keys[pygame.K_d]: 
            self.rect.x += self.speed
            self.left = False
            #
        if not keys[pygame.K_w] and not keys[pygame.K_a] and not keys[pygame.K_s] and not keys[pygame.K_d]: self.moving = False
        else:self.moving = True
        #mouse
        if pygame.mouse.get_pressed()[0]:
            is_swipe = True
            if not sword_swipe_group:
                sword_swipe_group.add(sword_swipe)
            if pygame.mouse.get_pos()[0] < self.rect.center[0]:
                self.left = True
                self.left_side_click = True
            else:
                self.left = False
                self.left_side_click = False
        
    def animation(self):
        if self.moving:
            self.index += 0.1
            if self.index > len(self.frames):
                self.index = 0
        self.image = self.frames[int(self.index)]
        if self.left:
            self.image = pygame.transform.flip(self.image, True, False)

    def get_pos(self):
        return (self.rect.midtop)
    
    def collisions(self):
        if self.rect.top <= self.boundries_rect.top: self.rect.top = self.boundries_rect.top
        if self.rect.bottom >= self.boundries_rect.bottom: self.rect.bottom = self.boundries_rect.bottom
        if self.rect.left <= self.boundries_rect.left: self.rect.left = self.boundries_rect.left
        if self.rect.right >= self.boundries_rect.right: self.rect.right = self.boundries_rect.right

    def update(self):
        self.player_input()
        self.collisions()
        self.animation()

class SwordSwipe(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.swipe1 = pygame.transform.scale_by(pygame.image.load('graphics/sword/1.png'),(0.3))
        self.swipe2 = pygame.transform.scale_by(pygame.image.load('graphics/sword/2.png'),(0.3))
        self.swipe3 = pygame.transform.scale_by(pygame.image.load('graphics/sword/3.png'),(0.3))
        self.swipe4 = pygame.transform.scale_by(pygame.image.load('graphics/sword/4.png'),(0.3))
        self.swipe5 = pygame.transform.scale_by(pygame.image.load('graphics/sword/5.png'),(0.3))
        self.swipe6 = pygame.transform.scale_by(pygame.image.load('graphics/sword/6.png'),(0.3))
        self.swipe7 = pygame.transform.scale_by(pygame.image.load('graphics/sword/7.png'),(0.3))
        self.swipe8 = pygame.transform.scale_by(pygame.image.load('graphics/sword/8.png'),(0.3))
        self.x = player.rect.center[0]
        self.y = player.rect.center[1]

        self.frames = [self.swipe1, self.swipe2, self.swipe3, self.swipe4, self.swipe5, self.swipe6, self.swipe7, self.swipe8]
        self.index = 0
        self.image = self.frames[self.index]

        self.rect = self.image.get_rect(center = (self.x,self.y))

    def animation(self):
        global is_swipe
        global sword_swipe
        if is_swipe and player.left_side_click:
            self.index += 0.5
            if self.index >= len(self.frames): 
                self.index = 0
                is_swipe = False
                sword_swipe_group.empty()
            self.image = self.frames[int(self.index)]
            self.image = pygame.transform.flip(self.image, True, False)
        elif is_swipe:
            self.index += 0.5
            if self.index >= len(self.frames): 
                self.index = 0
                is_swipe = False
                sword_swipe_group.empty()
            self.image = self.frames[int(self.index)]
    
    def check_move(self):
        if player.left_side_click:
            self.rect.center = (player.rect.center[0]-50, player.rect.center[1])
        else:
            self.rect.center = (player.rect.center[0]+50, player.rect.center[1])
    def update(self):
        self.check_move()
        self.animation()


    





rescale = 800/2160
background = pygame.transform.scale_by(pygame.image.load('graphics/background/game_background_4.png').convert_alpha(),rescale)
background_rocks = pygame.transform.scale_by(pygame.image.load('graphics/background/front_decor.png').convert_alpha(),rescale)

player = Player()
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

sword_swipe_group = pygame.sprite.GroupSingle()


game_run = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     sword_swipe_group.add(sword_swipe)
    if game_run:

        sword_swipe = SwordSwipe()


        screen.blit(background,(0,0))
        player_group.draw(screen)
        player_group.update()
        sword_swipe_group.draw(screen)
        sword_swipe_group.update()
        screen.blit(background_rocks,(0,0))
        clock.tick(60)
        
        pygame.display.update()
    
