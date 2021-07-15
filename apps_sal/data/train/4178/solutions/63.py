def min_sum(arr):
    arr.sort()
    l = len(arr)
    return sum(a*b for a,b in zip(arr[:l//2], arr[l//2:][::-1]))
