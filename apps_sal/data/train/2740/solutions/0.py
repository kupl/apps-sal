def wheat_from_chaff(values):
    i, j = 0, len(values) - 1
    while True:
        while i < j and values[i] < 0:
            i += 1
        while i < j and values[j] > 0:
            j -= 1
        if i >= j:
            return values
        values[i], values[j] = values[j], values[i]
