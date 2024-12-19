# Muss installiert werden:
# pip install pyxel
import pyxel

class Game:
    def __init__(self):
        pyxel.init(8*8, 8*8)
        pyxel.run(self.update, self.draw)

    def update(self):
        "Wird jeden Frame aufgerufen."
        pass

    def draw(self):
        "Zeichne den Bildschirm"

        pyxel.cls(0)


# Das Spiel wird gestartet
Game()
