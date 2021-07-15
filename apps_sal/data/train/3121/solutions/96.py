def solve(arr):
    return [i for i in arr if arr.count(-i) == 0][0]
