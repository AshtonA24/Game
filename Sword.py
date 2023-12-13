import pygame
from Main import player
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