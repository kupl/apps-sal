move = ['left', 'up', 'right', 'down']


def robot_walk(a):
    if len(a) <= 3:
        return False
    left, upper, right, lower = 0, a[0], a[1], a[0] - a[2]
    for i, x in enumerate(a[3:]):
        m = move[i % 4]
        if m == 'left':
            if right - x <= left:
                return True
            left = right - x
        elif m == 'up':
            if lower + x >= upper:
                return True
            upper = lower + x
        elif m == 'right':
            if left + x >= right:
                return True
            right = left + x
        elif m == 'down':
            if upper - x <= lower:
                return True
            lower = upper - x
    return False
