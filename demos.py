import pyxel
import math
import time
import random

WIDTH = 8*8
HEIGHT = 8*8

class SwirlDemo:
    def __init__(self):
        self.timestep = 0
        self.parameter1 = 0
        
    def update(self):
        self.timestep = math.sin(time.time() / 18) * 1500
        self.parameter1 = pyxel.mouse_x / WIDTH

    def draw(self):
        pyxel.cls(0)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                b = self.swirl(x, y, self.timestep) > 0.2
                if b:
                    col = random.randint(5, 6)
                    pyxel.pset(x, y, col)

        #pyxel.text(0, 0, f"p1 {self.parameter1}", 2)

    def swirl(self, x, y, step):
        x -= (WIDTH/2.0)
        y -= (HEIGHT/2.0)

        dist = math.sqrt(pow(x, 2) + pow(y, 2))

        angle = (step / 10.0) + dist / 1.5

        s = math.sin(angle)
        c = math.cos(angle)

        xs = x * c - y * s
        ys = x * s + y * c

        r = abs(xs + ys)

        val =  max(0.0, 0.7 - min(1.0, r/8.0))
        return val

class Plasma:
    def __init__(self):
        self.i = 0
        self.s = 1

    def update(self):
        self.i += 2
        self.s = math.sin(self.i / 100.0) * 2.0 + 6.0

    def draw(self):
        pyxel.cls(0)
        
        for y in range(HEIGHT):
            for x in range(WIDTH):
                b = self.handle_px(x, y)
                if b:
                    pyxel.pset(x, y, 6)

    def handle_px(self, x, y):
        v = 0.3 + (0.3 * math.sin((x * self.s) + self.i / 4.0) *
                   math.cos((y * self.s) + self.i / 4.0))
        return v > 0.3

class RotatingPlasmaDemo:
    def __init__(self):
        self.current = time.time()

    def update(self):
        self.current = time.time()

    def draw(self):
        pyxel.cls(0)

        for y in range(HEIGHT):
            for x in range(WIDTH):
                b = self.handle_px(x, y)
                col = int(b * 3)
                if b:
                    pyxel.pset(x, y, col)

    def handle_px(self, x, y):
        v = math.sin(1*(0.5*x*math.sin(self.current/2) +
                        0.5*y*math.cos(self.current/3)) + self.current)
        # -1 < sin() < +1
        # therfore correct the value and bring into range [0, 1]
        v = (v+1.0) / 2.0
        return v 


class DemoHandler:
    def __init__(self):
        self.timestep = 0
        self.parameter1 = 0        
        self.current_demo = 0
        self.demos = [
            SwirlDemo(), Plasma(), RotatingPlasmaDemo()
        ]
        pyxel.init(WIDTH, HEIGHT)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_RIGHT, hold=10):
            print("next")
            self.current_demo += 1
            if self.current_demo >= len(self.demos):
                self.current_demo = 0

        self.demos[self.current_demo].update()

    def draw(self):
        self.demos[self.current_demo].draw()


DemoHandler()
