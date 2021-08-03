def sum_cubes(n):
    ans = 0
    for x in range(1, n + 1):
        ans += x ** 3
    return ans
