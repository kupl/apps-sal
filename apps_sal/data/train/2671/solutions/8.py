def cat_mouse(x,j):
    c,d,m = [x.find(ch) for ch in 'CDm']
    if -1 in [c,d,m]: return "boring without all three"
    if abs(c-m)-1 <= j: return "Protected!" if (c<d<m or m<d<c) else "Caught!"
    return "Escaped!"
