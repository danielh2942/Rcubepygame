import pygame
"""
Rubicks cube in python 
test
version 0.001
2017 Daniel Hannon


Layout

      top1
      top2
      top3
left1 front1 right1 back1
left2 front2 right2 back2
left3 front3 right3 back3
      bottom3
      bottom2
      bottom1

"""
 
# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (248, 156, 83)
"""BLACK = 'B'
WHITE = 'W'
RED = 'R'
GREEN = 'G'
BLUE = 'B'
YELLOW = 'Y'
ORANGE = 'O'"""

#Game grid
grid = []
for row in range(13):
    #add empty array
    grid.append([])
    for column in range(12):
        grid[row].append(BLACK)
        
# static Width and Height
WIDTH = 30
HEIGHT = 30

#Distance between cells
MARGIN = 5

#filler

filler = [BLACK,BLACK,BLACK]

""" Defining front """
front1 = [RED, RED, RED]
front2 = [RED, RED, RED]
front3 = [RED, RED, RED]
front = [front1,front2,front3]

"""defining left side """
left1 = [YELLOW, YELLOW, YELLOW]
left2 = [YELLOW, YELLOW, YELLOW]
left3 = [YELLOW, YELLOW, YELLOW]
left_side = [left1,left2,left3]

"""defining right side"""
right1 = [GREEN, GREEN, GREEN]
right2 = [GREEN, GREEN, GREEN]
right3 = [GREEN, GREEN, GREEN]
right_side = [right1,right2,right3]

"""defining back"""
back1 = [BLUE, BLUE, BLUE]
back2 = [BLUE, BLUE, BLUE]
back3 = [BLUE, BLUE, BLUE]
back = [back1,back2,back3]

"""defining top"""
top1 = [ORANGE, ORANGE, ORANGE]
top2 = [ORANGE, ORANGE, ORANGE]
top3 = [ORANGE, ORANGE, ORANGE]
top_row = [top1,top2,top3]

"""defining bottom"""
bottom1 = [WHITE, WHITE, WHITE]
bottom2 = [WHITE, WHITE, WHITE]
bottom3 = [WHITE, WHITE, WHITE]
bottom_row = [bottom1,bottom2,bottom3]

"""rows"""
row1 = left_side[0] + front[0] + right_side[0] + back[0]
row2 = left_side[1] + front[1] + right_side[1] + back[1]
row3 = left_side[2] + front[2] + right_side[2] + back[2]
rows = [row1,row2,row3]

#Functions
"""Up down conditional for top and bottom for left/right movements of top only"""

def up_down_conditional(row):
    if row == 0:
        return 9
    elif row == 1:
        return 8
    elif row == 2:
        return 7
    elif row == 6:
        return 7
    elif row == 7:
        return 8
    elif row == 8:
        return 9

"""defining the layout"""
def refresh():
    front = [front1,front2,front3]
    left_side = [left1,left2,left3]
    right_side = [right1,right2,right3]
    back = [back1,back2,back3]
    top_row = [top1,top2,top3]
    bottom_row = [bottom1,bottom2,bottom3]
    row1 = left_side[0] + front[0] + right_side[0] + back[0]
    row2 = left_side[1] + front[1] + right_side[1] + back[1]
    row3 = left_side[2] + front[2] + right_side[2] + back[2]
    rows = [row1,row2,row3]
    grid[0] = filler + top1 + filler + filler
    grid[1] = filler + top2 + filler + filler
    grid[2] = filler + top3 + filler + filler
    grid[3] = rows[0]
    grid[4] = rows[1]
    grid[5] = rows[2]
    grid[6] = filler + bottom3 + filler + filler
    grid[7] = filler + bottom2 + filler + filler
    grid[8] = filler + bottom1 + filler + filler
    grid[9][6] = (255,0,0)
    grid[10][5] = (255,0,0)
    grid[10][7] = (255,0,0)
    grid[11][6] = (255,0,0)


"""Face rotations"""
def face_left(row):
    buffer1 = row[2]
    buffer2 = row[1]
    buffer3 = row[0]
    row[0] = [buffer1[0],buffer2[0],buffer3[0]]
    row[1] = [buffer1[1],buffer2[1],buffer3[1]]
    row[2] = [buffer1[2],buffer2[2],buffer3[2]]

