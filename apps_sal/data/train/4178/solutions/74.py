def min_sum(arr):
    temp = sorted(arr)
    return sum(temp[i] * temp[-i - 1] for i in range(len(arr) // 2))
