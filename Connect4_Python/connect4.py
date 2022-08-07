import numpy as np
import pygame
import sys

# Number of columns and rows
COLUMN_COUNT = 8
ROW_COUNT = COLUMN_COUNT - 1

STREAK = 5

# Colors
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

# Check if either player has winning streak
def winning_move(board, turn, row, col):
    
    # check horizontal locations for win
    streak_count = 1
    right_count = 1
    left_count = 1
    # right of the newest piece
    while (col + right_count < COLUMN_COUNT) and (board[row][col+right_count] == turn) and (right_count < STREAK):
        right_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True
    # left of the newest piece
    while (col - left_count >= 0) and (board[row][col-left_count] == turn) and (left_count < STREAK) :
        left_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True

    # check vertical locations for win
    streak_count = 1
    up_count = 1
    down_count = 1
    # above of the newest piece
    while (row - up_count >= 0) and (board[row-up_count][col] == turn) and (up_count < STREAK):
        up_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True
    # below of the newest piece
    while (row + down_count < ROW_COUNT) and (board[row+down_count][col] == turn) and (down_count < STREAK):
        down_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True

    # check positive diagonal locations for win
    streak_count = 1
    up_right_count = 1
    down_left_count = 1
    # up right direction
    while (row - up_right_count >= 0) and (col + up_right_count < COLUMN_COUNT) and (board[row-up_right_count][col+up_right_count] == turn) and (up_right_count < STREAK):
        up_right_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True
    # down left direction
    while (row + down_left_count < ROW_COUNT) and (col - down_left_count >= 0) and (board[row+down_left_count][col-down_left_count] == turn)  and (down_left_count < STREAK):
        down_left_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True
    
    # check negative diagonal locations for win
    streak_count = 1
    up_left_count = 1
    down_right_count = 1
    # up left direction
    while (row - up_left_count >= 0) and (col - up_left_count >= 0) and (board[row-up_left_count][col-up_left_count] == turn) and (up_left_count < STREAK):
        up_left_count += 1
        streak_count += 1
        if streak_count >= STREAK:
            return True
    # down right direction
    while (row + down_right_count < ROW_COUNT) and (col + down_right_count < COLUMN_COUNT) and (board[row+down_right_count][col+down_right_count] == turn) and (down_right_count < STREAK):
        down_right_count += 1
        streak_count += 1
        if streak_count >= STREAK:
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

                    if winning_move(board, 1, row, col):
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

                    if winning_move(board, 2, row, col):
                        label = myfont.render("Player 2 wins!", 1, (255,255,255))
                        screen.blit(label, (WIDTH//2 - SQUARESIZE//0.6,SQUARESIZE//4))
                        game_over = True
                turn = 1

            print(board)
            draw_board(board)

            if game_over:
                pygame.time.wait(3000)

