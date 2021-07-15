def segments(m, a):
    return([i for i in range (m+1) if not any([i in range(x[0], x[1]+1) for x in a])])
