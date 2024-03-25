import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Circle")

x = 300
y = 300
r = 25
vel = 20


run = True
clock = pygame.time.Clock()
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    clock.tick(60)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 600 - r:
        x += vel
    if keys[pygame.K_UP] and  y > vel:
        y -= vel      
    if keys[pygame.K_DOWN] and y < 600 - r:
        y += vel
     
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen ,("red") , (x, y) , r)

    pygame.display.update()
        
pygame.quit()