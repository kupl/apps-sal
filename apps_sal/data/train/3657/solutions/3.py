def series_slices(d, n):
    # Good Luck!
    if(n > len(d)):
        return error
    x = []
    i = 0
    while(i <= len(d) - n):
        x.append([int(i) for i in d[i:i + n]])
        i += 1
    return x
