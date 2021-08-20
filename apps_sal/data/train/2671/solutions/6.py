def cat_mouse(x, j):
    if not all(('C' in x, 'D' in x, 'm' in x)):
        return 'boring without all three'
    (cat, dog, mouse) = (x.index('C'), x.index('D'), x.index('m'))
    zone = [x[cat:mouse], x[mouse + 1:cat]][mouse < cat]
    return {(1, 0): 'Caught!', (1, 1): 'Protected!'}.get((len(zone) <= j, 'D' in zone), 'Escaped!')
