import sys
import heapq as hq

readline = sys.stdin.readline
readall = sys.stdin.read
ns = lambda: readline().rstrip()
ni = lambda: int(readline().rstrip())
nm = lambda: map(int, readline().split())
nl = lambda: list(map(int, readline().split()))
prn = lambda x: print(*x, sep='\n')


def solve():
    n = ni()
    a = [0]*n
    q = [(-n, 0, n-1)]
    for i in range(n):
        v, l, r = hq.heappop(q)
        m = (l + r)//2
        a[m] = i + 1
        hq.heappush(q, (-(m-l), l, m-1))
        hq.heappush(q, (-(r-m), m+1, r))
    print(*a)


# solve()

T = ni()
for _ in range(T):
    solve()

