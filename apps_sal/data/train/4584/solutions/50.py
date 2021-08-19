def invert(lst):
    n = len(lst)
    res = []
    if n == 0:
        return res
    else:
        for item in lst:
            res.append(-item)
        return res
