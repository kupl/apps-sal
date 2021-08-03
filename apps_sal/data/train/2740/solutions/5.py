def wheat_from_chaff(values):
    values = values[:]
    i, j = 0, len(values) - 1
    while i < j:
        while values[i] < 0:
            i += 1
        while values[j] > 0:
            j -= 1
        if i < j:
            values[i], values[j] = values[j], values[i]
    return values
