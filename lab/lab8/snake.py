import pygame, random
from pygame.math import Vector2

pygame.init()

path = "catch.mp3"
collision_sound = pygame.mixer.Sound(path)

cell_size = 40
cell_number = 20
run = True

x = random.randint(0, cell_number - 1)
y = random.randint(0, cell_number - 1)
pos = Vector2(x, y)

#creating random spot for fruit
def randomize_fruit():
    global pos
    x = random.randint(0, cell_number - 1)
    y = random.randint(0, cell_number - 1)
    pos = Vector2(x, y)

#drawing Fruits
def drawFruits():
    fruit_rect = pygame.Rect((pos.x * cell_size), (pos.y * cell_size), cell_size, cell_size) 
    pygame.draw.rect(screen,(255, 0 , 0), fruit_rect) 



screen = pygame.display.set_mode((cell_size * cell_number, cell_number * cell_size))
pygame.display.set_caption("SNAKE")

#creating SNAKE BODY
global body
body = [Vector2(5, 10), Vector2(4, 10), Vector2(3,10)]
direction = Vector2(1, 0)
global new_BLOCK
new_BLOCK = False


#checking if snake goes out of screen
def check_fail():
    if not 0<=body[0].x <= cell_number-1 or  not 0 <= body[0].y <= cell_number - 1:
        pygame.quit()
        exit()
    for block in body[1:]:      #cheking every block except the head
        if block == body[0]:
            pygame.quit()
            exit()
    

def drawSNAKEBODY():
    for block in body:
        block_rect = pygame.Rect((block.x * cell_size), (block.y * cell_size), cell_size, cell_size)
        pygame.draw.rect(screen,('blue'), block_rect)
def move_SNAKE():
    global new_BLOCK
    global body
    if new_BLOCK == True:
        body_copy = body[:]
        body_copy.insert(0, body_copy[0] + direction)
        body = body_copy[:]
        new_BLOCK = False
    else:
        body_copy = body[:-1]
        body_copy.insert(0, body_copy[0] + direction)
        body = body_copy[:]
def add_block_after_eating():
    global new_BLOCK
    new_BLOCK = True
    
#drawing the score we get per food
game_font = pygame.font.Font(None, 25)

#heart pict
heart_img = pygame.image.load("smallheart.png")
def draw_score():
    score_text = str(len(body) - 3)  #decreasing 3 because initial size of snake is 3 
    score_surface = game_font.render(score_text, True, (56, 74, 12))
    score_x = int(cell_number *cell_size - 60)
    score_y = int(cell_number * cell_size - 40)
    score_rect = score_surface.get_rect(center = (score_x, score_y))
    screen.blit(score_surface, score_rect)
    screen.blit(heart_img,(score_x + 10, score_y - 13 ))
    
    


def Chech_EATING():
    if pos == body[0]:
        randomize_fruit()
        add_block_after_eating()
        print("GOOD")
        collision_sound.play()



SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

level = 150

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SCREEN_UPDATE:
            move_SNAKE()
            Chech_EATING()
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] :
        if direction.x != 1:
            direction = Vector2(-1, 0)
    if keys[pygame.K_RIGHT] :
        if direction.x != -1:
            direction = Vector2(1, 0)
    if keys[pygame.K_UP] :
        if direction.y != 1:
            direction = Vector2(0, -1)
    if keys[pygame.K_DOWN]:
        if direction.y != -1:
            direction = Vector2(0, 1)
    

    screen.fill((167,209,61)) 
    draw_score()
    drawFruits()
    drawSNAKEBODY()
    check_fail()
    pygame.display.update()