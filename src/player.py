
class Player:

    nextId = 0

    def __init__(self, board, pos=0):
        self.board = board
        self.pos = pos

        self.id = Player.nextId
        Player.nextId += 1

        self.places = []

    def updatePos(self):
        self.pos = self.pos % len(self.board.tiles)

        currTile = self.board.tiles[self.pos % len(self.board.tiles)]
        currTile.updatePlayer(self)

        self.places.append(self.pos)

    def move(self, amt):
        self.pos += amt
        self.updatePos()

    def goto(self, pos):
        self.pos = pos
        self.updatePos()

    def rollDice(self):
        amt = 0
        for die in self.board.dice:
            amt += die.roll()

        return amt

    def update(self):
        print("Player" + str(self.id) + "updating")
        amt = self.rollDice()
        self.move(1)

    def __repr__(self):
        return "Player: [pos=" + str(self.pos) + "]"

    def __str__(self):
        return "Player: [id=" + str(self.id) + ", pos=" + str(self.pos) + "]"
