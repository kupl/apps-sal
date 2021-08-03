import math


def union_jack(n):
    if type(n) not in (int, float):
        return False
    n = max(7, math.ceil(n))
    ans = [['-'] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n - 1 or i in [n // 2, (n - 1) // 2] or j in [n // 2, (n - 1) // 2]:
                ans[i][j] = "X"
    return '\n'.join(''.join(i) for i in ans)
