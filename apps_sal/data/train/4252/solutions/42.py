def merge_arrays(first, second):
    bigboy = []
    for x in second:
        if x not in bigboy:
            bigboy.append(x)
    for x in first:
        if x not in bigboy:
            bigboy.append(x)
    bigboy.sort()
    return bigboy
