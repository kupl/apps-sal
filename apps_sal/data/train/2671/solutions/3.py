def cat_mouse(x, j):
    c, d, m = (x.find(animal) for animal in 'CDm')
    return ('boring without all three' if c < 0 or d < 0 or m < 0 else
            'Escaped!' if abs(c - m) > j else
            'Protected!' if c < d < m or c > d > m else
            'Caught!')
