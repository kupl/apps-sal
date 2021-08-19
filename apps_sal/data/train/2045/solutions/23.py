import sys


def I():
    return int(input())


def readline():
    return sys.stdin.readline().strip('\n')


RM = readmap = lambda x=int: list(map(x, readline().split(' ')))
(n, m) = RM()
conq = ['0'] * (n + 1)
nxt = list(range(1, n + 2))
for _ in range(m):
    (l, r, m) = RM()
    cur = l
    while cur <= r:
        if conq[cur] == '0' and cur != m:
            conq[cur] = str(m)
        nx = nxt[cur]
        nxt[cur] = [r + 1, m][cur < m]
        cur = nx
print(' '.join(conq[1:]))
