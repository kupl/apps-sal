def array_manip(array):
    res = []
    for i, n in enumerate(array):
        try:
            res.append(min([x for x in array[i+1:] if x > n]))
        except ValueError:
            res.append(-1)
    return res
