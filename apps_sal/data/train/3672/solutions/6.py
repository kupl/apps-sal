def solve(s):
    return sum((len(s) - i for (i, j) in enumerate(s[::-1]) if int(j) % 2 == 1))
