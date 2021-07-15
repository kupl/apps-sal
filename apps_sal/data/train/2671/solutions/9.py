def cat_mouse(x,j):
    if not all(['C' in x, 'm' in x, 'D' in x]):
        return 'boring without all three'
    c, m, d = list(map(x.index, ['C', 'm', 'D']))
    if abs(m-c) <= j+1: return ['Caught!', 'Protected!'][x.replace('.', '')[1] == 'D']
    else: return 'Escaped!'

