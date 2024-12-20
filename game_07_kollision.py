import pyxel

class Game:
    def __init__(self):
        # Sprite innerhalb der Levelgrenzen platzieren
        self.x = 8
        self.y = 8

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")

        # Hintergrundmusik starten - muss vor run passieren
        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)


    def update(self):
        "Wird jeden Frame aufgerufen."
        # Neue Position ermittteln aber Spieler noch nicht bewegen
        newx, newy = self.x, self.y

        if pyxel.btn(pyxel.KEY_RIGHT):
            newx = self.x + 1
            # Spiele Sound bei Bewegung
            pyxel.play(0, 0) # Kanal 0, Sound 0        

        # Prüfen, ob eine Kollision mit einem Tilemap-Tile stattfindet
        # Das Wand-Tile hat in der Tilemap die Kooridnaten (0, 1)
        WAND_TILE = (0, 1)
        # Prüfe, ob alle vier Ecken des Sprites NICHT auf einem WAND_TILE liegen
        if self.tile_under(newx, newy) != WAND_TILE and \
           self.tile_under(newx+7, newy) != WAND_TILE and \
           self.tile_under(newx, newy+7) != WAND_TILE and \
           self.tile_under(newx+7, newy+7) != WAND_TILE:
            
            # Soll kein Wand-Tile unter dem Spieler sein, dann bewege den Spieler
            self.x, self.y = newx, newy

    def tile_under(self, x, y):
        "Ermittelt das Tile unter der Position (x,y)"

        # Die passende Tilemap ermitteln
        tilemap = pyxel.tilemaps[0]

        # Die Bildschirmkoordinaten in Tilemap-Koordinaten umrechnen
        tilemapx, tilemapy = int(x/8), int(y/8)

        # Das Tile an der Position ermitteln und zurückgeben
        tile = tilemap.pget(tilemapx, tilemapy)
        return tile

    def draw(self):
        "Zeichne den Bildschirm"

        # Bildschirm leeren
        pyxel.cls(0)

        # Level als Tilemap zeichnen
        pyxel.bltm(
            0,0,  # x,y (Koordinaten auf dem Bildschirm)
            0,    # Tilemap Nummer
            0,0,  # u,v (Koordinaten im Tilemap)
            8*8,8*8   # Breite, Höhe
        )

        # Sprite an der aktuellen Position zeichnen
        pyxel.blt(
            self.x,self.y,  # x,y (Koordinaten auf dem Bildschirm)
            0,    # Image Nummer
            8,0,  # v,w (Koordinaten im Bild)
            8,8   # Breite, Höhe
        )


Game()
