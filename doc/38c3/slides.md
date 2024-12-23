---
<!-- Doku: https://marpit.marp.app/image-syntax -->
marp: true
header: 38c3 - lightning talk
theme: base-theme
title: Old-School demos mit pyxel
author: Pintman
---

# Old-School demos mit pyxel!

Kontakt: @pintman@chaos.social

---

# Motivation

- Einfache Game-Engine lernen -> pyxel
- Einfach Algorithmen für Old-School Demos

---

# pyxel

- Einfache Game-Engine
- Editoren für   
  - Sprites
  - Tilemaps
  - Sounds
  - Musik
- Python

---

# Sprite und Tilemaps

![drop-shadow](pyxel_sprites_tiles.gif)

---

# Musik

![drop-shadow](pyxel_music.gif)


---

# 16 Farben

![drop-shadow](pyxel_colors.png)

--- 

# Old-School-Demo-Algorithmen

- Plasma
- Swirl
- Moire
- Perlin Noise

---

# Einfaches Programm

```python
import pyxel

class App:
    def __init__(self):
        pyxel.init(64, 64)
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, 0, 8, 8, 9)

App()
```

---

# Plasma Demo

```python
class Plasma:
    def __init__(self):
        self.i = 0
        self.s = 1

    def update(self):
        self.i += 2
        self.s = math.sin(self.i / 100.0) * 2.0 + 6.0

    def draw(self):
        pyxel.cls(0) # clear screen
        
        for y in range(HEIGHT):
            for x in range(WIDTH):
                b = self.handle_px(x, y)
                if b:
                    pyxel.pset(x, y, 6)

    def handle_px(self, x, y):
        v = 0.3 + (0.3 * math.sin((x * self.s) + self.i / 4.0) *
                   math.cos((y * self.s) + self.i / 4.0))
        return v > 0.3
```

---

# Quellen

- Pyxel: 
  - github.com/kitao/pyxel
- Meine Demos: 
  - github.com/tbs1-bo/pyxel-tutorial
