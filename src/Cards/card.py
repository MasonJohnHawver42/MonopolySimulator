class Card:
    def __init__(self, action):
        self.action = action

    def updatePlayer(self, player):
        self.action.commitAction(player);
        print("Card Drawn")
