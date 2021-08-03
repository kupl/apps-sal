def unflatten(flat_array, depth):
    r = flat_array
    direction = 1
    for d in range(depth):
        r = _unflatten(r, direction)
        direction *= -1
    return r


def _unflatten(flat_array, direction):
    q = flat_array[:]
    r = []
    while(q):
        if direction > 0:
            x = q.pop(0)
        else:
            x = q.pop()
        if type(x) == list:
            if direction > 0:
                r.append(_unflatten(x, direction))
            else:
                r.insert(0, _unflatten(x, direction))
        elif x % (len(q) + 1) < 3:
            if direction > 0:
                r.append(x)
            else:
                r.insert(0, x)
        else:
            t = [x]
            for _ in range(x % (len(q) + 1) - 1):
                if not q:
                    break
                if direction > 0:
                    t.append(q.pop(0))
                else:
                    t.append(q.pop())
            if direction > 0:
                r.append(t)
            else:
                r.insert(0, t[::-1])
    return r
