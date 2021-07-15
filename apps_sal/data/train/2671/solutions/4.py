def cat_mouse(x,j):
    try:
        d, c, m = map(x.index,'DCm')
    except ValueError:
        return 'boring without all three'
    if j < abs(c - m)-1 : return 'Escaped!'
    elif c>d>m or m>d>c : return 'Protected!'
    return 'Caught!'
