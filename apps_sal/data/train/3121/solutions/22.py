def solve(arr):
    return [el for el in arr if -el not in arr ][0]
