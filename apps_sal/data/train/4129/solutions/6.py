def queue(q, pos, r=0):
    while True:
        r += 1
        q[0] -= 1
        if q[pos] == 0:
            return r
        q = q[1:] + [q[0]] if q[0] > 0 else q[1:]
        pos -= 1
        if pos < 0:
            pos = len(q) - 1
