def solve(arr):
    if arr[-1] > arr[-2]:
        if sorted(arr) == arr:
            return "A"
        else:
            return "RA"
    elif arr[-1] < arr[-2]:
        if sorted(arr)[::-1] == arr:
            return "D"
        else:
            return "RD"
