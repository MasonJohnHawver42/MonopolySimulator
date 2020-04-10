from Actions.action import *

class Move(Action):
    def __init__(self, board, amt):
        super().__init__(board)
        self.amt = amt

    def commitAction(self, player):
        player.move(self.amt)
