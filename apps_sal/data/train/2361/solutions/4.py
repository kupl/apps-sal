from heapq import *
t = int(input())

while t:
    t -= 1
    n = int(input())
    q = []
    heappush(q, (-n, 0, n - 1))
    arr = [0] * n
    for i in range(n):
        # print(q)
        # print(arr)
        p = heappop(q)
        l, r = p[1], p[2]
        mid = (l + r) // 2
        arr[mid] = i + 1
        if mid - l > 0:
            heappush(q, (-mid + l, l, mid - 1))
        if r - mid > 0:
            heappush(q, (-r + mid, mid + 1, r))
    print(*arr)
