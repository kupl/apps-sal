def row_weights(arr):
    even = sum([el for (i, el) in enumerate(arr) if i % 2 == 0])
    odd = sum([el for (i, el) in enumerate(arr) if i % 2 == 1])
    return (even, odd)
