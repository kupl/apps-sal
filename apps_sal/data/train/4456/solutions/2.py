def flatten_me(lst):
    res = []
    for i in lst:
        if type(i) is list:
            res += i
        else:
            res.append(i)
    return res

