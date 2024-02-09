import pygame as pg
import numpy as np


class Screen:
    def __init__(self, scale, points_size):
        """
        :param scale: two tuple, both ints. How many points vertically/horizontally the screen should have
        :param points_size: int. Radius of each of the points
        """
        self.scale = scale
        self.size = points_size
        self.screen_size = (scale[0] * (points_size + 1) + 1, scale[1] * (points_size + 1) + 1)
        self.dis = make_screen(self.screen_size)

    @staticmethod
    def draw_point(loc, cur_screen, color=(7, 132, 148)):
        """
        Drawing a circle on a pygame screen
        :param loc: numpy array of size 2
        :param cur_screen: A screen object
        :param color: Tuple of size 3 composed of ints in [0, 256)
        :return: none
        """
        final_loc = Screen.change_scale(cur_screen, loc)
        pg.draw.circle(cur_screen.dis, color, final_loc, cur_screen.size / 2)
        pg.display.update()

    @staticmethod
    def draw_line(cur_screen, point_one, point_two, color=(7, 132, 148)):
        """
        :param cur_screen: Screen object that the line is to be drawn on
        :param point_one: point (unconverted) where the line is to start
        :param point_two: point (unconverted) where the line is to end
        :param color: 3 tuple that denotes the line's color
        :return: none
        """
        pt_one = Screen.change_scale(cur_screen, point_one)
        pt_two = Screen.change_scale(cur_screen, point_two)
        pg.draw.line(cur_screen.dis, color, pt_one, pt_two)
        pg.display.update()

    @staticmethod
    def change_scale(cur_screen, point):
        """
        :param cur_screen: the screen that the point is to be placed on
        :param point: A point that is in screen points (numpy array)
        :return: numpy array of the points position in pixels
        """
        # final_point = point * cur_screen.scale
        final_point = point * cur_screen.size
        final_point += cur_screen.size / 2
        final_point += 1
        return np.array((point[0] + final_point[0], point[1] + final_point[1]))


def make_screen(screen_size):
    pg.init()
    dis = pg.display.set_mode(screen_size)
    return dis
