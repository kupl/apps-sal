def mark_spot(n):
    if not isinstance(n, int) or n < 0 or n % 2 != 1:
        return '?'
    ans = [[' '] * (2 * n - 1) for _ in range(n)]
    for i in range(n):
        ans[i][i * 2] = ans[i][2 * n - 2 * i - 2] = 'X'
    return '\n'.join(''.join(a).rstrip() for a in ans) + '\n'
