import pyxel

class Game:
    def __init__(self):
        self.x = 8
        self.y = 8

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        newx, newy = self.x, self.y

        if pyxel.btn(pyxel.KEY_LEFT):
            newx = self.x - 1
        if pyxel.btn(pyxel.KEY_RIGHT):
            newx = self.x + 1
        if pyxel.btn(pyxel.KEY_UP):
            newy = self.y - 1
        if pyxel.btn(pyxel.KEY_DOWN):
            newy = self.y + 1

        if (self.x,self.y)!=(newx,newy) and not self.collides(newx, newy):
            self.x, self.y = newx, newy
            pyxel.play(0, 0)

        if self.coin_found():
            pyxel.play(1,1)
            print("coin found")
            pyxel.tilemaps[0].pset(self.x//8, self.y//8, (0,0))

    def coin_found(self):
        tm = pyxel.tilemaps[0]
        return tm.pget(self.x//8, self.y//8) == (1,1)

    def collides(self, x, y):
        tm = pyxel.tilemaps[0]

        return tm.pget(x//8, y//8) == (0,1) or \
            tm.pget((x+7)//8, y//8) == (0,1) or \
            tm.pget(x//8, (y+7)//8) == (0,1)

        #return pyxel.tilemap(0).pget(x//8, y//8) != (0,0)         

    def draw(self):
        pyxel.cls(0)
        # tilemap
        # bltm(x, y, tm, u, v, w, h, [colkey], [rotate], [scale])
        pyxel.bltm(0, 0, 0, 0,0, 8*8,8*8)

        # blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])
        pyxel.blt(self.x,self.y, 0, 8,0, 8, 8)


Game()
