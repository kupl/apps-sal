from collections import deque


def rotate(arr, n):
    """Return a given array, rotated by n spaces."""
    rotator = deque(arr)
    rotator.rotate(n)
    return list(rotator)

