import pygame
import pygwidgets
import pyghelpers
import random
from Team import Player
import Constants
from Constants import *

class Inventory(pyghelpers.Scene):

    def __init__(self, window):
        self.window = window
        self.player = Player(window)
        self.player0 = pygwidgets.CustomButton(self.window, (30, 250), 'images/madrid_inv.png')
        self.player1 = pygwidgets.CustomButton(self.window, (280, 250), 'images/barca_inv.png')
        self.player2 = pygwidgets.CustomButton(self.window, (30, 450), 'images/bayern_inv.png')
        self.inventory = []
        self.image = pygwidgets.Image(self.window,(0, 0),'images/inventory.png')

        self.quitButton = pygwidgets.CustomButton(self.window,
                                                  (30, 650),
                                                  up='images/quitNormal.png',
                                                  down='images/quitDown.png',
                                                  over='images/quitOver.png',
                                                  disabled='images/quitDisabled.png')

        self.backButton = pygwidgets.CustomButton(self.window,
                                                  (240, 650),
                                                  up='images/backNormal.png',
                                                  down='images/backDown.png',
                                                  over='images/backOver.png',
                                                  disabled='images/backDisabled.png')

    def getSceneKey(self):
        return SCENE_INVENTORY

    def enter(self, data):
        pass

    def handleInputs(self, eventsList, keyPressedList):
        for event in eventsList:
            if self.quitButton.handleEvent(event):
                self.quit()

            elif self.backButton.handleEvent(event):
                self.goToScene(Constants.SCENE_PLAY)

            if self.player0.handleEvent(event):
                self.player.imagelink = 'images/madrid.png'
                self.goToScene(Constants.SCENE_PLAY)

            elif self.player1.handleEvent(event):
                self.player.imagelink = 'images/barca.jpg'
                self.goToScene(Constants.SCENE_PLAY)

            elif self.player2.handleEvent(event):
                self.player.imagelink = 'images/bayern.png'
                self.goToScene(Constants.SCENE_PLAY)

    def update(self):
        pass

    def draw(self):
        self.image.draw()
        self.quitButton.draw()
        self.backButton.draw()
        self.player0.draw()
        self.player1.draw()
        self.player2.draw()