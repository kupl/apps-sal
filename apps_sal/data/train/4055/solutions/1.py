def solve(n):
    return "0" if n == 0 else "01" if n == 1 else solve(n - 1) + solve(n - 2)
