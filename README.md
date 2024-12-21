# Pyxel Tutorial

Ein paar Versuche mit der [Pyxel](https://github.com/kitao/pyxel)-Game-Engine.

## Basic Setup

In der Datei [game_01_basic_setup.py](game_01_basic_setup.py) wird der allgemeine Aufbau eines
Pyxel-Spiels dargestellt.

## Sprite zeichnen und bewegen

Ein Sprite ist Game-Objekt, das sich über die Spielwelt bewegen kann. Das kann z.B. ein Spieler oder eine Münze sein, die eingesammelt werden muss.

[game_02_sprite_zeichnen.py](game_02_sprite_zeichnen.py) zeigt, wie man einen Sprite zeichnet.

In [game_03_sprite_bewegen.py](game_03_sprite_bewegen.py) wird der Sprite bewegt.

## Level zeichnen

Sprites können auch als Kacheln verwendet werden, um eine Spielwelt zu erstellen.

In [game_04_level_zeichnen.py](game_04_level_zeichnen.py) wird ein einfaches Level erstellt.

## Sound und Musik

Die Akustik ist ein wichtiger Bestandteil eines Spiels. 

In [game_05_sound.py](game_05_sound.py) wird gezeigt, wie man einen Bewegungssound abspielt.

In [game_06_musik.py](game_06_musik.py) wir die Verwendung von Musik demonstriert.

## Kollisionserkennung

Wenn verschiedene Sprites aufeinandertreffen, kann es zu Kollisionen kommen. So kann etwa eine Münze eingesammelt werden, wenn der Spieler sie berührt.

In [game_06_kollision.py](game_06_kollision.py) wird eine einfache Kollisionserkennung implementiert.


## TODO

Die Physik-Engine [PyMonk](http://www.pymunk.org)
ermöglicht die Simulation von physikalischen Kräften.
