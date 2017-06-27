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
for row in range(10):
    #add empty array
    grid.append([])
    for column in range(11):
        grid[row].append(BLACK)
        
# static Width and Height
WIDTH = 30
HEIGHT = 30

#Distance between cells
MARGIN = 5

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

"""defining the layout"""
def refresh():
    front = [front1,front2,front3]
    left_side = [left1,left2,left3]
    right_side = [right1,right2,right3]
    back = [back1,back2,back3]
    top_row = [top1,top2,top3]
    bottom_row = [bottom1,bottom2,bottom3]
    row1 = [right_side[0],front[0],left_side[0],back[0]]
    row2 = [right_side[1],front[1],left_side[1],back[1]]
    row3 = [right_side[2],front[2],left_side[2],back[2]]
    rows = [row1,row2,row3]
    grid[0][3:5] = top1
    grid[1][3:5] = top2
    grid[2][3:5] = top3
    grid[3] = row1
    grid[4] = row2
    grid[5] = row3
    grid[6][3:5] = bottom3
    grid[7][3:5] = bottom2
    grid[8][3:5] = bottom1

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
    back_row_num = 3 - row_num
    buffer1 = [front[0][row_num],front[1][row_num],front[2][row_num]]
    buffer2 = [top_row[0][row_num],top_row[1][row_num],top_row[2][row_num]]
    buffer3 = [back[2][back_row_num],back[1][back_row_num],back2[0][back_row_num]]
    buffer4 = [bottom_row[2][row_num],bottom_row[1][row_num],bottom_row[0][row_num]]

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
    back_row_num = 3 - row_num
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
    back_row_num = 3 - row_num
    buffer1 = [left_side[0][row_num],left_side[1][row_num],left_side[2][row_num]]
    buffer2 = [top_row[row_num]]
    buffer3 = [right_side[2][back_row_num],right_side[1][back_row_num],right_side[0][back_row_num]]
    buffer4 = [bottom_row[row_num]]

    left_side[0][row_num] = buffer4[0]
    left_side[1][row_num] = buffer4[1]
    left_side[2][row_num] = buffer4[2]

    top_row[row_num][0] = buffer1[0]
    top_row[row_num][1] = buffer1[1]
    top_row[row_num][2] = buffer1[2]

    right[2][back_row_num] = buffer2[0]
    right[1][back_row_num] = buffer2[1]
    right[0][back_row_num] = buffer2[2]

    bottom_row[row_num][0] = buffer3[0]
    bottom_row[row_num][1] = buffer3[1]
    bottom_row[row_num][2] = buffer3[2]

def side_down(row_num): 
    row_num = row_num - 1
    back_row_num = 3 - row_num
    buffer1 = [left_side[0][row_num],left_side[1][row_num],left_side[2][row_num]]
    buffer2 = [top_row[row_num]]
    buffer3 = [right_side[2][back_row_num],right_side[1][back_row_num],right_side[0][back_row_num]]
    buffer4 = [bottom_row[row_num]]

    left_side[0][row_num] = buffer2[0]
    left_side[1][row_num] = buffer2[1]
    left_side[2][row_num] = buffer2[2]

    top_row[row_num][0] = buffer3[0]
    top_row[row_num][1] = buffer3[1]
    top_row[row_num][2] = buffer3[2]

    right[2][back_row_num] = buffer4[0]
    right[1][back_row_num] = buffer4[1]
    right[0][back_row_num] = buffer4[2]

    bottom_row[row_num][0] = buffer1[0]
    bottom_row[row_num][1] = buffer1[1]
    bottom_row[row_num][2] = buffer1[2]


    
"""defining rotations"""
def rotate(row,direction):
    direction = direction.lower()
    if row <= 3 and row > 0:
        if direction == 'left' or direction =='l':
            buffer1 = rows[row][0] #Buffer exists in order to ensure no data is lost
            rows[row][0] = rows[row][3]
            rows[row][3] = rows[row][2]
            rows[row][2] = rows[row][1]  #rotates all left
            rows[row][1] = buffer1
            if row == 1: #checks if top row
                top_row = face_left(top_row)
            elif row == 3: #checks for bottom row
                bottom_row = face_right(bottom_row)
        elif direction == 'right' or direction =='r':
            buffer1 = rows[row][0]
            rows[row][0] = rows[row][1]
            rows[row][1] = rows[row][2]
            rows[row][2] = rows[row][3]
            rows[row][3] = buffer1
            if row == 1: #checks if top
                top_row = face_right(top_row)
            if row == 3: #checks if bottom row
                bottom_row = face_left(bottom_row)
        else:
            print 'command not recognised'
    elif 3<row<=6:
        if direction == 'up' or direction == 'u':
            up(row)
            if row == 4:
                left_side = face_right(left_side)
            elif row == 6:
                right_side = face_left(right_side)
        if direction  =='down' or direction == 'd':
            down(row)
            if row == 4:
                left_side = face_left(left_side)
            elif row == 6:
                right_side = face_right(right_side)
        else:
            print 'command not recognised'
    elif 6<row<=9:
        if direction == 'up' or direction == 'u':
            if row == 7:
                side_up(1) #uses slightly modified up function code
                front = face_left(front)
            elif row == 8:
                side_up(2)
            elif row == 9:
                side_up(3)
                back = face_right(back)
        if direction == 'down' or direction == 'd':
            if row == 7:
                side_down(1) #uses slightly modified down function code
                front = face_right(front)
            elif row == 8:
                side_down(2)
            elif row == 9:
                side_down(3)
                back = face_left(back)
            else:
                print 'command not recognised'
    else:
        print 'number out of bounds'

refresh()
#starting pygame
pygame.init()

#Setting window dimensions
WINDOW_SIZE = [425,320]
screen = pygame.display.set_mode(WINDOW_SIZE)

#Giving window a title
pygame.display.set_caption("Rubicks Cube in python test v0.0001")

#manage refresh rate

clock = pygame.time.Clock()

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
    screen.fill(BLACK)
    refresh()

    #draw grid
    for row in range(10):
        for column in range(11):
            Color = grid[row][column]
            pygame.draw.rect(screen,Color,
                             [((MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN),
                              (WIDTH ,HEIGHT)])
    clock.tick(60)

    pygame.display.flip()
        
        
pygame.quit()
"""for i in range(10):
    print grid[i]"""
