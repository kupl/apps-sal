def solve(arr):
    for i in arr:
        if i and -i not in arr:
            return i
