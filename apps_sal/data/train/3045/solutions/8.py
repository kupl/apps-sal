def elevator(left, right, call):
    dr = abs(call - right)
    dl = abs(call - left)
    return 'left' if dr > dl else 'right'
