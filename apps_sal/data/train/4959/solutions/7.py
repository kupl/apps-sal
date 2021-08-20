def split(scales, next):
    if len(next) == 1:
        return next[0]
    elif len(next) == 2:
        w = scales.get_weight([next[0]], [next[1]])
        if w == 1:
            return next[1]
        else:
            return next[0]
    elif len(next) == 3:
        w = scales.get_weight([next[0]], [next[1]])
        if w == 0:
            return next[2]
        elif w == -1:
            return next[0]
        else:
            return next[1]
    lock_size = (len(next) + 1) // 3
    l = next[:lock_size]
    r = next[lock_size:lock_size + lock_size]
    f = next[lock_size + lock_size:]
    return find(scales, f, l, r)


def find(scales, free, first, second):
    w = scales.get_weight(first, second)
    if w == 0:
        return split(scales, free)
    elif w == -1:
        return split(scales, first)
    elif w == 1:
        return split(scales, second)


def find_ball(scales, ball_count):
    next = list(range(ball_count))
    return split(scales, next)
