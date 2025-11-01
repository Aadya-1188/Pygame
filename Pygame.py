#Import nessesary Libraries
import pygame

#Initialize
pygame.init()

#Setup windoe geometry
screen = pygame.display.set_mode((400 , 500))

#Create a loop

done = False

while not done :

    #clear the event queue
    for event in pygame:
            if event.type == pygame.Quit:
                  pygame.quit()

    #Make th changes Visible
    pygame.display.flip()