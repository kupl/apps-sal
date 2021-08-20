import heapq


def solve():
    n = int(input())
    cur = 1
    a = [0] * n
    q = []
    heapq.heappush(q, (-n, 0, n))
    while q:
        (_, l, r) = heapq.heappop(q)
        mid = (l + r - 1) // 2
        a[mid] = cur
        cur += 1
        if l < mid:
            heapq.heappush(q, (l - mid, l, mid))
        if mid + 1 < r:
            heapq.heappush(q, (mid + 1 - r, mid + 1, r))
    print(*a)


t = int(input())
for _ in range(t):
    solve()
