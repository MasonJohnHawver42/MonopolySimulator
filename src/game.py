from board import *

tiles = []
cards = []

testBoard = Board()
testBoard.addPlayer()
testBoard.addDie(6)

baseAction = Action(testBoard)
lightSpeed = GoTo(testBoard, 0)
gotoJail = Confine(testBoard)

blankTile = Tile(baseAction)
gotoJailTile = Tile(gotoJail)
lightSpeedTile = Tile(lightSpeed)


tiles = [blankTile, blankTile, blankTile, blankTile, lightSpeedTile, blankTile, blankTile, blankTile, blankTile]
tiles += tiles + tiles + tiles

testBoard.tiles = tiles

testBoard.init(1, 10, 2)

testBoard.reprTiles()

while 1:
    print(testBoard)
    testBoard.update()

    if input("continue[y/n]? ") == "n":
        break
