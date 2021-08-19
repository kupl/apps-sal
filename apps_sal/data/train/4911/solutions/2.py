def sum_arrays(arrays, shift):
    shifted = [[0] * i * shift + a + [0] * (len(arrays) - i - 1) * shift for (i, a) in enumerate(arrays)]
    return list(map(sum, zip(*shifted)))
