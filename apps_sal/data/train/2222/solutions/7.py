import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return map(int, minp().split())


def main():
    (n, k) = mints()
    a = [list(minp()) for i in range(3)]
    w = [[False] * (n + 1) for i in range(3)]
    for j in range(3):
        if a[j][0] == 's':
            a[j][0] = '.'
            w[j][0] = True
    for i in range(n):
        for j in range(3):
            if w[j][i]:
                if i * 3 + 1 >= n or a[j][i * 3 + 1] == '.':
                    for z in range(max(j - 1, 0), min(j + 2, 3)):
                        if (i * 3 + 1 >= n or a[z][i * 3 + 1] == '.') and (i * 3 + 2 >= n or a[z][i * 3 + 2] == '.') and (i * 3 + 3 >= n or a[z][i * 3 + 3] == '.'):
                            w[z][i + 1] = True
    can = w[0][n] or w[1][n] or w[2][n]
    if can:
        print('YES')
    else:
        print('NO')


t = mint()
for i in range(t):
    main()
