def min_sum(arr):
    sort = sorted(arr)
    return sum(x * y for x, y in zip(sort, sort[::-1])) // 2
