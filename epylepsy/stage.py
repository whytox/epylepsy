import pygame as pg
import numpy as np


class Stage:
    def __init__(self, screen: pg.Surface, length: int):
        self.screen = screen
        self.screen_size = screen.get_size()
        self.focal = self.screen_size[0] // 2, self.screen_size[1] // 2
        self.length = length
        self.margin_w = (self.screen_size[0] - self.length) // 2
        self.margin_h = (self.screen_size[1] - self.length) // 2

    def draw(self):
        # draw the stage cube
        outer_points = self.__outer_points()
        pg.draw.rect(self.screen, (255, 255, 255), (self.margin_w, self.margin_h, self.length, self.length), 1, 0)
        inner_points = []
        for x, y in outer_points:
            dy, dx = (y - self.focal[1]), (x - self.focal[0])
            print(dx, dy)
            theta = np.arctan2(dy, dx)
            x_in = x - self.length * np.cos(theta)
            y_in = y - self.length * np.sin(theta)
            inner_points.append((x_in, y_in))
            pg.draw.circle(self.screen, (255, 255, 255), (x_in, y_in), 5)
            # not working as expected... ask on stackoverflow
            pg.draw.line(self.screen, (255, 255, 255), (x, y), (x_in, y_in))

        for i in range(4):
            outer = outer_points[i]
            inner = inner_points[(i + 1) % 4]



    def __outer_points(self):
        return [(self.margin_w, self.margin_h), (self.margin_w + self.length, self.margin_h),
                (self.margin_w, self.margin_h + self.length),
                (self.margin_w + self.length, self.margin_h + self.length)]
