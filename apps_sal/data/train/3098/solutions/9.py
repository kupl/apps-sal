from itertools import count


def compute_depth(n):
    (v, target) = (0, set('0123456789'))
    for x in count(1):
        v += n
        target -= set(str(v))
        if not target:
            return x
