def max_tri_sum(arr):
    arr = list(reversed(sorted(set(arr))))
    total = 0
    for i in range(0, 3):
        total += arr[i]
    return total
