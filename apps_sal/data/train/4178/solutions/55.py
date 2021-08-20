def min_sum(arr):
    arr = sorted(arr)
    return sum([x * y for (x, y) in zip(arr[0:len(arr) // 2], arr[len(arr) // 2:][::-1])])
