def solve(n):
    if n == 0:
        return '0'
    elif n == 1:
        return '01'
    else:
        return solve(n - 1) + solve(n - 2)
