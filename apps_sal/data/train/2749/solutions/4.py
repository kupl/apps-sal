def solve(arr):
    if arr == sorted(arr):
        return "A"
    elif arr == sorted(arr, reverse=True):
        return "D"
    elif arr[0]>arr[-1]:
        return "RA"
    else:
        return "RD"
