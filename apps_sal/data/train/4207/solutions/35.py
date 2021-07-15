def sum_cubes(n):
    ans = 0
    while n > 0:
        ans += pow(n, 3)
        n -= 1
    return ans
