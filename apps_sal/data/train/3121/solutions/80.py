def solve(arr):
    newArr = []
    for x in arr:
        if x * -1 not in arr:
            return x
