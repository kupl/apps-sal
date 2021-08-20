def elevator(l, r, c):
    if l == c and r != c:
        return 'left'
    elif r == c:
        return 'right'
    elif c > r and r > l:
        return 'right'
    elif r > c and c > l:
        return 'right'
    elif r == l and r != c:
        return 'right'
    elif l > c and l > r:
        return 'right'
    else:
        return 'left'
