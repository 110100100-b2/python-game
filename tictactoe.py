import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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
        else:
            pass #i.e. do not move selector

    
    elif key == 'down':
        if (current_pos[1] + 1 <= 2):
            if (grid[current_pos[0]][current_pos[1] +1] == 0):
                current_pos[1] += 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[1] += 1
                return(current_pos, RED) # Make Red  
        else:
            pass #i.e. do not move selector        

    
    elif key == 'left':
        if (current_pos[0] - 1 >= 0):
            if (grid[current_pos[0] - 1][current_pos[1]] == 0):
                current_pos[0] -= 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[0] -= 1
                return(current_pos, RED) # Make Red  
        else:
            pass #i.e. do not move selector        
        

    elif key == 'right':
        if (current_pos[0] + 1 <= 2):
            if (grid[current_pos[0] + 1][current_pos[1]] == 0):
                current_pos[0] += 1
                return(current_pos, GREEN) # Make Green
            else:
                current_pos[0] += 1
                return(current_pos, RED) # Make Red  
        else:
            pass #i.e. do not move selector        
        

         
#Returns (new_pos, color)




# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            
            # Set that location to one or two depending on wheter it's been clicked before.
            if (grid[row][column] == 0):                
                grid[row][column] = 1
            else:
                grid[row][column] = 2
            print("Click ", pos, "Grid coordinates: ", row, column)
            
        elif event.type == pygame.KEYDOWN:            
            
            """Player 1 Controls"""
            
            if event.key == pygame.K_UP:
                if (player == 1):
                    data = moveSelector('up', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                else:
                    print('It is player 2 turn')
                
            elif event.key == pygame.K_DOWN:
                if (player == 1):
                    data = moveSelector('down', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                else:
                    print('It is player 2 turn')
            elif event.key == pygame.K_LEFT:
                if (player == 1):
                    data = moveSelector('left', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                else:
                    print('It is player 2 turn')
            elif event.key == pygame.K_RIGHT:
                if (player == 1):
                    data = moveSelector('right', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                    print(current_pos)
                else:
                    print('It is player 2 turn')            
            
            
            
                 
            #Player 2 Controls
             
            elif event.key == pygame.K_w:
                if (player == 2):
                    data = moveSelector('up', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                    
                else:
                    print('It is player 1 turn')
                
            elif event.key == pygame.K_s:
                if (player == 2):
                    data = moveSelector('down', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                else:
                    print('It is player 1 turn')
            elif event.key == pygame.K_a:
                if (player == 2):
                    data = moveSelector('left', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1] 
                else:
                    print('It is player 1 turn')
            elif event.key == pygame.K_d:
                if (player == 2):
                    data = moveSelector('right', grid, current_pos)
                    current_pos = data[0]
                    current_color = data[1]
                else:
                    print('It is player 1 turn') 
                    
            
                    
            
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(3):
        for column in range(3):
            color = WHITE
            if (row == current_pos[1] and column == current_pos[0]):
                color = current_color
            elif grid[row][column] == 1:
                color = GREEN
            elif grid[row][column] == 2:
                color = RED            
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
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


