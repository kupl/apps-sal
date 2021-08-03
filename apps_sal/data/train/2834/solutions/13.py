from typing import List


def symmetric_point(p: List[int], q: List[int]) -> List[int]:
    """ Get the symmetric point of point P about Q. """
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]
