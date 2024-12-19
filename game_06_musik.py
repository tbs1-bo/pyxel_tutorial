import pyxel

class Game:
    def __init__(self):
        # Sprite innerhalb der Levelgrenzen platzieren
        self.x = 8
        self.y = 8

        pyxel.init(8*8, 8*8)
        pyxel.load("my_resource.pyxres")

        # Hintergrundmusik starten - muss vor run passieren
        # Über den Musikeditor können sound zusammengestellt werden.
        # Channel 0 wird hier für Soundeffekte genutzt. Die anderen Kanälen
        # nutzen eine Melodie, Bassline und Schlagzeug.
        # Über loop=True wird die Musik in einer Endlosschleife abgespielt.
        pyxel.playm(0, loop=True)

        pyxel.run(self.update, self.draw)


    def update(self):
        "Wird jeden Frame aufgerufen."

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 1
            # Spiele Sound bei Bewegung
            pyxel.play(0, 0) # Kanal 0, Sound 0

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
