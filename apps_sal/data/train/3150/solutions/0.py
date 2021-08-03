def binary_cleaner(seq):
    res = ([], [])
    for i, x in enumerate(seq):
        if x < 2:
            res[0].append(x)
        else:
            res[1].append(i)
    return res
