def min_sum(arr):
    sorted_arr = sorted(arr)
    ml = len(sorted_arr)//2
    i = 0
    sum = 0
    while i < ml:
        sum += sorted_arr[i] * sorted_arr[-i-1]
        i += 1
    return sum
