import math


def union_jack(n):
    if not isinstance(n, int) and (not isinstance(n, float)):
        return False
    n = max(7, math.ceil(n))
    m = n // 2 - 1 if n % 2 == 0 else (n - 1) // 2
    vertical = 'XX' if n % 2 == 0 else 'X'
    horizontal = 'X' * n + '\n' + 'X' * n if n % 2 == 0 else 'X' * n
    str = ''
    for i in range(m):
        s = ''
        for j in range(m):
            s += 'X' if i == j else '-'
        str += s + vertical + s[::-1] + '\n'
    return str + horizontal + str[::-1]
