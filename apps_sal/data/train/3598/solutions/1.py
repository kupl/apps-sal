def plane_seat(a):
    (n, c) = (int(a[:-1]), a[-1])
    side = 'Left' if c in 'ABC' else 'Middle' if c in 'DEF' else 'Right' if c in 'GHK' else ''
    depth = 'Front' if 0 < n < 21 else 'Middle' if 20 < n < 41 else 'Back' if 40 < n < 61 else ''
    return f'{depth}-{side}' if depth and side else 'No Seat!!'
