import numpy as np


def create_random_point(max_x, max_y):
    """
    :param max_x: The maximum x value that the point is allowed to occupy (exclusive).
    :param max_y: The maximum y value that the point is allowed to occupy (exclusive).
    :return: Numpy array of size two. [x,y]
    """
    return np.array([np.random.randint(0, max_x), np.random.randint(0, max_y)])


def create_points(num_points, max_x, max_y):
    """
    Purpose: Create num_points number of points in [0, max_x), [0, max_y)
    :param num_points: The number of points to create (int)
    :param max_x: The max x value the point can take (exclusive) (int)
    :param max_y: The max y value the point can take (exclusive) (int)
    :return points: A numpy array of size [num_points, 2]
    """
    points = np.zeros((num_points, 2))
    for i in range(num_points):
        points[i] = create_random_point(max_x, max_y)
    return points


def calc_distance(point_one, point_two):
    """
    Purpose: Calculate the distance between 2 points in R^2
    :param point_one: A numpy array of shape [2]
    :param point_two: A numpy array of shape [2]
    :return: A float
    """
    return np.sqrt((point_one[0] - point_two[0]) ** 2 + (point_one[1] + point_two[1]) ** 2)


def random_lines(ar_size):
    nums = np.random.randint(0, 1000000, ar_size)
    return np.argsort(nums)

