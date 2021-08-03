def solve(arr):
    arr = sorted(arr)
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            return arr[i]
    return sum(arr)
