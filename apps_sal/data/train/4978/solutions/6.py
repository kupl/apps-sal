from collections import deque
from itertools import chain, count


def _code(n, s, sign):
    (non_space, offset) = ([], count())
    slice_points = [0] + [i - (0 if c != ' ' else next(offset)) for (i, c) in enumerate(s) if c == ' ' or non_space.append(c)] + [len(s)]
    slices = [slice(start, end) for (start, end) in zip(slice_points, slice_points[1:])]
    ops = ([slice(None)] * (sign == 1) + slices + [slice(None)] * (sign == -1)) * n
    for op in ops:
        d = deque(non_space[op])
        d.rotate(sign * n)
        non_space[op] = d
    return ' '.join((''.join(non_space[x]) for x in slices))


def encode(n, s):
    ciphered = _code(n, s, 1)
    return f'{n} {ciphered}'


def decode(s):
    (n, s) = s.split(' ', 1)
    return _code(int(n), s, -1)
