def solve(arr):
    for i in range(len(arr)):
        if -1 * arr[i] not in arr[0:i] + arr[i + 1:]:
            return arr[i]
