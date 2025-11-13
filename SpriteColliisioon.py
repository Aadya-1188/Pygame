import pygame
import random

#Contanats
SCREEN_WIDTH , SCREEN_HEIGHT = 500 , 400
MOVEMENT_SPEED = 5
FONT_SIZE = 72

pygame.init()

background_image  = pygame.transform.scale(pygame.imgae.load("bg.jpeg") ,
                                            (SCREEN_WIDTH , SCREEN_HEIGHT))

font = pygame.font.SysFont("Times New Roman" , FONT_SIZE)

class Sprite(pygame.sprite.Sprite):
    
    def __init__(self , color , height , width):
        super().__init__()
        self.image = pygame.Surface([width , height])
        self.image.fill(
            pygame.color("dogerblue"))
        pygame.draw.rect(self.image , color , pygame.Rect(0 , 0 , width , height))
        self.rect = self.image.get_rect()

    def move(self , x_change , y_change):
        self.rect.x = max(
            min (self.rect.x + x_change  , SCREEN_WIDTH - self.rect.width)  , 0)
        
        self.rect.y = max(
            min (self.rect.y + y_change  , SCREEN_HEIGHT - self.rect.height)  , 0)
        

    #setup
    screen = pygame.display.set_mode((SCREEN_WIDTH , SCREEN_HEIGHT))
    pygame.display.set_caption("Sprite Collision")

    all_sprites = pygame.sprite.Group()

    #create sprites
    sprite1 = Sprite(pygame.Color("Black") , 20 , 30)
    sprite1.rect.x , sprite1.rect.width  = random.radint(
    0 , SCREEN_HEIGHT - sprite1.rect.height) 

    all_sprites.add(sprite1)


    #create sprites
    sprite2 = Sprite(pygame.Color("red") , 20 , 30)
    sprite1.rect.x , sprite2.rect.width  = random.radint(
    0 , SCREEN_HEIGHT - sprite2.rect.height) 

    all_sprites.add(sprite2)

    #Game loop variables
    running , won = True , False
    clock = pygame.time.clock()

    #main game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN )