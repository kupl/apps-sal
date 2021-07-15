from heapq import heappush, heappop

def n_linear(m, n):
    h = [1]
    x = 0
    for _ in range(n+1):
        x = heappop(h)
        while h and h[0] == x:
            heappop(h)
        for y in m:
            a = y * x + 1
            heappush(h, a)
    return x
