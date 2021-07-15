def solve(arr):
    x = 1
    for a in arr:
        x *= len(set(a))
    return x
