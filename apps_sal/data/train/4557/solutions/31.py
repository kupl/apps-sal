def row_weights(arr):
    s = sum([el for (i, el) in enumerate(arr) if i % 2 == 0])
    return (s, sum(arr) - s)
