x = 200
y = 50

import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (60, 186, 84)
RED = (219, 50, 54)
BLUE = (72, 133, 237)
YELLOW = (244, 194, 13)

screen= pygame.display.set_mode((600,625))

 
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 150
HEIGHT = 150
 
# This sets the margin between each cell
MARGIN = 5
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(3):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(3):
        grid[row].append(0)  # Append a cell
 
# Set row 2, cell 2 to one. (Remember rows and
# column numbers start at zero.)
#grid[1][1] = 1
 
# Initialize pygame
pygame.init()
pygame.font.init()

 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [600, 625]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Tic-Tac-Toe")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#Player turn
player = 1


current_pos = [1,1]
current_color = GREEN



# initialize font; must be called after 'pygame.init()' to avoid 'Font not Initialized' error
myfont = pygame.font.Font(None, 24)

# render text
notification = myfont.render("Let's get started!", 1, (255,255,255))



#surface = pygame.image.load('foo.png')

def updateNotification(notification_object, text, screen):
    notification_object = myfont.render(text, 1, (255,255,255))
    screen.blit(notification_object, (225, 625-60))    


def moveSelector(key, grid, current_pos):
    #Returns a 2-tuple (color, current_pos)
    if key == 'up':
        if (current_pos[1] - 1 >= 0):
            if (grid[current_pos[0]][current_pos[1] -1] == 0):
                current_pos[1] -= 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[1] -= 1
                return(current_pos, RED) # Make Red               


    
    elif key == 'down':
        if (current_pos[1] + 1 <= 2):
            if (grid[current_pos[0]][current_pos[1] +1] == 0):
                current_pos[1] += 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[1] += 1
                return(current_pos, RED) # Make Red  

    
    elif key == 'left':
        if (current_pos[0] - 1 >= 0):
            if (grid[current_pos[0] - 1][current_pos[1]] == 0):
                current_pos[0] -= 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[0] -= 1
                return(current_pos, RED) # Make Red  
       
        

    elif key == 'right':
        if (current_pos[0] + 1 <= 2):
            if (grid[current_pos[0] + 1][current_pos[1]] == 0):
                current_pos[0] += 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[0] += 1
                return(current_pos, RED) # Make Red  
    
        

         

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  

            
        elif event.type == pygame.KEYDOWN:            
            
            """Player 1 Controls"""
            
            if event.key == pygame.K_UP:
                if (player == 1 and current_pos[1] != 0):
                    data = moveSelector('up', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                elif current_pos[1] == 0:
                    notification = myfont.render('You cannot move further up', 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
                else:
                    notification = myfont.render("It is player 2's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
                
            elif event.key == pygame.K_DOWN:
                if (player == 1 and current_pos[1] != 2):
                    data = moveSelector('down', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                elif current_pos[1] == 2:
                    notification = myfont.render("You cannot move further down", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))               
                else:
                    notification = myfont.render("It is player 2's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
            elif event.key == pygame.K_LEFT:
                if (player == 1 and current_pos[0] != 0):
                    data = moveSelector('left', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                elif current_pos[0] == 0:
                    notification = myfont.render("You cannot move further left", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))                
                else:
                    notification = myfont.render("It is player 2's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
            elif event.key == pygame.K_RIGHT:
                if (player == 1 and current_pos[0] != 2):
                    data = moveSelector('right', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                    print(current_pos)
                elif current_pos[0] == 2:
                    notification = myfont.render("You cannot move further right", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))               
                else:
                    notification = myfont.render("It is player 2's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))    
                    
                    
             #Player 2 Controls
            
            
            if event.key == pygame.K_w:
                if (player == 2 and current_pos[1] != 0):
                    data = moveSelector('up', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                elif current_pos[1] == 0:
                    notification = myfont.render("You cannot move further up", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
                else:
                    notification = myfont.render("It is player 1's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
                
            elif event.key == pygame.K_s:
                if (player == 2 and current_pos[1] != 2):
                    data = moveSelector('down', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                elif current_pos[1] == 2:
                    notification = myfont.render("You cannot mvoe further down", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))               
                else:
                    notification = myfont.render("It is player 1's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
            elif event.key == pygame.K_a:
                if (player == 2 and current_pos[0] != 0):
                    data = moveSelector('left', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                elif current_pos[0] == 0:
                    notification = myfont.render("You cannot move further left", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))                
                else:
                    notification = myfont.render("It is player 1's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))
            elif event.key == pygame.K_d:
                if (player == 2 and current_pos[0] != 2):
                    data = moveSelector('right', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                    print(current_pos)
                elif current_pos[0] == 2:
                    notification = myfont.render("You cannot move further right", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))              
                else:
                    notification = myfont.render("It is player 1's turn", 1, (255,255,255))
                    screen.blit(notification, (225, 625-60))               
                        
           
            if event.key == pygame.K_RETURN:
                if (player == 1):
                    grid[current_pos[0]][current_pos[1]] = 1
                    player = 2
                else:
                    grid[current_pos[0]][current_pos[1]] = 2
                    player = 1
                   
            
 
    # Set the screen background
    screen.fill(BLACK)
    # Updating notification
    screen.blit(notification, (225, 625-60))
    
    # Draw the grid
    for row in range(3):
        for column in range(3):
            color = WHITE
            if (row == current_pos[1] and column == current_pos[0]):
                color = current_color
            elif grid[column][row] == 1: #This convention is kind of backwards because of the way cartesian co-ordinates are switched with inex notation aij
                color = BLUE
            elif grid[column][row] == 2:
                color = YELLOW           
            pygame.draw.rect(screen,
                             color,
                             [50+(MARGIN + WIDTH) * column + MARGIN,
                              75+(MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()



"""IMPORTANT"""

#Key Bindings to Grid:

#Up = -1 (for Row), bound = 0
#Down = +1 (for Row), bound = 2
#Left = -1 (for Column), bound = 0
#Right = +1 (for Column), bound = 2


def printX_s(grid):
    # Take a look at grid values and load images onto x-y co-ordinates
    pass

def printO_s(grid):
    # Take a look at grid values and load images onto x-y co-ordinates
    pass


