def solve(n):
    if n < 1: return str(n)
    if n < 2: return solve(n-1) + str(n)
    return solve(n-1) + solve(n-2)
