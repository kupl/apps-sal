def min_sum(arr):
    lst = sorted(arr)
    return sum(lst[i] * lst[-i - 1] for i in range(len(lst) // 2))
