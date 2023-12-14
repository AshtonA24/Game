import pygame, math, Player, Sword, Projectiles, Enemies
from random import randint

pygame.init()
screen = pygame.display.set_mode((1400,800))
pygame.display.set_caption("GAME")
clock = pygame.time.Clock()
waves_complete = 0
game_run = False
text_font = pygame.font.Font('graphics/fonts/old.ttf',70)

def check_all_collisions():
    #check sword collisions
    if sword_swipe.is_swipe:
        for enemy in enemy_group:
            if sword_swipe.rect.colliderect(enemy.rect) and enemy.i_frame_timer < 0:
                enemy.health -= 25
                enemy.i_frame_timer = 30
    if pygame.sprite.spritecollide(Player.player, projectile_group, True): Player.player.dead = True
    
def update_sword_class():
        sword_swipe.player_pos_x = Player.player.rect.center[0]
        if sword_swipe.left:
            sword_swipe.rect.midright = (Player.player.rect.midleft[0], Player.player.rect.center[1])
        else:
            sword_swipe.rect.midleft = (Player.player.rect.midright[0], Player.player.rect.center[1])

def restart_game():
    global game_run, enemy_group
    game_run = True
    enemy_group.empty()

    Player.player.rect.center = (700,500)
    Player.player.dead = False
    Player.player.full_dead = False
    enemy_group.add(Enemies.Ogre(True))
    enemy_group.add(Enemies.Mage(False))
    # enemy_group.add(Ogre(False))
    # enemy_group.add(Ogre(True))

def show_hitboxes(show):
    if show:
        for enemy in enemy_group:
            pygame.draw.rect(screen, (255,0,0), enemy.rect, 1)
            pygame.draw.rect(screen, (255,0,255), enemy.attack_rect, 1)
        for projectile in projectile_group:
            pygame.draw.rect(screen, (0,255,0), projectile.rect, 1)
        pygame.draw.rect(screen, (0,0,255), Player.player.rect, 1) 
        pygame.draw.rect(screen, (0,255,0), sword_swipe.rect, 1)

def move_enemy():
    for enemy in enemy_group:
        prev = enemy.rect.center 
        
        x = enemy.rect.center[0] - Player.player.rect.center[0]
        y = enemy.rect.center[1] - Player.player.rect.center[1]
        angle = math.atan2(y, x)
        speed = enemy.speed
        move_x = speed * math.cos(angle)
        move_y = speed * math.sin(angle)

        #checks direction for later
        if x < 0: enemy.left = False
        else: enemy.left = True

        if enemy.attacking: enemy.moving = False
        else: enemy.moving = True


        # Calculate the new position based on the angle and speed
        if enemy.moving:
            enemy.rect.x -= move_x
            enemy.rect.y -= move_y

        for enemy2 in enemy_group:
            if pygame.sprite.collide_rect(enemy, enemy2) and enemy != enemy2:
                enemy.rect.center = prev
        
    

#blackground
rescale = 800/2160
background = pygame.transform.scale_by(pygame.image.load('graphics/background/game_background_4.png').convert_alpha(),rescale)
background_rocks = pygame.transform.scale_by(pygame.image.load('graphics/background/front_decor.png').convert_alpha(),rescale)

#initializing classes
player_group = Player.player_group
enemy_group = Enemies.enemy_group
projectile_group = Projectiles.projectile_group

sword_swipe = Sword.sword_swipe
sword_swipe_group = Sword.sword_swipe_group


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
        check_all_collisions()
        move_enemy()
        enemy_group.update()
        enemy_group.draw(screen)
        player_group.update()
        player_group.draw(screen)
        projectile_group.update()
        projectile_group.draw(screen)
        update_sword_class()
        sword_swipe_group.update()
        sword_swipe_group.draw(screen)
        screen.blit(background_rocks,(0,0))

        #draw health bars
        for enemy in enemy_group:
            pygame.draw.rect(screen, (255,255,255), enemy.white_rect)
            pygame.draw.rect(screen, (0,255,0), enemy.green_rect)
        show_hitboxes(False)
        if Player.player.full_dead: game_run = False
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
        
        
    
