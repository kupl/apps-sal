def solve(arr):
    for index, value in enumerate(arr):
        if value * -1 in arr:
            continue
        else:
            return value
