from random import randint
import numpy as np

class RoomGenerator:
    def __init__(self, min_w, max_w, min_h, max_h, map_w, map_h):
        self.min_w = min_w
        self.max_w = max_w
        self.min_h = min_h
        self.max_h = max_h
        self.map_w = map_w
        self.map_h = map_h

    def generate_room(self):
        w = randint(self.min_w, self.max_w)
        h = randint(self.min_h, self.max_h)
        x = randint(0, self.map_w - w)
        y = randint(0, self.map_h - h)
        return (x, y, w, h)

    def generate_rooms(self):
        np.full(map)