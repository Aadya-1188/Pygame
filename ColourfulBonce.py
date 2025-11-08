import pygame
import random


#INITIALIZE PYGAME
pygame.init

#CUSTOM EVNT ID's
SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2


#bASIC COLORS
BLUE = pygame.Color("blue")
LIGHTBLUE = pygame.Color("lightblue")
DARKBLUE = pygame.Color("darkblue")

#SPRITE COLORS
YELLOW = pygame.Color("yellow")
MAGENTA = pygame.Color("magenta")
ORANGE = pygame.Color("orange")
WHITE = pygame.Color("white")

#moving object
class Sprite(pygame.sprite.Sprite):

    #constructor method
    def __init__(self,color,height,width):
        #call parent class
        super().__init__()
        #create sprite's surface
        self.image = pygame.Surface([width , height])
        self.image.fill(color)
        #define sprite's rect
        self.rect = self.image.get_rect()
        #set initial velocity
        self.velocity = [random.choice([-1 , 1])  , random.choice([-1 , 1])]

    #to update the sprite's position:
    def update(self):
        #move the sprite by its velocity
        self.rect.move_ip(self.velocity)
        #to track weather it hits the boundary
        boundary_hit = False
        #check for colision right or left
        if self.rect.left <= 0 or self.rect.right >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True
        #check for colision bottom or top
        if self.rect.top <= 0 or self.rect.bottom >= 500:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True

        #boundary hit = change color!
        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    #CHANGE SPRITE COLOR
    def change_color(self):
        self.image.fill(random.choice([YELLOW , MAGENTA , ORANGE , WHITE]))
        
    #change background color
    def change_background_color():
        global bg_color
        bg_color = (random.choice([ DARKBLUE , LIGHTBLUE , BLUE]))

all_sprites_list = pygame.sprite.Group()
sp1 = Sprite(WHITE , 20 , 30)

sp1.rect.x = random.randint(0 , 480)
sp1.rect.y = random.randint(0 , 370)
all_sprites_list.add(sp1)

screen = pygame.display.set_mode((500 , 400))
#set the window title
pygame.display.set_caption("Boundary Sprite")
bg_color = BLUE
screen.fill(bg_color)


exit = False
clock = pygame.time.Clock()

while not exit:
    for event in pygame:
        if event.type == pygame.QUIT:
            exit = True
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            change_background_color()
        
        all_sprites_list.update()
