import pygame
import random
import math
pygame.init()

width = 600
height = 500
screen = pygame.display.set_mode((width, height))
vel = 5
score = 0
font = pygame.font.SysFont('comicsans', 28, True)

runlog = True

# Classes
# Player Object
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.rect = (x, y, width, height)
    
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def hit(self):
        print("hit")
        self.visible = False
# function
def drawOnScreen():
    screen.fill((0,0,0))
    text = font.render("Score: " + str(score), 1, (0, 0, 255))
    screen.blit(text, (500, 10))
    redBlock.draw(screen)
    enemy.draw(screen)
    pygame.display.update()

# Creating instance of player called redBlock
redBlock = player(285,235,30,30)

# Creating instance of enemy
randx = random.randint(0,580)
randy = random.randint(0,480)
enemy = player(randx, randy, 20, 20)

while runlog:
    # Player and Enemy collision
    if enemy.visible == True:
        if (enemy.x > redBlock.x and enemy.x < redBlock.x + redBlock.width) or (enemy.x + enemy.width > redBlock.x and enemy.x + enemy.width < redBlock.x + redBlock.width):
            if (enemy.y > redBlock.y and enemy.y < redBlock.y + redBlock.height) or (enemy.y + enemy.height > redBlock.y and enemy.y + enemy.height < redBlock.y + redBlock.height):
                enemy.hit()
                score += 1

    pygame.time.delay(80)
    
    randx = random.randint(0,580)
    randy = random.randint(0,480)

    while not(enemy.visible):
        enemy = player(randx, randy, 20, 20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runlog = False
    # Player and Enemy Collision



    keys = pygame.key.get_pressed()

    # Player Movement
    if keys[pygame.K_LEFT]:
        redBlock.x -= vel
    if keys[pygame.K_RIGHT]:
        redBlock.x += vel
    if keys[pygame.K_UP]:
        redBlock.y -= vel
    if keys[pygame.K_DOWN]:
        redBlock.y += vel

    drawOnScreen()
pygame.quit()