def min_sum(arr):
    arr.sort()
    return sum(a * b for a, b in zip(arr[:len(arr) // 2], arr[::-1]))
