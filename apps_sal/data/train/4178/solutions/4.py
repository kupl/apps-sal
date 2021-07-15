def min_sum(arr):
    return sum(x * y for x, y in zip(sorted(arr)[::2], sorted(arr)[-1::-2]))
