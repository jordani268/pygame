import pygame

pygame.init()

S_WIDTH = 1920
S_HEIGHT = 1080

screen = pygame.display.set_mode((S_WIDTH, S_HEIGHT)) # screen

player = pygame.Rect((300, 200, 50, 50))

running = True 

while running: # game loop
    screen.fill((0,0,0))
    pygame.draw.rect (screen, (122, 5, 255), player)
    key = pygame.key.get_pressed()

    pygame.display.set_caption("Purple hand")
    if key[pygame.K_w] == True:
        player.move_ip(0, -1)
    elif key[pygame.K_a] == True:
        player.move_ip(-1, 0)
    elif key[pygame.K_s] == True:
        player.move_ip(0, 1)
    elif key[pygame.K_d] == True:
        player.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # event handler
            running = False

    pygame.display.update()

pygame.quit()