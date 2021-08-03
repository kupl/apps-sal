import sys


def input(): return sys.stdin.readline().strip()
def iinput(): return int(input())
def rinput(): return list(map(int, sys.stdin.readline().strip().split()))
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))


t = iinput()

for _ in range(t):
    n = iinput()
    p = []
    mi = []
    for i in range(n):
        x, y = rinput()
        p.append(x + y)
        mi.append(x - y)

    p.sort()
    mi.sort()
    m = float('inf')
    for i in range(1, n):
        if(p[i] - p[i - 1] < m):
            m = p[i] - p[i - 1]
        if(mi[i] - mi[i - 1] < m):
            m = mi[i] - mi[i - 1]

    if m % 2 == 0:
        print(m // 2)
    else:
        print(m / 2)
