def wheat_from_chaff(values):
    (i, j) = (0, len(values) - 1)
    vals = values[:]
    while i < j:
        if vals[i] < 0:
            i += 1
        elif vals[j] > 0:
            j -= 1
        else:
            (vals[i], vals[j]) = (vals[j], vals[i])
            (i, j) = (i + 1, j - 1)
    return vals
