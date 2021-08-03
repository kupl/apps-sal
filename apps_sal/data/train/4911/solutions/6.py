from itertools import zip_longest


def sum_arrays(arrays, shift):
    new_arr = []
    for i, arr in enumerate(arrays):
        new_arr.append([0] * shift * i + arr)
    return list(map(sum, zip_longest(*new_arr, fillvalue=0)))
