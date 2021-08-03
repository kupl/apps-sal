from itertools import zip_longest


def sum_arrays(arrays, shift):
    shifted = [([0] * shift * i) + array for i, array in enumerate(arrays)]
    return [sum(nums) for nums in zip_longest(*shifted, fillvalue=0)]
