def solve(n):
    presum, arr = 1, list(range(2, n + 1))
    while arr[0] < len(arr):
        presum += arr[0]
        del arr[::arr[0]]
    return presum + sum(arr)
