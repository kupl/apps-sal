def min_sum(arr):
    low, high = sorted(arr)[:len(arr) // 2], sorted(arr, reverse=True)[:len(arr) // 2]
    return sum(x * y for x, y in zip(low, high))
