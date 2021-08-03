def min_sum(arr):
    ls = sorted(arr)
    return sum(ls[i] * ls[-i - 1] for i in range(len(ls) // 2))
