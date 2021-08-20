from typing import List


def find_slope(points: List[int]) -> str:
    """ Get a string representation of the slope of the line joining these two points. """
    (x1, y1, x2, y2) = points
    try:
        return str(int((y2 - y1) / (x2 - x1)))
    except ZeroDivisionError:
        return 'undefined'
