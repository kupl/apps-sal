def min_sum(arr):
    arr = sorted(arr)
    s = [arr[i] * arr[-i - 1] for i in range(len(arr) // 2)]
    return sum(s)
