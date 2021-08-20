def solve(arr):
    for i in range(0, len(arr)):
        if -arr[i] not in arr:
            return arr[i]
