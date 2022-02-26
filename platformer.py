# platformer
import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import*
pygame.init()  # initiates pygame

pygame.display.set_caption("platformer")

window_size = (1200, 500)

screen = pygame.display.set_mode(window_size, 0, 32)

display = pygame.Surface((600, 400))

moving_right = False
moving_left = False
vertical_momentum = 0
#//this is the map we can change everything we want with this map//
game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0',],
            ['0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1','1','1','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',]]
grass_img = pygame.image.load('grass.png')
grass_img = pygame.transform.scale(grass_img,(16,16))
dirt_img = pygame.image.load('dirt.png')
dirt_img = pygame.transform.scale(dirt_img,(16,16))

player_img = pygame.image.load("Character 1.png")
player_rect = pygame.Rect(50,50,1,13) #( , , , player speed)

def collision_test (rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {"top": False, "bottom": False, "right": False, "left": False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0 :
            rect.right = tile.left
            collision_types['right'] = True
            print('left')
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
            print('right')

    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0 :
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types

while True:
    display.fill((255,225,0))

    tile_rect = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '1':
                display.blit(dirt_img, (x*16, y*16))
            if tile == '2':
                display.blit(grass_img, (x*16, y*16))
            if tile_rect != '0':
                tile_rect.append(pygame.Rect(x*16, y*16, 16,16))
            x+=1
        y +=1
    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 2
        print(player_movement)
    if moving_left == True:
        player_movement[0] -= 2
        print(player_movement)
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3 :
        vertical_momentum = 3

    player_rect, collisions = move(player_rect, player_movement, tile_rect)

    #if collisions["bottom"] == True:
        #air_timer =0
    #else:
        #air_timer +=1

    display.blit(player_img, (player_rect.x, player_rect.y))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                moving_left = True
                print("test")
            if event.key == K_RIGHT:
                moving_right = True
                print("test")
            if event.key == K_UP:
                vertical_momentum = -5
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False

    screen.blit(pygame.transform.scale(display, window_size), (0,0))
    pygame.display.update()
    clock.tick(60)
