def solve(arr):
    (arr, res, n, i) = (sorted(arr), 1, len(arr), 0)
    while i < n and res >= arr[i]:
        (res, i) = (res + arr[i], i + 1)
    return res
