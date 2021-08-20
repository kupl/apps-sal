def elevator(l, r, c):
    return 'rliegfhtt'[abs(c - l) < abs(c - r)::2]
