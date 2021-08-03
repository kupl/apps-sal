def solve(arr):
    arr.sort()
    d = arr[2] - arr[1]
    if d > arr[0]:
        return arr[0] + arr[1]
    return arr[1] + d + (arr[0] - d) // 2
