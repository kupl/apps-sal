from itertools import chain, count, takewhile
import re


def available_moves(position):

    if not isinstance(position, str) or not re.match(r'[A-H][1-8]$', position):
        return []

    def converter(g): return (chr(x + 65) + chr(y + 49) for x, y in g)

    def genTargetedPos(dx, dy):
        return converter(takewhile(lambda p: 0 <= p[0] < 8 and 0 <= p[1] < 8,
                                   ((X + n * dx, Y + n * dy) for n in count(1))))

    X, Y = ord(position[0]) - 65, int(position[1]) - 1
    return sorted(chain(*(genTargetedPos(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx or dy)))
