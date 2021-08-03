import sys
stdin = sys.stdin

sys.setrecursionlimit(10 ** 7)


def li(): return map(int, stdin.readline().split())
def li_(): return map(lambda x: int(x) - 1, stdin.readline().split())
def lf(): return map(float, stdin.readline().split())
def ls(): return stdin.readline().split()
def ns(): return stdin.readline().rstrip()
def lc(): return list(ns())
def ni(): return int(stdin.readline())
def nf(): return float(stdin.readline())


n, t = li()
a = list(li())

mina = [0] * n
mina[0] = a[0]
maxprof = 0

for i in range(1, n):
    mina[i] = min(mina[i - 1], a[i])

ans = 0
for i in range(n):
    if a[i] - mina[i] > maxprof:
        maxprof = a[i] - mina[i]
        ans = 1

    elif a[i] - mina[i] == maxprof:
        ans += 1

print(ans)
