def solve(arr):
    for num in arr:
        if arr.count(num * -1) == 0:
            return num
