def cat_mouse(x,j):
    d, c, m = x.find('D'), x.find('C'), x.find('m')
    if -1 in [d, c, m]:
        return 'boring without all three'
    if abs(c - m) <= j:
        return 'Protected!' if c < d < m or m < d < c else 'Caught!' 
    return 'Escaped!'
