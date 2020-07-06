#https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life

import math
import random
import pygame
from pygame.locals import *

class Conways:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screenWidth = 500
        self.screenHeight = 500
        self.cellWidth = self.screenWidth/self.width
        self.cellHeight = self.screenHeight/self.height
        self.stategrid = list()
        self.displaygrid = list()

        for i in range(0,self.width * self.height):
            num = random.randint(0,100) % 2
            self.stategrid.append(num)
            self.displaygrid.append(num)

    def cell(self,x,y):
        return self.displaygrid[y * self.height + x]

    def update(self,win):
        for i in range(0,self.width * self.height):
            self.displaygrid[i] = self.stategrid[i]

        for i in range(1,self.width-1):
            for j in range(1,self.height-1):
                neighbors = self.findNeighbors(i,j)
                if self.cell(i,j) == 1:
                    if neighbors < 2 or neighbors > 3:
                        self.stategrid[j * self.height + i] = 0
                else:
                    if neighbors == 3:
                        self.stategrid[j * self.height + i] = 1

                if self.cell(i,j) == 1:
                    pygame.draw.rect(win,(255,255,255),pygame.Rect(i * self.cellWidth,j * self.cellHeight, self.cellWidth, self.cellHeight),0)
                else:
                    pygame.draw.rect(win,(0,0,0),pygame.Rect(i * self.cellWidth,j * self.cellHeight, self.cellWidth, self.cellHeight),0)

    def findNeighbors(self,x,y):
        return self.cell(x-1,y-1) + self.cell(x,y-1) + self.cell(x+1,y-1) + self.cell(x-1,y) + 0 + self.cell(x+1,y) + self.cell(x-1,y+1) + self.cell(x,y+1) + self.cell(x+1,y+1)

def main():
    cwol = Conways(100,100)
    pygame.init()
    screen = pygame.display.set_mode((cwol.screenWidth, cwol.screenHeight))
    pygame.display.set_caption("Conway's Game of Life")
    running = True
    while running:
        pygame.time.delay(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        cwol.update(screen)
        pygame.display.update()
    pygame.quit()
if __name__ == '__main__':
    main()
