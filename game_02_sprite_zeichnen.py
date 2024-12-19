import pyxel

class Game:
    def __init__(self):
        pyxel.init(8*8, 8*8)
        # Lade alle Ressourcen
        # mit "pyxel edit my_resource.pyxres" wird der Editor gestartet
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        "Wird jeden Frame aufgerufen."
        pass

    def draw(self):
        "Zeichne den Bildschirm"

        # Bildschirm leeren
        pyxel.cls(0)
        # Sprite zeichnen
        pyxel.blt(
            0,0,  # x,y (Koordinaten auf dem Bildschirm)
            0,    # Image Nummer
            8,0,  # v,w (Koordinaten im Bild)
            8,8   # Breite, Höhe
        )


Game()
