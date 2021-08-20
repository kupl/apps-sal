def guess_hat_color(a, b, c, d):
    w = 0
    bl = 0
    if b == 'white':
        w += 1
    if b == 'black':
        bl += 1
    if c == 'white':
        w += 1
    if c == 'black':
        bl += 1
    if w == bl:
        return 2
    else:
        return 1
