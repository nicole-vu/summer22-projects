import pygame
import random

# creating the data structure for pieces
# setting up global vars
# functions
# - create_grid
# - draw_grid
# - draw_window
# - rotating shape in main
# - setting up the main

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""


# GLOBAL STATIC VARS
S_WIDTH = 800 # screen width
S_HEIGHT = 700 # screen height
PLAY_WIDTH = 300 # meaning 300//10 = 30 width per block
PLAY_HEIGHT = 600 # meaning 600//20 = 30 height per block
BLOCK_SIZE = 30

TOP_LEFT_X = (S_WIDTH - PLAY_WIDTH) // 2
TOP_LEFT_Y = (S_HEIGHT - PLAY_HEIGHT)

# SHAPE FORMATS
# each sublist is a different rotation of the shape, 0 represents the blocks of the actual shape
S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y 
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    # i row, j column
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if (c, r) in locked_pos:
                color = locked_pos[(c, r)]
                grid[r][c] = color
    return grid


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]
    for r, line in enumerate(format):
        row_value = list(line)
        for c, col_value in enumerate(row_value):
            if col_value == '0':
                positions.append((shape.x + c, shape.y + r))

    for r, pos_value in enumerate(positions):
        positions[r] = (pos_value[0] - 2, pos_value[1] - 4) # offset so the shape is centered 

    return positions


def valid_space(shape, grid):
    accepted_pos = [[(c,r) for c in range(10) if grid[r][c] == (0,0,0)] for r in range (20)] # 2D list, add when the pos is empty
    accepted_pos = [j for sub in accepted_pos for j in sub] # flatten to 1D list

    formatted = convert_shape_format(shape)

    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True
            

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def draw_text_middle(text, size, color, surface):
    pass

# draw the lines of the grids
def draw_grid(surface, row, col):
    for r in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (TOP_LEFT_X, TOP_LEFT_Y+r*BLOCK_SIZE), (TOP_LEFT_X+PLAY_WIDTH, TOP_LEFT_Y+r*BLOCK_SIZE)) # horizontal lines
        for c in range(len(grid[r])):
            pygame.draw.line(surface, (128,128,128), (TOP_LEFT_X+c*BLOCK_SIZE, TOP_LEFT_Y), (TOP_LEFT_X+c*BLOCK_SIZE, TOP_LEFT_Y+PLAY_HEIGHT)) # vertical lines


def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('centurygothic', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    # position of the next piece display
    sx = TOP_LEFT_X + PLAY_WIDTH + 50
    sy = TOP_LEFT_Y + PLAY_HEIGHT/2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for r, line in enumerate(format):
        row_value = list(line)
        for c, col_value in enumerate(row_value):
            if col_value == '0':
                pygame.draw.rect(surface, shape.color, (sx+c*BLOCK_SIZE, sy+r*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    surface.blit(label, (sx + 10, sy - 30))


def draw_window(surface):
    surface.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont("centurygothic", 60)
    label = font.render("Tetris", 1, (255,255,255))

    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH/2 - (label.get_width()/2), 30))

    for r in range(len(grid)):
        for c in range(len(grid[r])):
            pygame.draw.rect(surface, grid[r][c], (TOP_LEFT_X + c*BLOCK_SIZE, TOP_LEFT_Y + r*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    pygame.draw.rect(surface, (255,0,0), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 4)

    draw_grid(surface, 20, 10)


def main():
    global grid
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick() # make sure that it runs with the same speed in every computers

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1 # if the piece reached an invalid position, reverse the move
                change_piece = True # call change_piece to lock the position and allow new piece to fall

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not(valid_space(current_piece, grid)):
                        current_piece.rotation -= 1
        
        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                locked_positions[(pos[0], pos[1])] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False

        draw_window(win)
        draw_next_shape(next_piece, win)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False
    
    pygame.display.quit()

def main_menu():
    main()

win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Tetris")

main_menu() # start game