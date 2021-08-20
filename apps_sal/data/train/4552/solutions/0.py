def rankings(arr):
    dct = {v: i for (i, v) in enumerate(sorted(arr, reverse=True), 1)}
    return [dct[v] for v in arr]
