def greatest_distance(arr):
    indexes, d = {}, 0
    for i, n in enumerate(arr):
        if n in indexes:
            d = max(d, i - indexes[n])
        else:
            indexes[n] = i
    return d
