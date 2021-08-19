def cat_mouse(stg, j):
    if set('mCD.') - set(stg):
        return 'boring without all three'
    (c, d, m) = (stg.index(a) for a in 'CDm')
    if abs(c - m) > j:
        return 'Escaped!'
    elif m < d < c or c < d < m:
        return 'Protected!'
    else:
        return 'Caught!'
