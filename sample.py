import pygame,sys,os
from pygame.locals import *


catx=10
caty=10
screen=0

def myquit():
    pygame.quit()
    sys.exit(0)
    
def check_inputs(events):
    global catx,caty,screen
    for event in events:
        if event.type == QUIT:
            quit()
        else:
            if event.type==KEYDOWN:
                if event.key==K_ESCAPE:
                    myquit()
                elif event.key==K_LEFT:
                    catx-=5
                elif event.key==K_RIGHT:
                    catx+=5
                else:
                    print(event.key)
                    
    screen.fill((255,0,0))
    pygame.draw.rect(screen,(50,255,50),(catx,50,50,10))
    pygame.display.update()

def main():
    
    global screen
    pygame.init()
    SCREEN_WIDTH=600
    SCREEN_HEIGHT=480
    window=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    screen=pygame.display.get_surface()
    pygame.display.update()
    while True:
        check_inputs(pygame.event.get())

main()

# red = (50,255,50)

# pygame.init()
 
# window= pygame.display.set_mode((1000,600))
# pygame.display.set_caption('The Snake Game')

# screen = pygame.display.get_surface()
# screen.fill(red)
# pygame.display.set_caption("snake")
# pygame.display.flip()

# while True:
#     for event in pygame.event.get():
#         print(event)
#         if event.type == QUIT:
#             pygame.quit()
#             sys.exit()
#     pygame.display.update()
    
    
    
    