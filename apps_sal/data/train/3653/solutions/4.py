from itertools import count


def tops(msg):
    deltas = count(7, 4)
    xs = []
    (i, n) = (2, 2)
    while i < len(msg):
        xs.append(msg[i:i + n])
        i += next(deltas)
        n += 1
    return ''.join(reversed(xs))
