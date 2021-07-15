def solve(arr):
    for i in arr:
        reverse = -i
        if reverse not in arr:
            return i
