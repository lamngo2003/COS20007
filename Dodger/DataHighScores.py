# HighScoresData class
from Constants import *
from pathlib import Path
import json

class HighScoresData():

    def __init__(self):
        self.BLANK_SCORES_LIST = NUM_HIGH_SCORE * [['-----', 0]]
        self.FilePath = Path('HighScores.json')


        try:
            data = self.FilePath.read_text()
        except FileNotFoundError:
            self.resetScores()
            return

        self.scores_List = json.loads(data)

    def addHighScore(self, name, new_HighScore):
        place_found = False
        for index, nameScoreList in enumerate(self.scores_List):
            thisScore = nameScoreList[1]
            if new_HighScore > thisScore:
                self.scores_List.insert(index, [name, new_HighScore])
                self.scores_List.pop(NUM_HIGH_SCORE)
                place_found = True
                break
        if not place_found:
            return

        self.saveScores()

    def saveScores(self):
        scoresAsJson = json.dumps(self.scores_List)
        self.FilePath.write_text(scoresAsJson)

    def resetScores(self):
        self.scores_List = self.BLANK_SCORES_LIST.copy()
        self.saveScores()

    def getScoresAndNames(self):
        names_list = []
        scores_list = []
        for nameAndScore in self.scores_List:
            this_name = nameAndScore[0]
            this_score = nameAndScore[1]
            names_list.append(this_name)
            scores_list.append(this_score)

        return scores_list, names_list

    def getHighestAndLowest(self):
        highest_entry = self.scores_List[0]
        lowest_entry = self.scores_List[-1]

        highest_score = highest_entry[1]
        lowest_score = lowest_entry[1]
        return highest_score, lowest_score

