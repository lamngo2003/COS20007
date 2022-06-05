import pygame
import pygwidgets
from Constants import *

class Player():
    def __init__(self, window):
        self.window = window
        self.imagelink = 'images/madrid.png'
        self.image = pygwidgets.Image(window,
                                (-100, -100), self.imagelink)
        playerRect = self.image.getRect()
        self.maxX = WIN_WIDTH - playerRect.width
        self.maxY = GAME_HEIGHT - playerRect.height


    def update(self, x, y):
        if x < 0:
            x = 0
        elif x > self.maxX:
            x = self.maxX
        if y < 0:
            y = 0
        elif y > self.maxY:
            y = self.maxY

        self.image.setLoc((x, y))
        return self.image.getRect()

    def draw(self):
        self.image.draw()