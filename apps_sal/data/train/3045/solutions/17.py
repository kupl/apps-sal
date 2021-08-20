def elevator(l, r, c):
    return ('right', 'left')[abs(c - l) < abs(c - r)]
