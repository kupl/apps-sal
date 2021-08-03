def solve(arr):
    return sum(x < y and y * 2 - x in arr for x in arr for y in arr)
