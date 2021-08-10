import pygame

#initialising pygame and its functions 
pygame.init()

# creating game window and title
screen = pygame.display.set_mode((300,300))

SAFFRON=(255, 153, 51)
saffron_rect=pygame.Rect(50,100,200,30)

WHITE=(255,255,255)
white_rect=pygame.Rect(50,125,200,30)

GREEN=(34, 139, 34)
green_rect=pygame.Rect(50,150,200,30)


while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.draw.rect(screen,SAFFRON,saffron_rect)
    pygame.draw.rect(screen,WHITE,white_rect)
    pygame.draw.rect(screen,GREEN,green_rect)
    
    pygame.display.update()