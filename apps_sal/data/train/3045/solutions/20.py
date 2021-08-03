def elevator(l, r, c):
    if l - c < 0:
        left = -(l - c)
    else:
        left = l - c
    if r - c < 0:
        right = -(r - c)
    else:
        right = r - c
    return 'left' if left < right else 'right'
