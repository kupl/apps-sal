def min_sum(arr):
    p = sorted(arr)
    return sum((p[i] * p[-(i + 1)] for i in range(int(len(arr) / 2))))
