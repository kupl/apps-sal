def pick_peaks(arr):
    cast = []

    for i, e in enumerate(arr):
        if cast and e == cast[-1][0]:
            continue
        cast.append((e, i))

    doc = {"pos": [], "peaks": []}

    for i in range(1, len(cast) - 1):
        if cast[i - 1][0] < cast[i][0] > cast[i + 1][0]:
            doc['peaks'].append(cast[i][0])
            doc['pos'].append(cast[i][1])

    return doc