def face_right(row):
    buffer1 = row[2]
    buffer2 = row[1]
    buffer3 = row[0]
    row[0] = [buffer1[2],buffer2[2],buffer3[2]]
    row[1] = [buffer1[1],buffer2[1],buffer3[1]]
    row[2] = [buffer1[0],buffer2[0],buffer3[0]]

"""
up/down side rotations
these can NOT be used for rows 7, 8, or 9 as those include eight lists rather than 12
"""

"""Bringing side up"""
def up(row_num): 
    row_num = row_num - 1
    back_row_num = 2 - row_num
    buffer1 = [front[0][row_num],front[1][row_num],front[2][row_num]]
    buffer2 = [top_row[0][row_num],top_row[1][row_num],top_row[2][row_num]]
    buffer3 = [back[2][back_row_num],back[1][back_row_num],back2[0][back_row_num]]
    buffer4 = [bottom_row[0][row_num],bottom_row[1][row_num],bottom_row[2][row_num]]

    front[0][row_num] = buffer4[0]
    front[1][row_num] = buffer4[1]
    front[2][row_num] = buffer4[2]

    top_row[0][row_num] = buffer1[0]
    top_row[1][row_num] = buffer1[1]
    top_row[2][row_num] = buffer1[2]

    back[2][back_row_num] = buffer2[0]
    back[1][back_row_num] = buffer2[1]
    back[0][back_row_num] = buffer2[2]

    bottom_row[0][row_num] = buffer3[0]
    bottom_row[1][row_num] = buffer3[1]
    bottom_row[2][row_num] = buffer3[2]

"""Bringing side down"""
def down(row_num): 
    row_num = row_num - 1
    back_row_num = 2 - row_num
    buffer1 = [front[0][row_num],front[1][row_num],front[2][row_num]]
    buffer2 = [top_row[0][row_num],top_row[1][row_num],top_row[2][row_num]]
    buffer3 = [back[2][back_row_num],back[1][back_row_num],back2[0][back_row_num]]
    buffer4 = [bottom_row[2][row_num],bottom_row[1][row_num],bottom_row[0][row_num]]

    front[0][row_num] = buffer2[0]
    front[1][row_num] = buffer2[1]
    front[2][row_num] = buffer2[2]

    top_row[0][row_num] = buffer3[0]
    top_row[1][row_num] = buffer3[1]
    top_row[2][row_num] = buffer3[2]

    back[2][back_row_num] = buffer4[0]
    back[1][back_row_num] = buffer4[1]
    back[0][back_row_num] = buffer4[2]

    bottom_row[0][row_num] = buffer1[0]
    bottom_row[1][row_num] = buffer1[1]
    bottom_row[2][row_num] = buffer1[2]

"""Rows 7 - 9 up/down rotations"""

def side_up(row_num): 
    row_num = row_num - 1
    back_row_num = 2 - row_num
    buffer1 = [left_side[0][row_num],left_side[1][row_num],left_side[2][row_num]]
    buffer2 = top_row[row_num]
    buffer3 = [right_side[2],right_side[1],right_side[0]]
    buffer4 = bottom_row[row_num]

    left_side[0][row_num] = buffer4[0]
    left_side[1][row_num] = buffer4[1]
    left_side[2][row_num] = buffer4[2]

    top_row[row_num][0] = buffer1[0]
    top_row[row_num][1] = buffer1[1]
    top_row[row_num][2] = buffer1[2]

    right_side[0][row_num] = buffer2[0]
    right_side[1][row_num] = buffer2[1]
    right_side[2][row_num] = buffer2[2]

    bottom_row[row_num][0] = buffer3[0]
    bottom_row[row_num][1] = buffer3[1]
    bottom_row[row_num][2] = buffer3[2]

def side_down(row_num): 
    row_num = row_num - 1
    back_row_num = 2 - row_num
    buffer1 = [left_side[0][row_num],left_side[1][row_num],left_side[2][row_num]]
    buffer2 = top_row[row_num]
    buffer3 = [right_side[2][back_row_num],right_side[1][back_row_num],right_side[0][back_row_num]]
    buffer4 = bottom_row[row_num]

    left_side[0][row_num] = buffer2[0]
    left_side[1][row_num] = buffer2[1]
    left_side[2][row_num] = buffer2[2]

    top_row[row_num][0] = buffer3[0]
    top_row[row_num][1] = buffer3[1]
    top_row[row_num][2] = buffer3[2]

    right_side[0][back_row_num] = buffer4[0]
    right_side[1][back_row_num] = buffer4[1]
    right_side[2][back_row_num] = buffer4[2]

    bottom_row[row_num][0] = buffer1[0]
    bottom_row[row_num][1] = buffer1[1]
    bottom_row[row_num][2] = buffer1[2]


    
