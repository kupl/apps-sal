def rankings(arr):
    d = dict(list(zip(sorted(arr, reverse=True), list(range(1, len(arr) + 1)))))
    return [d[a] for a in arr]
