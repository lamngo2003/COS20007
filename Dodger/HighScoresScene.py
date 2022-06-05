# High Scores scene
import pygwidgets
import pyghelpers
from DataHighScores import *

def showCustomAnswerDialog(theWindow, theText):
    BackgroundDialog = pygwidgets.Image(theWindow, (37, 452),
                                                'images/dialog.png')

    UserText = pygwidgets.InputText(theWindow, (202, 550), '',
                                                fontSize=38, initialFocus=True)
    DisplayText = pygwidgets.DisplayText(theWindow, (0, 482),
                                         theText, width=WIN_WIDTH,
                                         justified='center', fontSize=36)
    YesButton = pygwidgets.CustomButton(theWindow, (332, 595),
                                        'images/addNormal.png',
                                        over='images/addOver.png',
                                        down='images/addDown.png',
                                        disabled='images/addDisabled.png')
    NoButton = pygwidgets.CustomButton(theWindow, (67, 595),
                                                'images/noThanksNormal.png',
                                       over='images/noThanksOver.png',
                                       down='images/noThanksDown.png',
                                       disabled='images/noThanksDisabled.png')

    userAnswer = pyghelpers.customAnswerDialog(theWindow,
                                               BackgroundDialog,
                                               DisplayText, UserText,
                                               YesButton, NoButton)
    return userAnswer

def showCustomResetDialog(theWindow, theText):
    DialogBackground = pygwidgets.Image(theWindow,
                                               (37, 452), 'images/dialog.png')
    PromptDisplayText = pygwidgets.DisplayText(theWindow, (0, 482),
                                                theText, width=WIN_WIDTH,
                                                justified='center', fontSize=36)
    NoButton = pygwidgets.CustomButton(theWindow, (67, 595),
                                                'images/cancelNormal.png',
                                                over='images/cancelOver.png',
                                                down='images/cancelDown.png',
                                                disabled='images/cancelDisabled.png')
    YesButton = pygwidgets.CustomButton(theWindow, (332, 595),
                                                'images/okNormal.png',
                                                over='images/okOver.png',
                                                down='images/okDown.png',
                                                disabled='images/okDisabled.png')
    choiceAsBoolean = pyghelpers.customYesNoDialog(theWindow,
                                                DialogBackground, PromptDisplayText,
                                                YesButton, NoButton)
    return choiceAsBoolean


class HighScoresScene(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window
        self.HighScoresData = HighScoresData()
        
        self.backgroundImage = pygwidgets.Image(self.window,
                                                (0, 0),
                                                'images/highScoresBackground.jpg')

        self.Names_Field = pygwidgets.DisplayText(self.window, (262, 152), '',
                                                  fontSize=50, textColor=BLACK,
                                                  width=302, justified='left')
        self.scoresField = pygwidgets.DisplayText(self.window,
                                                  (27, 152), '', fontSize=48,
                                                  textColor=WHITE,
                                                  width=177, justified='right')

        self.Button_Quit = pygwidgets.CustomButton(self.window,
                                                   (32, 652),
                                                   up='images/quitNormal.png',
                                                   down='images/quitDown.png',
                                                   over='images/quitOver.png',
                                                   disabled='images/quitDisabled.png')

        self.Button_Back = pygwidgets.CustomButton(self.window,
                                                   (242, 652),
                                                   up='images/backNormal.png',
                                                   down='images/backDown.png',
                                                   over='images/backOver.png',
                                                   disabled='images/backDisabled.png')

        self.ScoresButton_Reset = pygwidgets.CustomButton(self.window,
                                                          (452, 652),
                                                          up='images/resetNormal.png',
                                                          down='images/resetDown.png',
                                                          over='images/resetOver.png',
                                                          disabled='images/resetDisabled.png')

        self.showHighScores()

    def getSceneKey(self):
        return SCENE_HIGH_SCORES

    def enter(self, newHighScoreValue=None):
        # 1. If no new high score, newHighScoreValue = 0 and the highscore shows the value of the current game
        # 2. If not, newHighScoreValue is the highest score
        if newHighScoreValue is None:
            return  # nothing to do

        self.draw()
        dialogQuestion = ('To record your score of ' +
                                 str(newHighScoreValue) + ',\n' +
                                 'please enter your name:')
        playerName = showCustomAnswerDialog(self.window, dialogQuestion)
        if playerName is None:
            return  # user pressed Cancel

        # Add user and score to high scores
        if playerName == '':
            playerName = 'Anonymous'
        self.HighScoresData.addHighScore(playerName, newHighScoreValue)

        self.showHighScores()

    def showHighScores(self):
        # Get the names and scores
        scores_list, names_list = self.HighScoresData.getScoresAndNames()
        self.Names_Field.setValue(names_list)
        self.scoresField.setValue(scores_list)

    def handleInputs(self, events_List, keyPressed_List):
        for event in events_List:
            if self.Button_Quit.handleEvent(event):
                self.quit()

            elif self.Button_Back.handleEvent(event):
                self.goToScene(SCENE_PLAY)

            elif self.ScoresButton_Reset.handleEvent(event):
                confirmed = showCustomResetDialog(self.window,
                                        'Are you sure you want to \nRESET the high scores?')
                if confirmed:
                    self.HighScoresData.resetScores()
                    self.showHighScores()

    def draw(self):
        self.backgroundImage.draw()
        self.scoresField.draw()
        self.Names_Field.draw()
        self.Button_Quit.draw()
        self.ScoresButton_Reset.draw()
        self.Button_Back.draw()

    def respond(self, ID_requested):
        if ID_requested == DATA_HIGH_SCORE:
            # Request from Play scene for the highest and lowest scores
            # Build a dictionary and return it to the Play scene
            highestScore, lowestScore = self.HighScoresData.getHighestAndLowest()
            return {'highest':highestScore, 'lowest':lowestScore}
