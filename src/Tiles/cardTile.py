from Tiles.tile import *

class CardTile(Tile):
    def __init__(self, board):
        super().__init__(board)

    def updatePlayer(self, player):
        card = self.board.drawCard()
        card.updatePlayer(player)
        
