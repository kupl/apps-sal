def min_sum(arr):
    return (sum(sorted(arr)[i] * sorted(arr)[len(arr) - 1 - i] for i in range(len(arr))) / 2)
