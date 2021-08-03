def solve(arr):
    arr2 = []
    for i in range(len(arr)):
        if arr[i] not in arr[i + 1:]:
            arr2.append(arr[i])
    return arr2
