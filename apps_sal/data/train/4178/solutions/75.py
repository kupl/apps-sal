def min_sum(arr):
    return sum((a * b for (a, b) in zip(sorted(arr)[:len(arr) // 2], sorted(arr)[len(arr) // 2:][::-1])))
