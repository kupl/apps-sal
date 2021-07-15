def solve(arr):
    res = 1
    for a in arr: res *= len(set(a))
    return res

