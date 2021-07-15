def wheat_from_chaff(values):
    end = len(values) - 1
    for start, n in enumerate(values):
        if start >= end: break
        if n > 0:
            while start < end and values[end] > 0: end -= 1
            values[start], values[end] = values[end], values[start]
    return values
