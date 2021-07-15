def solve(n):
    a = (len(str(n)) - 1) * '9' or '0'
    return sum(map(int, a + str(n - int(a))))
