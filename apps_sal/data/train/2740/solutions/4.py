def wheat_from_chaff(values):
    (i, j) = (0, len(values) - 1)
    while i < j:
        (a, b) = (values[i], values[j])
        if a > 0 and b < 0:
            (values[i], values[j]) = (values[j], values[i])
        elif b > 0:
            j -= 1
        else:
            i += 1
    return values
