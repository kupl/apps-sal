def elevator(l, r, c):
    return 'right' if abs(r - c) <= abs(l - c) else 'left'
