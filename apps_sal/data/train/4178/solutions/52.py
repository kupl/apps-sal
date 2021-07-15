def min_sum(arr):
    arr.sort()
    middle = len(arr) // 2
    return sum(a * b for a, b in zip(arr[:middle], reversed(arr[-middle:])))
