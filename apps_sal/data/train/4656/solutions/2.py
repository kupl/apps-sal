from collections import deque
from itertools import count, islice


def iter_center(s):
    q = deque(s)
    for i in count():
        yield q[i % len(q)]
        q.rotate(-3 - i * 4)


def find_repeat(g):
    xs = []
    for i in count(1):
        xs.extend(islice(g, 10))
        if all(len(set(xs[j::i])) == 1 for j in range(i)):
            return ''.join(xs[:i])


def center_of(chars):
    return chars and find_repeat(iter_center(chars))
