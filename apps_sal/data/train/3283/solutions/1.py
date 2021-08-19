import math


def union_jack(n):
    if type(n) not in [int, float]:
        return False
    if n < 7:
        n = 7
    n = math.ceil(n)
    x = '-' * (n // 2 - 1) + 'XX' + '-' * (n // 2 - 1) if n % 2 == 0 else '-' * (n // 2) + 'X' + '-' * (n // 2)
    tmp = list(x)
    (ans, n1) = ([], n // 2 if n % 2 != 0 else n // 2 - 1)
    for i in range(n1):
        t = tmp[:]
        t[i] = 'X'
        t[-i - 1] = 'X'
        ans.append(''.join(t))
    center = 'X' * n if n % 2 != 0 else 'X' * n + '\n' + 'X' * n
    return '\n'.join(ans + [center] + ans[::-1])
