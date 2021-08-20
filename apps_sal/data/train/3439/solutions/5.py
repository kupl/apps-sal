def solve(n):
    a = 10 ** (len(str(n)) - 1) - 1
    return sum(map(int, str(a) + str(n - a)))
