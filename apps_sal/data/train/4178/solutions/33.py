from itertools import combinations


def min_sum(arr):
    s_arr = sorted(arr)
    n = len(arr) // 2
    l = [*zip(s_arr[:n], s_arr[-1:-n - 1:-1])]
    return sum(x * y for x, y in l)
