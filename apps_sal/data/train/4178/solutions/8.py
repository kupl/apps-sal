def min_sum(arr):
    arr = sorted(arr)
    return sum([e1 * e2 for e1, e2 in zip(arr[:len(arr) // 2], arr[::-1][:len(arr) // 2])])
