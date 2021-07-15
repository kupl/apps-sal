def solve(arr):
    arr.sort()
    days = min(arr[1] + arr[0], arr[2])
    otherDays = (arr[0] + arr[1] + arr[2]) // 2
    if arr[1] + arr[0] - arr[2] < 0:
        return days
    return otherDays
