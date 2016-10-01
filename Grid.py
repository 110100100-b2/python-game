import pygame
import sys


pygame.init()
screen= pygame.display.set_mode((600,625))
pygame.display.set_caption=('Tic-Tac-Toe')
black= pygame.Color(0,0,0)


#draw lines
screen.fill((255, 255, 255))
def drawgrid():
    """
   This function draws the grid using rectangles.
   """
    x,y,w,h  = 75,75,150,150
    count = 0
    for i in range(9):
            pygame.draw.rect(screen,black,(x,y,w,h),1)
            x += 150
            count +=1
            if count == 3:
                y += 150
                x = 75
            if count == 6:
                y += 150
                x = 75

drawgrid()
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit() 

pygame.display.flip()
  


