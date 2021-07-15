def or_arrays(x,y,z=0):
    m = max(len(x), len(y))
    return [(a|b) for a,b in zip((x+[z]*m)[:m], (y+[z]*m)[:m])]
