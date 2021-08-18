from bisect import bisect_right
import sys
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))


N = I()
x = LI()
L = I()


arrive = [[0] * N for _ in range(30)]
for k in range(30):
    if k == 0:
        for i in range(N):
            arrive[0][i] = bisect_right(x, x[i] + L) - 1
    else:
        for i in range(N):
            arrive[k][i] = arrive[k - 1][arrive[k - 1][i]]


def query(a, b):
    a -= 1
    b -= 1
    ans = 1
    for k in range(29, -1, -1):
        if arrive[k][a] >= b:
            continue
        else:
            a = arrive[k][a]
            ans += 1 << k
    print(ans)


Q = I()
for i in range(Q):
    a, b = MI()
    if a > b:
        a, b = b, a
    query(a, b)
