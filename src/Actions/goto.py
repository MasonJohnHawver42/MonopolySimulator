from Actions.action import *

class GoTo(Action):
    def __init__(self, board, gotoPos):
        super().__init__(board)
        self.gotoPos = gotoPos

    def commitAction(self, player):
        player.goto(self.gotoPos)
