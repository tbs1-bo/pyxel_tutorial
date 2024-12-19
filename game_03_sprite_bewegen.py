import pyxel

class Game:
    def __init__(self):
        # Koordinaten des Sprites
        # Muss vor dem Aufruf von pyxel.init() gesetzt werden
        self.x = 0
        self.y = 0

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        "Wird jeden Frame aufgerufen."

        # Spriteposition aktualisieren, wenn Taste gedrückt wurde
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
        # analog für die anderen Richtungen.

    def draw(self):
        "Zeichne den Bildschirm"

        # Bildschirm leeren
        pyxel.cls(0)
        # Sprite zeichnen
        pyxel.blt(
            self.x,self.y,  # x,y (Koordinaten auf dem Bildschirm)
            0,    # Image Nummer
            8,0,  # v,w (Koordinaten im Bild)
            8,8   # Breite, Höhe
        )


Game()
