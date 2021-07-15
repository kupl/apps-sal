def flatten_me(lst):
    res = []
    for x in lst:
        if type(x) == list: 
            for y in x: res.append(y)
        else:
            res.append(x)
    return res

