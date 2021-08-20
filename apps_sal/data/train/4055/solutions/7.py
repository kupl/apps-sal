def solve(n):
    if n == 0:
        return '0'
    if n == 1:
        return '01'
    return f'{solve(n - 1)}{solve(n - 2)}'
