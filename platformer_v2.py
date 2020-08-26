# platformer
import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import*
pygame.init()  # initiates pygame
pygame.display.set_caption("platformer")

window_size = (600, 400)

screen = pygame.display.set_mode(window_size, 0, 32)
display = pygame.Surface((300,200))

moving_right = False
moving_left = False
vertical_momentum = 0

game_map = [['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','1','1','0','0',],
            ['0','0','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['2','2','2','2','2','2','2','2','2','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','0','1','1','1','1','1','1','1','2','2','2','1','0','0','0','1','1','1','1','1','1','0','0','0','0',],
            ['0','0','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','1','1','1','1','1','1','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','0','0','0','0','0','0','0','0','0','0','0','0',],
            ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1',]]

grass_img = pygame.image.load('grras.png')
dirt_img = pygame.image.load('dirrt.png')
player_image = pygame.image.load("playerr.png")
#player_image.set_colorkey((55,255,255))
player_rect = pygame.Rect(100,100,5,13)

def collision_test (rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move (rect, movement, tiles):
    collision_types = {"top":False, "bottom":False, "right":False, "left":False}
    rect.x +=movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement [0] > 0:
            rect.right = tile.left
            collision_types["right"] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types["left"] = True
    rect.y +=movement [1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0 :
            rect.bottom = tile.top
            collision_types["bottom"] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types["top"] = True
    return rect, collision_types



#player_location = [50,50]
#player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
#test_rect = pygame.Rect(100,100,100,50)
while True:

    display.fill((145,244,255))

    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile =="1":
                display.blit(dirt_img,(x*16, y*16))
            if tile =="2":
                display.blit(grass_img,(x*16, y*16))
            if tile != "0":
                tile_rects.append(pygame.Rect(x*16, y*16, 16, 16))

            x += 1
        y += 1

    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] +=2
    if moving_left == True:
        player_movement[0] -= 2
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2
    if vertical_momentum > 3:
        vertical_momentum = 3

    player_rect, collisins = move(player_rect, player_movement, tile_rects)

    display.blit(player_image, (player_rect.x, player_rect.y))


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right =  True
            if event.key == K_LEFT:
                moving_left = True
            if event.key == K_UP:
                vertical_momentum = -5

        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False


    screen.blit(pygame.transform.scale(display, window_size), (0,0))
    pygame.display.update()
    clock.tick(60)
