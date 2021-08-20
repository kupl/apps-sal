def solve(arr):
    check = []
    for i in arr:
        if -i not in arr:
            return i
