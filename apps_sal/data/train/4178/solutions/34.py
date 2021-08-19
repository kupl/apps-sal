def min_sum(arr):
    l1 = sorted(arr)
    return sum((l1[i] * l1[~i] for i in range(len(arr) // 2)))
