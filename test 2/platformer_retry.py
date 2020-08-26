# platformer
import pygame, sys
clock = pygame.time.Clock()
from pygame.locals import*
pygame.init()  # initiates pygame
pygame.display.set_caption("platformer")

window_size = (400, 400)

screen = pygame.display.set_mode(window_size, 0, 32)


player_image = pygame.image.load("Character 1.png")
moving_right = False
moving_left = False

player_location = [50,50]
vertical_momentum = 0

player_rect = pygame.Rect(player_location[0], player_location[1], player_image.get_width(), player_image.get_height())
test_rect = pygame.Rect(100,100,100,50)
while True:

    screen.fill((145,244,255))
    screen.blit(player_image, player_location)

    if player_location[1] > window_size[1] - player_image.get_height():
        vertical_momentum = - vertical_momentum
    else:
        vertical_momentum += 0.2
    player_location[1] += vertical_momentum

    if moving_right == True:
        player_location[0] +=4
    if moving_left == True:
        player_location[0] -= 4

    player_rect.x = player_location[0]
    player_rect.y = player_location[1]
    if player_rect.colliderect(test_rect):
        pygame.draw.rect(screen,(255,0,0), test_rect)
    else:
        pygame.draw.rect(screen,(0,0,15), test_rect )

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                moving_right =  True
            if event.key == K_LEFT:
                moving_left = True
        elif event.type == KEYUP:
            if event.key == K_RIGHT:
                moving_right = False
            if event.key == K_LEFT:
                moving_left = False


    pygame.display.update()
    clock.tick(60)
