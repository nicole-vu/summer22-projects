import numpy as np
import pygame
import sys

# board dimensions
COLUMN_COUNT = 13
ROW_COUNT = COLUMN_COUNT - 1

P1_COLOR = (240,60,60)
P2_COLOR = (230,177,52)
BOARD_COLOR = (54,140,180)
SCREEN_COLOR = (84,73,75)

def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT)) # create a zero matrix of 6 rows and 7 columns
    return board

# check if the chosen column still have space for the next move
def is_valid_location(board, col):
    return board[0][col] == 0

# find the bottom most empty slot in a column
def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[ROW_COUNT - r - 1][col] == 0:
            return ROW_COUNT - r - 1

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
    pygame.draw.rect(screen, BOARD_COLOR, (0, SQUARESIZE, WIDTH, WIDTH-SQUARESIZE))
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT):
            if board[r][c] == 1:
                pygame.draw.circle(screen, P1_COLOR, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, P2_COLOR, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, SCREEN_COLOR, (c*SQUARESIZE+SQUARESIZE//2, r*SQUARESIZE+SQUARESIZE+SQUARESIZE//2), RADIUS)
    pygame.display.update()


board = create_board()
game_over = False
turn = 1

# initialize board
pygame.init()

WIDTH = 700
SQUARESIZE = WIDTH // COLUMN_COUNT
RADIUS = SQUARESIZE//2.5

screen = pygame.display.set_mode((WIDTH, WIDTH))
screen.fill(SCREEN_COLOR)
pygame.display.set_caption("Connect 4")
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("Century Gothic", SQUARESIZE//2)

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, SCREEN_COLOR, (0, 0, WIDTH, SQUARESIZE))
            posx = event.pos[0]
            if turn == 1:
                pygame.draw.circle(screen, P1_COLOR, (posx, SQUARESIZE//2), RADIUS)
            else:
                pygame.draw.circle(screen, P2_COLOR, (posx, SQUARESIZE//2), RADIUS)
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(screen, SCREEN_COLOR, (0, 0, WIDTH, SQUARESIZE))
            col = event.pos[0] // SQUARESIZE
            # Ask for player 1 input
            if turn == 1:
                # check location validity and drop piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    board[row][col] = 1

                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!", 1, (255,255,255))
                        screen.blit(label, (WIDTH//2 - SQUARESIZE//0.6,SQUARESIZE//4))
                        game_over = True
                turn = 2

            # Ask for player 2 input
            else:
                # check location validity and drop piece
                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    board[row][col] = 2

                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!", 1, (255,255,255))
                        screen.blit(label, (WIDTH//2 - SQUARESIZE//0.6,SQUARESIZE//4))
                        game_over = True
                turn = 1

            print(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(3000)

