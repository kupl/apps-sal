from math import ceil

def union_jack(n):
    if not isinstance(n, int) and not isinstance(n, float):
        return False
    n = max(7, ceil(n))
    data = [['-'] * n for _ in range(n)]
    for y in range(n):
        data[y][y] = 'X'
        data[y][n-y-1] = 'X'
    col_row = [n // 2] if n % 2 else [n // 2 - 1, n // 2]
    for cr in col_row:
        data[cr] = ['X'] * n
        for y in range(n):
            data[y][cr] = 'X'
    return '\n'.join(''.join(d) for d in data)
