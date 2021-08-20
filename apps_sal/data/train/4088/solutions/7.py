def tetris(a):
    (b, glob_min) = ([0] * 9, 29)
    for (x, y, z) in a:
        i = int(z) * (-1) ** (y == 'R')
        b[i] += int(x)
        if b[i] > glob_min:
            n = min(b)
            if b[i] - n > 29:
                return n
            glob_min = n + 29
    return min(b)
