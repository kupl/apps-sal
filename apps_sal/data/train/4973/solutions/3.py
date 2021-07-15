def trouble(x, t):
    res = [x[0]]
    for elem in x[1:]: 
        if elem + res[-1] != t: 
            res.append(elem)
    return res
