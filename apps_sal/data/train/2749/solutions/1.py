def solve(arr):
    if sorted(arr) == arr:
        return 'A'
    if sorted(arr)[::-1] == arr:
        return 'D'
    return 'RA' if arr[0] > arr[-1] else 'RD'
