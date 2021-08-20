def elevator(l, r, c):
    return 'rliegfhtt'[1 - (abs(l - c) >= abs(r - c))::2]
