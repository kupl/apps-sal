def invert(lst):
    if lst == []: return []
    res = []
    for x in lst:
        res.append(x * -1) 
    return res
