def g2(n):
    l = []
    while n:
        l.append(n % 12)
        n /= 12
    for x in reversed(l):
        if x >= 6:
            return 0
        if x >= 4:
            return 3
        if x >= 2:
            return 2
        if x >= 1:
            return 1
    return 0


def solve(n, a):
    r = 0
    for x in a:
        r ^= g2(x)
    return r


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().strip().split()))
    r = solve(n, a)
    if r == 0:
        print('Derek')
    else:
        print('Henry')
