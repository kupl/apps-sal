def solve(n):
    l = len(str(n)) - 1
    return sum(map(int, str(n - 10**l + 1))) + 9 * l
