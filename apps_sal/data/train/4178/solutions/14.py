def min_sum(arr):
    arr.sort()
    return sum(x * y for x, y in zip(arr[len(arr) // 2:], arr[:len(arr) // 2][::-1]))
