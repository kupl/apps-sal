def int_diff(arr, n):
    cnt = 0
    for i, x in enumerate(arr):
        for y in arr[i+1:]:
           if abs(x-y) == n:
               cnt += 1
    return cnt

