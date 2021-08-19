def min_sum(arr):
    s = sorted(arr)
    return sum((x * y for (x, y) in zip(s[:len(s) // 2], s[len(s) // 2:][::-1])))
