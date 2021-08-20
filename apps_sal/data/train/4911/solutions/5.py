import itertools


def sum_arrays(arrays, shift):
    return [sum(xs) for xs in itertools.zip_longest(*[[0] * (shift * i) + a for (i, a) in enumerate(arrays)], fillvalue=0)]
