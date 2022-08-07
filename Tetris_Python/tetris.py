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
S = [[\'.....\',
      \'......\',
      \'..00..\',
      \'.00...\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..00.\',
      \'...0.\',
      \'.....\']]
 
Z = [[\'.....\',
      \'.....\',
      \'.00..\',
      \'..00.\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'.00..\',
      \'.0...\',
      \'.....\']]
 
I = [[\'..0..\',
      \'..0..\',
      \'..0..\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'0000.\',
      \'.....\',
      \'.....\',
      \'.....\']]
 
O = [[\'.....\',
      \'.....\',
      \'.00..\',
      \'.00..\',
      \'.....\']]
 
J = [[\'.....\',
      \'.0...\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..00.\',
      \'..0..\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'...0.\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..0..\',
      \'.00..\',
      \'.....\']]
 
L = [[\'.....\',
      \'...0.\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..0..\',
      \'..00.\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'.0...\',
      \'.....\'],
     [\'.....\',
      \'.00..\',
      \'..0..\',
      \'..0..\',
      \'.....\']]
 
T = [[\'.....\',
      \'..0..\',
      \'.000.\',
      \'.....\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'..00.\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'.....\',
      \'.000.\',
      \'..0..\',
      \'.....\'],
     [\'.....\',
      \'..0..\',
      \'.00..\',
      \'..0..\',
      \'.....\']]

shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y 
        self.shape = shape
        self.color = shape.colors[shape.index(shape)]
        self.rotation = 0

def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    # i row, j column
    for r in range(len(grid)):
        for c in range(len(grid[i])):
            if (c, r) in locked_pos:
                color = locked_pos[(c, r)]
                grid[r][c] = color
    return grid

def convert_shape_format(shape):
    pass

def valid_space(shape, grid):
    pass

def check_lost(positions):
    pass

def get_shape():
    return Piece(5, 0, random.choice(shapes))

def draw_text_middle(text, size, color, surface):
    pass

def draw_grid(surface, row, col):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            pygame.draw.rect(surface, grid[r][c], (TOP_LEFT_X + c*BLOCK_SIZE, TOP_LEFT_Y + r*BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 0)

    pygame.draw.rect(surface, (255,0,0), (TOP_LEFT_X, TOP_LEFT_Y, PLAY_WIDTH, PLAY_HEIGHT), 4)

def clear_rows(grid, locked):
    pass

def draw_next_shape(shape, surface):
    pass

def draw_window(surface):
    surface.fill((0,0,0))

    pygame.font.init()
    font = pygame.font.SysFont("centurygothic", 60)
    label = font.render("Tetris", 1, (255,255,255))

    surface.blit(label, (TOP_LEFT_X + PLAY_WIDTH/2 - (label.get_width()/2), 30))

    draw_grid(suface, grid)
    pygame.display.update()

def main():
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0

    while run:
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
        draw_window(win, grid)

def main_menu(win):
    main(win)

win = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption("Tetris")

main_menu() # start game