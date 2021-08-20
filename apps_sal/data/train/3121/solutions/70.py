def solve(arr):
    for (i, v) in enumerate(arr):
        isTrue = False
        for (k, kv) in enumerate(arr):
            if i == k:
                continue
            if v == arr[k] * -1:
                isTrue = True
                break
        if isTrue == False:
            return v
