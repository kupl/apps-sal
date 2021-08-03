import heapq
for _ in range(int(input())):
    n = int(input())
    a = [0] * n
    que = [(-n, 0, n - 1)]
    heapq.heapify(que)
    i = 1
    while que:
        len, l, r = heapq.heappop(que)
        if len % 2 == 1:
            a[(l + r) // 2] = i
            if r != l:
                nl = (-(r - l) // 2, l, (l + r) // 2 - 1)
                nr = (-(r - l) // 2, (l + r) // 2 + 1, r)
                heapq.heappush(que, nl)
                heapq.heappush(que, nr)
        else:
            a[(l + r - 1) // 2] = i
            nl = (-(r - l - 1) // 2, l, (l + r - 1) // 2 - 1)
            nr = (-(r - l + 1) // 2, (l + r - 1) // 2 + 1, r)
            if r == l + 1:
                heapq.heappush(que, nr)
            else:
                heapq.heappush(que, nr)
                heapq.heappush(que, nl)
        i += 1
    print(*a)