"""defining rotations"""
def rotate(row,direction):
    if row <= 3 and row > 0:
        row = row - 1
        if direction == 'left':
            buffer1 = rows[row][0] #Buffer exists in order to ensure no data is lost
            print rows[row]
            rows[row][0] = rows[row][3]
            rows[row][3] = rows[row][2]
            rows[row][2] = rows[row][1]  #rotates all left
            rows[row][1] = buffer1
            print rows[row]
            if row == 1: #checks if top row
                top_row = face_left([top1,top2,top3])
            elif row == 3: #checks for bottom row
                bottom_row = face_right([bottom1,bottom2,bottom3])
        elif direction == 'right':
            buffer1 = rows[row][0]
            rows[row][0] = rows[row][1]
            rows[row][1] = rows[row][2]
            rows[row][2] = rows[row][3]
            rows[row][3] = buffer1
            if row == 1: #checks if top
                top_row = face_right([top1,top2,top3])
            if row == 3: #checks if bottom row
                bottom_row = face_left([bottom1,bottom2,bottom3])
            
        else:
            return False
    elif 3<row<=6:
        if direction == 'up':
            if row == 4:
                up(1)
                left_side = face_right([left1,left2,left3])
            elif row == 5:
                up(2)
            elif row == 6:
                up(3)
                right_side = face_left([right1,right2,right3])
        if direction  =='down':
            down(row)
            if row == 4:
                left_side = face_left([left1,left2,left3])
            elif row == 6:
                right_side = face_right([right1,right2,right3])
        else:
            return False
    elif 6<row<=9:
        if direction == 'up':
            if row == 7:
                side_up(3) #uses slightly modified up function code
                front = face_left([front1,front2,front3])
            elif row == 8:
                side_up(2)
            elif row == 9:
                side_up(1)
                back = face_right([back1,back2,back3])
        if direction == 'down':
            if row == 7:
                side_down(3) #uses slightly modified down function code
                front = face_right([front1,front2,front3])
            elif row == 8:
                side_down(2)
            elif row == 9:
                side_down(1)
                back = face_left([back1,back2,back3])
            else:
                return False
    else:
        return False

refresh()
#starting pygame
pygame.init()

#Setting window dimensions
WINDOW_SIZE = [425,460]
screen = pygame.display.set_mode(WINDOW_SIZE)

#Giving window a title
pygame.display.set_caption("Rubicks Cube in python test v0.0001")

#manage refresh rate

clock = pygame.time.Clock()
command = [0,0]
#variable that declares whether the game is running or not
stopped = False
while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            if row == 10 and column == 5:
                command[0] = "left"
            if row == 10 and column == 7:
                command[0] = "right"
            if row == 9 and column == 6:
                command[0] = "up"
            if row == 11 and column == 6:
                command[0] = "down"

            if (row == 0 or row == 1 or row == 2) and column > 2 and column < 6:
                command[1] = 9
                if command[0] == "left":
                    command[0] = "down"
                    command[1] = up_down_conditional(row)
                elif command[0] == "right":
                    command[0] = "up"
                    command[1] = up_down_conditional(row)
                elif command[0] == "up":
                    if column == 3:
                        command[1] = 4
                    if column == 4:
                        command[1] = 5
                    if column == 5:
                        command[1] = 6
            elif row == 3 or row == 4 or row == 5:
                if command[0] == "left":
                    if row == 3:
                        command[1] = 1
                    if row == 4:
                        command[1] = 2
                    if row == 5:
                        command[1] = 3
    if command[0] != 0 and command[1] != 0:
        rotate(command[1],command[0])
        print command
        command = [0,0]
    refresh()

    #draw grid
    for row in range(13):
        for column in range(12):
            Color = grid[row][column]
            pygame.draw.rect(screen,Color,[((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN),(WIDTH ,HEIGHT)])
    clock.tick(60)

    pygame.display.flip()
        
        
pygame.quit()
"""for i in range(10):
    print grid[i]"""
