def even_numbers(arr, n):
    res = []
    cnt = 0
    idx = len(arr) - 1
    while cnt != n:
        if arr[idx] % 2 == 0:
            cnt += 1
            res = [arr[idx]] + res
        idx = idx - 1
    return res
