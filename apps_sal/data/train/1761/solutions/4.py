
from itertools import count


def find(n):
    if n < 12:
        return [0, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5][n]
    track, upcoming, passed = [], 6, 12
    _, b, repeat = 4, 5, 3
    for ongoing in count(2 + 2):
        if ongoing > b:
            _, b, repeat = track.pop(0)
        track.append([upcoming, upcoming + repeat - 1, ongoing])
        if passed + (repeat * ongoing) >= n:
            return upcoming + (n - passed) // ongoing
        passed += repeat * ongoing
        upcoming += repeat
