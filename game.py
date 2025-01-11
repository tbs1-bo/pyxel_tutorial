import pyxel

# Tilemap layout
# EMPTY  PLAYER
# WALL   COIN
EMPTY = 0,0
PLAYER = 1,0
WALL = 0,1
COIN = 1,1


class Player:
    def __init__(self, x, y):
        self.xy = x,y
        self.width = 8
        self.height = 8

    def draw(self):
        px, py = self.xy
        pyxel.blt(px, py, 0, 8, 0, self.width, self.height)
        pyxel.text(0, 0, "x: %d, y: %d" % (self.xy), 1)

    def move(self):
        newx, newy = self.xy

        if pyxel.btn(pyxel.KEY_LEFT):
            newx += - 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            newx += + 1
        if pyxel.btn(pyxel.KEY_UP):
            newy += - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            newy += + 1

        return newx, newy

class Game:
    def __init__(self):
        self.player = Player(9, 8)

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        newx, newy = self.player.move()        
        if (self.player.xy)!=(newx,newy) and self.inside(newx, newy):
            self.player.xy = newx, newy
            pyxel.play(0, 0)

        if self.coin_found():
            pyxel.play(1,1)
            print("coin found")
            px, py = self.player.xy
            # TODO currently not working
            pyxel.tilemaps[0].pset(px//8, py//8, EMPTY)

    def coin_found(self):
        tm = pyxel.tilemaps[0]
        px, py = self.player.xy
        COIN = 1,1
        LEVEL_OFFSET = 8, 0
        tile = tm.pget(px//8 + LEVEL_OFFSET[0], py//8 + LEVEL_OFFSET[1])
        return tile == COIN

    def inside(self, x, y):
        return 8 <= x <= 48 and 8 <= y <= 48

    def draw(self):
        pyxel.cls(0)

        # tilemap
        # bltm(x, y, tm, u, v, w, h, [colkey], [rotate], [scale])
        pyxel.bltm(0, 0, 0, 8*8,0, 8*8,8*8)

        # blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])
        self.player.draw()


Game()
