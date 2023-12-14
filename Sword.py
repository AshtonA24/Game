import pygame
pygame.mixer.init()
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
        self.rect = self.image.get_rect(center = (0,0))
        self.is_swipe = False
        self.left = False
        self.timer = 0
        self.player_pos_x = 0

        self.woosh = pygame.mixer.Sound("sounds/sword/woosh.mp3")
        self.woosh.set_volume(0.1)
        
    def user_input(self):
        if pygame.mouse.get_pressed()[0] and self.timer < 0:
            print('yuh')
            self.timer = 30
            self.woosh.play()
            self.is_swipe = True
            if pygame.mouse.get_pos()[0] < self.player_pos_x:       
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

sword_swipe = SwordSwipe()
sword_swipe_group = pygame.sprite.GroupSingle()
sword_swipe_group.add(sword_swipe)