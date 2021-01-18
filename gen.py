from random import randint
import numpy as np


class RoomGenerator:
    def __init__(self, min_w, max_w, min_h, max_h, margin, map_w, map_h, room_max_iters = 1000):
        self.min_w = min_w
        self.max_w = max_w
        self.min_h = min_h
        self.max_h = max_h
        self.margin = margin
        self.map_w = map_w
        self.map_h = map_h
        self.m = np.zeros((self.map_w, self.map_h), np.int)
        self.i = 0
        self.rooms = []
        self.room_max_iters = room_max_iters

    def _generate_room(self):
        w = randint(self.min_w, self.max_w)
        h = randint(self.min_h, self.max_h)
        x = randint(0, self.map_w - w)
        y = randint(0, self.map_h - h)
        return (x, y, w, h)

    def _check_collision(self, room):
        (x, y, w, h) = room
        from_x = max(0, x-self.margin)
        to_x = min(x + w + self.margin, self.map_w - 1)
        from_y = max(0, y - self.margin)
        to_y = min(y + h + self.margin, self.map_h - 1)
        return np.all(self.m[from_x:to_x,from_y:to_y] == 0)

    def _add_room(self, room):
        (x, y, w, h) = room
        self.i += 1
        self.m[x:x+w,y:y+h] = self.i
        self.rooms.append(room)

    def generate_next_room(self):
        for it in range(self.room_max_iters):
            room = self._generate_room()
            if self._check_collision(room):
                self._add_room(room)
                return room
        return None

    def generate_rooms(self, n):
        for i in range(n):
            self.generate_next_room()
            print("%d room generated" % i)
        return self.rooms


