def solve(arr):
    for num in arr:
        if not -num in arr:
            return num
