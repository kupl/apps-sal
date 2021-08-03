def elevator(l, r, c):
    ld = abs(l - c)
    rd = abs(r - c)
    if rd <= ld:
        return "right"
    else:
        return "left"
