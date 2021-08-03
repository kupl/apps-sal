def solve(n):
    a = []
    for e in [500, 200, 100, 50, 20, 10]:
        a.append(n // e)
        n = n % e
    return [-1, sum(a)][n % 10 == 0]
