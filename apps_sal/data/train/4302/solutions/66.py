import math


def better_than_average(class_points, your_points):
    # Your code here
    return your_points > (sum(class_points) / len(class_points))
