import pyxel

class Game:
    def __init__(self):
        # Sprite innerhalb der Levelgrenzen platzieren
        self.x = 8
        self.y = 8

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        "Wird jeden Frame aufgerufen."

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1

    def draw(self):
        "Zeichne den Bildschirm"

        # Bildschirm leeren
        pyxel.cls(0)

        # Level als Tilemap zeichnen
        # Tilemaps können mit pyxel edit erstellt werden
        # Das Menü befindet sich an zweiter Stelle
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
