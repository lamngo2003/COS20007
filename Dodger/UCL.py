# Goodie and GoddieMgr classes
import pygame
import random
import pygwidgets
from Constants import *

class UCLs():
    MIN_SIZE = 11
    MAX_SIZE = 41
    MIN_SPEED = 2
    MAX_SPEED = 9
    UCL_IMAGE = pygame.image.load('images/cup.png')
    LEFT = 'left'
    RIGHT = 'right'

    def __init__(self, window):
        self.window = window
        size = random.randrange(UCLs.MIN_SIZE, UCLs.MAX_SIZE + 1)
        self.y = random.randrange(0, GAME_HEIGHT - size)

        self.direction = random.choice([UCLs.LEFT, UCLs.RIGHT])
        if self.direction == UCLs.LEFT:
            self.x = WIN_WIDTH
            self.speed = - random.randrange(UCLs.MIN_SPEED,
                                            UCLs.MAX_SPEED + 1)
            self.minLeft = - size
        else:
            self.x = 0 - size
            self.speed = random.randrange(UCLs.MIN_SPEED,
                                          UCLs.MAX_SPEED + 1)

        self.image = pygwidgets.Image(self.window,
                                      (self.x, self.y), UCLs.UCL_IMAGE)
        percentage = int((size * 100) / UCLs.MAX_SIZE)
        self.image.scale(percentage, False)

    def update(self):
        self.x = self.x + self.speed
        self.image.setLoc((self.x, self.y))
        if self.direction == UCLs.LEFT:
            if self.x < self.minLeft:
                return True
            else:
                return False
        else:
            if self.x > WIN_WIDTH:
                return True
            else:
                return False

    def draw(self):
        self.image.draw()

    def collide(self, playerRect):
        collidedWithPlayer = self.image.overlaps(playerRect)
        return collidedWithPlayer


class UCLMgr():
    UCL_RATE_LOW = 90
    UCL_RATE_HIGH = 111

    def __init__(self, window):
        self.window = window
        self.reset()

    def reset(self):
        self.UCLsList = []
        self.numFramesUntilNextUCL = UCLMgr.UCL_RATE_HIGH

    def update(self, thePlayerRect):

        num_UCL_Hit = 0
        goodiesListCopy = self.UCLsList.copy()
        for UCL in goodiesListCopy:
            deleteMe = UCL.update()
            if deleteMe:
                self.UCLsList.remove(UCL)

            elif UCL.collide(thePlayerRect):
                self.UCLsList.remove(UCL)
                num_UCL_Hit = num_UCL_Hit + 1
        

        self.numFramesUntilNextUCL = self.numFramesUntilNextUCL - 1
        if self.numFramesUntilNextUCL == 0:
            UCL = UCLs(self.window)
            self.UCLsList.append(UCL)
            self.numFramesUntilNextUCL = random.randrange(
                                                            UCLMgr.UCL_RATE_LOW,
                                                            UCLMgr.UCL_RATE_HIGH)

        return num_UCL_Hit

    def draw(self):
        for UCLs in self.UCLsList:
            UCLs.draw()
