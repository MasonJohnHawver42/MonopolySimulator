class Tile:
    def __init__(self, action):
        self.action = action
        self.landedOn = 0

    def updatePlayer(self, player):
        self.action.commitAction(player)
        self.landedOn += 1

    def __str__(self):
        return "Tile: []"
