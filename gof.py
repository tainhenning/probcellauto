import pygame
from pygame.locals import *
import numpy
import random
#colors#
RED = (255, 0, 0, 1)
BLUE = (0, 0, 255, 1)
GREEN = (0, 255, 0, 1)
WHITE = (255, 255, 255, 1)
GREY = (50, 50, 50, 1)
gridWidth = 50
gridHeight = 50
blockWidth = 10
blockHeight = 10
margin = 1;
screenSize = 551,551
screen = pygame.display.set_mode(screenSize)
clock = pygame.time.Clock()

mainMatrix = [[0 for i in range(gridWidth)] for i in range(gridHeight)]
mainMatrix[random.randint(1,49)][random.randint(1,48)] = 2
mainMatrix[random.randint(1,49)][random.randint(1,48)] = 3
mainMatrix[random.randint(1,49)][random.randint(1,48)] = 4

for x in range(gridWidth):
    mainMatrix[x][0] = 1
    mainMatrix[x][gridHeight-1] = 1
for y in range(gridHeight):
    mainMatrix[0][y] = 1
    mainMatrix[gridWidth - 1][y] = 1
class movement():
    def __init__(self, number):
        self.move(number)
    def move(self, number):
        breaking = False
        for x in range(gridWidth - 1):
            for y in range(gridHeight):
                if mainMatrix[x][y] == number:

                    decider = random.randint(1,4)
                    spawnNew = random.randint(1, 50)
                    if(spawnNew != number): spawnNew = 0

                    conquerChance = random.randint(1, 50)
                    mutateChance = random.randint(1,1000)
                    deathChance = random.randint(1, 100)

                    if(mutateChance == 1):
                        mainMatrix[x][y] = random.randint(2,4)
                    if(deathChance == 1):
                        mainMatrix[x][y] == 1
                        break
                    elif(decider == 1 and x < gridWidth - 2):
                        if(mainMatrix[x + 1][y] == 0):
                            mainMatrix[x][y] = spawnNew
                            mainMatrix[x+1][y] = number
                        else:
                            if conquerChance == 1 and mainMatrix[x+1][y] != number:
                                mainMatrix[x][y] = spawnNew
                                mainMatrix[x + 1][y] = number
                    elif(decider == 2 and x > 1):
                        if(mainMatrix[x-1][y] == 0):
                            mainMatrix[x][y] = spawnNew
                            mainMatrix[x-1][y] = number
                        else:
                            if conquerChance == 1 and mainMatrix[x-1][y] != number:
                                mainMatrix[x][y] = spawnNew
                                mainMatrix[x - 1][y] = number

                    elif(decider == 3 and y > 1):
                        if(mainMatrix[x][y-1] == 0):
                            mainMatrix[x][y] = spawnNew
                            mainMatrix[x][y-1] = number
                        else:
                            if conquerChance == 1 and mainMatrix[x][y-1] != number:
                                mainMatrix[x][y] = spawnNew
                                mainMatrix[x][y - 1] = number

                    elif(decider == 4 and y < gridHeight - 2):
                        if(mainMatrix[x][y+1] == 0):
                            mainMatrix[x][y] = spawnNew
                            mainMatrix[x][y+1] = number
                        else:
                            if conquerChance == 1 and mainMatrix[x][y+1] != number:
                                mainMatrix[x][y] = spawnNew
                                mainMatrix[x][y+1] = number

class grid():
    def __init__(self):
        self.drawMap()

    def drawMap(self):
        for x in range(gridWidth):
            for y in range(gridHeight):
                color = WHITE
                if mainMatrix[x][y] == 2:
                    color = RED
                elif mainMatrix[x][y] == 1:
                    color = GREY
                elif mainMatrix[x][y] == 3:
                    color = BLUE
                elif mainMatrix[x][y] == 4:
                    color = GREEN
                pygame.draw.rect(screen, color,[(blockWidth + margin) * x + margin, (blockHeight + margin) * y + margin, blockWidth, blockHeight])


if __name__ == '__main__':
    done = False
    while not done:
        grid()
        movement(2)
        movement(3)
        movement(4)
        pygame.display.flip()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                done = True
    pygame.quit()