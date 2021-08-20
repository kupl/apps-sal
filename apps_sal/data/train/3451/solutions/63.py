def triangle(row):
    colors = ['R', 'G', 'B']
    result = list(row)
    while len(result) > 1:
        current = list()
        for (i, j) in zip(result[:-1], result[1:]):
            if i == j:
                current.extend([i])
            else:
                for c in colors:
                    if c not in [i, j]:
                        current.extend([c])
        result = current
    return result[0]
