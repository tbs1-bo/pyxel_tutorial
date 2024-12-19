import pyxel

class Game:
    def __init__(self):
        self.x = 0
        self.y = 0

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        "Wird jeden Frame aufgerufen."

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1

            # Spiele Sound bei Bewegung
            # Sound muss im Pyxel-Editor erstellt werden
            # Der Sound-Editor ist im Menü an der dritten Stelle
            pyxel.play(0, 0) # Kanal 0, Sound 0

    def draw(self):
        "Zeichne den Bildschirm"

        pyxel.cls(0)
        pyxel.blt(
            self.x,self.y,  # x,y (Koordinaten auf dem Bildschirm)
            0,    # Image Nummer
            8,0,  # v,w (Koordinaten im Bild)
            8,8   # Breite, Höhe
        )


Game()
