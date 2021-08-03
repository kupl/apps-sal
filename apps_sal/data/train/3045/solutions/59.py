def elevator(l, r, c):
    return 'left' if r > l >= c or r < l <= c else 'right'
