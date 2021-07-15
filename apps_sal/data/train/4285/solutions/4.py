from typing import List


def find_slope(points: List[int]) -> str:
    try:
        return str((points[3] - points[1]) // (points[2] - points[0]))
    except ZeroDivisionError:
        return "undefined"

