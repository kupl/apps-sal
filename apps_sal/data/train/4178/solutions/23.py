def min_sum(arr):
    halflig = len(arr) // 2
    arr.sort()

    return sum(arr[x] * arr[-(x + 1)] for x in range(halflig))
