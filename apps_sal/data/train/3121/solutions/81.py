def solve(arr):
    for num in arr:
        if -1 * num not in arr:
            return num
