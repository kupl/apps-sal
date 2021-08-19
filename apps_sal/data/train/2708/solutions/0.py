from collections import deque


def yes_no(arr):
    (d, result) = (deque(arr), [])
    while d:
        result.append(d.popleft())
        d.rotate(-1)
    return result
