def or_arrays(x,y,mod=0):
    m = maxLen = max(len(x), len(y))
    return [(a|b) for a,b in zip((x+[mod]*m)[:m], (y+[mod]*m)[:m])]
