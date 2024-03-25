import pygame
import math
import datetime


width , height = 800, 800
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CLOCK")

center_X = width //2
center_Y = height //2

mainpic = pygame.image.load("mainclock.png")
rightarm = pygame.image.load("rightarm.png")
leftarm = pygame.image.load("leftarm.png")

resized_mainpic = pygame.transform.scale(mainpic, (width, height))
right_arm = rightarm.get_rect(center = (center_X, center_Y))
left_arm = leftarm.get_rect(center = (center_X, center_Y))


run = True


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    current_time = datetime.datetime.today()
    
    seconds = current_time.second
    seconds_angle = 360*seconds/60
    
    
    minutes = current_time.minute
    minutes_angle = 360*minutes/60 + seconds_angle/60
    

    rotated_left_arm = pygame.transform.rotate(leftarm, -seconds_angle)
    rotated_left_arm_rect = rotated_left_arm.get_rect(center = ( (center_X, center_Y)))
    
    rotated_right_arm = pygame.transform.rotate(rightarm, -minutes_angle)
    rotated_right_arm_rect = rotated_right_arm.get_rect(center = ( (center_X, center_Y)))

   
    
    screen.fill("black")
    screen.blit(resized_mainpic, (0, 0))
    screen.blit(rotated_left_arm, rotated_left_arm_rect)
    screen.blit(rotated_right_arm, rotated_right_arm_rect)
    
    
    #pygame.draw.line(screen, 'red', (center_X, 0), (center_X, height), 2)
    #pygame.draw.line(screen, 'red', (0, center_Y), (width, center_Y), 2)
    
    
    pygame.display.update()
    
    
pygame.quit()