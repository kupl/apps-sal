def solve(arr):
    for i in range(len(arr)):
        while i + 1 < len(arr) + 1 and arr[i] in arr[i + 1:]:
            arr.pop(i)
    return arr
