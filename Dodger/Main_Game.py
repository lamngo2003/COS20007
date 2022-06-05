#Road to UCL
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

import pygame
import pyghelpers
from SplashScene import *
from PlayScene import *
from HighScoresScene import *
from Inventory import *


FRAMES_PER_SECOND = 40

pygame.init()
window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))


scenesList = [SceneSplash(window),
              HighScoresScene(window),
              ScenePlay(window), Inventory(window)]


SceneMgr = pyghelpers.SceneMgr(scenesList, FRAMES_PER_SECOND)

SceneMgr.run()
