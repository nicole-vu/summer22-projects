import pygame

# VARIABLES
width = 500
clientNumber = 0
bg_color = (255,255,255)


# CREATING WINDOW
win = pygame.display.set_mode((width, width))
pygame.display.set_caption("Client")


# CLASS
class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 3

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


# FUNCTIONS
def redrawWindow(win, player):
    win.fill(bg_color)
    player.draw(win)
    pygame.display.update()


# MAIN
def main():
    run = True
    p = Player(50,50,100,100,(0,255,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)

main()