def nth_smallest(arr, pos):
    if pos > len(arr):
        return max(arr)
    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr) // 2]
    lit = [i for i in arr if i < pivot]
    big = [i for i in arr if i > pivot]
    k = len(arr) - len(big)
    if pos > k:
        return nth_smallest(big, pos - k)
    elif pos > len(lit):
        return pivot
    else:
        return nth_smallest(lit, pos)
