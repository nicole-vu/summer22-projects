import numpy as np
import pygame
import sys

# board dimensions
ROW_COUNT = 6
COLUMN_COUNT = 7

P1_COLOR = (0,255,0)
P2_COLOR = (255,0,0)
BOARD_COLOR = (0,0,255)
SCREEN_COLOR = (0,0,0)

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) # create a zero matrix of 6 rows and 7 columns
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

# check if the chosen column still have space for the next move
def is_valid_location(board, col):
    return board[0][col] == 0

# find the bottom most empty slot in a column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[ROW_COUNT - r - 1][col] == 0:
            return ROW_COUNT - r - 1

# print board in the descending order
def print_board(board):
    print(np.flip(board,0))

def winning_move(board, piece):
    # check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True

    # check vertical locations for win
    for r in range(ROW_COUNT-3):
        for c in range(COLUMN_COUNT):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # check positively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):    
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True

    # check negatively sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):    
            if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
                return True

def draw_board(board):
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            pygame.draw.rect(screen, BOARD_COLOR, (c*SQUARESIZE, SQUARESIZE+r*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            if board[r][c] == 1:
                pygame.draw.circle(screen, P1_COLOR, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, P2_COLOR, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, SCREEN_COLOR, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIUS)
    pygame.display.update()


board = create_board()
print_board(board)
game_over = False
turn = 0

# initialize board
pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = SQUARESIZE//2 - 5 

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, SCREEN_COLOR, (0, 0, COLUMN_COUNT*SQUARESIZE, SQUARESIZE))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen, P1_COLOR, (posx, SQUARESIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, P2_COLOR, (posx, SQUARESIZE//2), RADIUS)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            posx = event.pos[0]
            col = posx // SQUARESIZE
            # Ask for player 1 input
            if turn == 1:
                # check location validity and drop piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 1)

                    if winning_move(board, 1):
                        print("Player 1 wins! Congrats!")
                        game_over = True

                turn = 2

            # Ask for player 2 input
            else:

                # check location validity and drop piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    drop_piece(board, row, col, 2)

                    if winning_move(board, 2):
                        print("Player 2 wins! Congrats!")
                        game_over = True

                turn = 1
            print(board)
            draw_board(board)
