from collections import Counter


def bucketize(*arr):
    result, arr_count = [None] * (len(arr) + 1), Counter(arr)
    for count in set(arr_count.values()):
        result[count] = sorted(v for v, c in arr_count.items() if c == count)
    return result
