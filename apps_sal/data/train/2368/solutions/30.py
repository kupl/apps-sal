import sys
def ii(): return sys.stdin.readline().strip()
def idata(): return [int(x) for x in ii().split()]


def solve():
    n = int(ii())
    a = idata()
    b = idata()
    a1, b1 = min(a), min(b)
    ans = 0
    for i in range(n):
        ans += max(b[i] - b1, a[i] - a1)
    print(ans)
    return


for t in range(int(ii())):
    solve()
