def solve(arr):
    miss = 1
    for a in sorted(arr):
        if a > miss:
            break
        miss += a
    return miss
