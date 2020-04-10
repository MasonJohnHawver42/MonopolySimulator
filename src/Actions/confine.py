from Actions.goto import *

class Confine(GoTo):
    def __init__(self, board):
        super().__init__(board, board.jailPos)

    def commitAction(self, player):
        super().commitAction(player)
        self.board.jail.append(player)

        print("Jailed")
