from bearlibterminal import terminal
from gen import RoomGenerator
import cProfile
import numpy as np

TITLE = "Rusla in Zuzino Adventure!"
W = 100
H = 80
ROOMS = 1488

def start_game():
    terminal.open()
    terminal.set("window: size=%dx%d, cellsize=8x8, title='%s'" % (W, H, TITLE))

    for x in range(W):
        for y in range(H):
            put(x, y, '.')

    c = '#'

    for (rx, ry, rw, rh) in generate_rooms():
        for x in range(rx, rx + rw):
            put(x, ry, c)
            put(x, ry + rh - 1, c)
        for y in range(ry, ry + rh):
            put(rx, y, c)
            put(rx + rw - 1, y, c)
    terminal.refresh()
    while terminal.read() != terminal.TK_CLOSE:
        terminal.refresh()

    terminal.close()

def put(x, y, c):
    terminal.put(x, y, c)

def generate_rooms():
    rg = RoomGenerator(8, 25, 8, 25, 3, W, H)
    return rg.generate_rooms(ROOMS)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #cProfile.run('generate_rooms()')
    start_game()

