def solve(arr):
    result = arr[0]
    for i in range(len(arr)):
        pair = False
        for j in range(len(arr)):
            if arr[i] == -arr[j]:
                pair = True
        if not pair:
            result = arr[i]
    return result
