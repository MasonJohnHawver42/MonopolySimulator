from player import *
from Actions.actions import *
from Tiles.tiles import *
from Cards.cards import *
from die import *

class Board:
    def init(self, numPlayers, numTiles=10, numDice=1):
        self.players = []
        self.tiles = []
        self.cards = []
        self.dice = []

        for i in range(numPlayers):
            newPlayer = Player(self)
            self.players.append(newPlayer)

        for i in range(numTiles):
            newAction = Action(self)
            newTile = Tile(newAction)
            self.tiles.append(newTile)

        for i in range(numDice):
            newDie = Die(6)
            self.dice.append(newDie)

        self.jail = []

        self.jailPos = 0

        self.turn = 0

    def __init__(self):
        self.players = []
        self.tiles = []
        self.cards = []
        self.dice = []

        self.jail = []

        self.jailPos = 0

        self.turn = 0

    #getters

    def getNumTiles(self):
        return len(self.tiles)

    def getCurrPlayer(self):
        return self.players[self.turn]

    def drawCard(self):
        card = self.cards[0]
        self.cards.remove(card)
        self.cards.append(card)

        return card

    #setters

    def setTiles(self, tiles):
        self.tiles = tiles

    def setCards(self, cards):
        self.cards = cards
        self.suffleCards()

    def setDice(self, dice):
        self.dice = dice

    #moders

    def addPlayer(self):
        newPlayer = Player(self)
        self.players.append(newPlayer)

    def addDie(self, sides):
        newDie = Die(sides)
        self.dice.append(newDie)

    def suffleCards(self):
        pass #implement latter

    #updaters

    def updateTurn(self):
        self.turn += 1
        self.turn = self.turn % len(self.players)

    def update(self):
        if len(self.players) > 0:
            currPlayer = self.players[self.turn]
            if currPlayer not in self.jail:
                currPlayer.update()
                print(currPlayer)
            else:
                self.jail.remove(currPlayer)

        self.updateTurn()

    #dunder methods

    def reprTiles(self):
        string = "Tiles: ["

        for tile in self.tiles:
            string += str(tile) + ", "

        string += "]"
        print(string)

    def __repr__(self):
        string = "Players: ["

        for player in self.players:
            string += str(player) + ", "

        string += "]"

        return string
