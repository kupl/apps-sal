def min_sum(arr):
    arr.sort()
    return sum(i * arr.pop() for i in arr)
