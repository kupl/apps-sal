from heapq import heappush, heappop
for _ in range(int(input())):
    n = int(input())
    pq = [(-n, 1, n)]
    a = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        (sz, l, r) = heappop(pq)
        j = (l + r) // 2 if (r - l + 1) % 2 else (l + r - 1) // 2
        a[j] = i
        if j + 1 <= r:
            heappush(pq, (-(r - (j + 1) + 1), j + 1, r))
        if l <= j - 1:
            heappush(pq, (-(j - 1 - l + 1), l, j - 1))
    print(*a[1:])
