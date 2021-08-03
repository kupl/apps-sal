import numpy as np


def better_than_average(class_points, your_points):
    return np.mean(class_points + [your_points]) < your_points
