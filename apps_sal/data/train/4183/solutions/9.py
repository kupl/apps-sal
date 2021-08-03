from collections import Counter


def greatest_distance(arr):
    r_arr, count_arr = arr[::-1], Counter(arr)
    return max(len(arr) - 1 - r_arr.index(k) - arr.index(k) if c > 1 else 0 for k, c in count_arr.items())
