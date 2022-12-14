# Adapted from TechWithTim
import pygame
import math
import random
import tkinter as tk
from tkinter import messagebox

class cube(object):
    global s
    rows = 20
    w = 500
    def __init__(self, start, dirnx=1, dirny=0, color=(120,210,130), shape="rect"):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
        self.shape = shape

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw(self, surface):
        dis = self.w // self.rows
        i = self.pos[0]
        j = self.pos[1]

        if self.shape == "cir":
            pygame.draw.circle(surface, self.color, (i*dis+dis//2, j*dis+dis//2), dis//2)

        elif self.shape == "head": 

            pygame.draw.circle(surface, self.color, (i*dis+dis//2, j*dis+dis//2), dis//2)
            # draw the head based on direction the snake is heading
            if self.dirnx == 1 and self.dirny == 0:
                pygame.draw.rect(surface, (192,37,51), (i*dis+dis-2, j*dis+dis//2+3, 6, 2)) # tongue
                if len(s.body) != 1:
                    pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis//2, dis-2))
            elif self.dirnx == -1 and self.dirny == 0:
                pygame.draw.rect(surface, (192,37,51), (i*dis-4, j*dis+dis//2+3, 6, 2))
                if len(s.body) != 1:    
                    pygame.draw.rect(surface, self.color, (i*dis+dis//2, j*dis+1, dis//2, dis-2))
            elif self.dirnx == 0 and self.dirny == 1:
                pygame.draw.rect(surface, (192,37,51), (i*dis+dis//2-1, j*dis+dis-2, 2, 6))
                if len(s.body) != 1:
                    pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis//2))
            elif self.dirnx == 0 and self.dirny == -1:
                pygame.draw.rect(surface, (192,37,51), (i*dis+dis//2-1, j*dis-4, 2, 6)) 
                if len(s.body) != 1: 
                    pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+dis//2, dis-2, dis//2))
            
            # draw 2 eyes
            pygame.draw.circle(surface, (85,73,75), (i*dis+dis//2-5, j*dis+10), 3)
            pygame.draw.circle(surface, (85,73,75), (i*dis+dis//2+5, j*dis+10), 3)

        elif self.shape == "tail":
            # change the direction of the tail according to the previous block
            prevx = s.body[len(s.body)-2].dirnx
            prevy = s.body[len(s.body)-2].dirny
            if prevx == -1 and prevy == 0:
                pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis//2, dis-2))
                pygame.draw.circle(surface, self.color, (i*dis+dis//2, j*dis+dis//2), dis//2)
            elif prevx == 1 and prevy == 0:
                pygame.draw.rect(surface, self.color, (i*dis+dis//2, j*dis+1, dis//2, dis-2))
                pygame.draw.circle(surface, self.color, (i*dis+dis//2, j*dis+dis//2), dis//2)
            elif prevx == 0 and prevy == -1:
                pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis//2))
                pygame.draw.circle(surface, self.color, (i*dis+dis//2, j*dis+dis//2), dis//2)
            elif prevx == 0 and prevy == 1:
                pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+dis//2, dis-2, dis//2))
                pygame.draw.circle(surface, self.color, (i*dis+dis//2, j*dis+dis//2), dis//2) 

        else:
            pygame.draw.rect(surface, self.color, (i*dis+1, j*dis+1, dis-2, dis-2)) # draw inside of the lines
            

class snake(object):
    body = [] # an list of cubes
    turns = {} # a dictionary of where the snake turned
    def __init__(self, color, pos):
        self.color = color
        self.head = cube(pos) # create a new cube at the head position 
        self.body.append(self.head) # add the new cube at head into the list
        self.dirnx = 0 
        self.dirny = 1

    def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()

            # the origin is at the upper left of the window
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0 
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny] 

                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0 
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1 
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1 
                    self.turns[self.head.pos[:]] = [self.dirnx, self.dirny]

        for i, c in enumerate(self.body):
            p = c.pos[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0], turn[1])
                if i == len(self.body)-1:
                     self.turns.pop(p)
            else:
                # if we reach the end of the screen
                if c.dirnx == -1 and c.pos[0] <= 0: c.pos = (c.rows-1, c.pos[1])
                elif c.dirnx == 1 and c.pos[0] >= c.rows-1: c.pos = (0, c.pos[1])
                elif c.dirny == -1 and c.pos[1] <= 0: c.pos = (c.pos[0], c.rows-1)
                elif c.dirny == 1 and c.pos[1] >= c.rows-1: c.pos = (c.pos[0], 0)
                # if not the end of the screen
                else: c.move(c.dirnx,c.dirny)

    def reset(self, pos):
        self.head = cube(pos)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1

    def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny

        # check the direction of the tail to add the new cube correctly
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.pos[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.pos[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.pos[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.pos[1]+1)))

        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy

    def draw(self, surface):
        for i, c in enumerate(self.body):
            if i == 0:
                c.shape = "head"
            elif i == len(self.body)-1:
                c.shape = "tail"
            else:
                c.shape = "rect"
            c.draw(surface)

def drawGrid (w, rows, surface):
    sizeBtwn = w // rows # how big each square in the row is

    x = 0
    y = 0 
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w)) # draw vertical lines
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y)) # draw horizontal lines

def redrawWindow(surface):
    global rows, width, s, snack
    surface.fill((85,73,75)) # set the bg color to black
    s.draw(surface)
    snack.draw(surface)
    drawGrid(width, rows, surface)
    pygame.display.update()

def randomSnack(rows, item):
    positions = item.body

    while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0: # avoid the snack appear on top of the snake
            continue
        else:
            break
    return (x,y) 

def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

# main function
def main():
    global width, rows, s,snack
    width = 500
    rows = 20
    window = pygame.display.set_mode((width, width)) # create game window
    s = snake((120,210,130), (10,10)) # snake object
    snack = cube(randomSnack(rows, s), color = (192,37,51), shape = "cir") 
    flag = True

    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50) # 50 ms every move so the snake won't move too fast
        clock.tick(10) # the snake will move 10 pixels at a time
        s.move()
        if s.body[0].pos == snack.pos:
            s.addCube()
            snack = cube(randomSnack(rows, s), color = (192,37,51), shape = "cir") 

        for x in range(len(s.body)):
            if s.body[x].pos in list(map(lambda z:z.pos, s.body[x+1:])): 
                print("Score: ", len(s.body))
                message_box("You lost", "Play again")
                s.reset((10,10))
                break

        redrawWindow(window)

main()