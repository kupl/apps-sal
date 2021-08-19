def main():
    from heapq import heappush, heappop
    import sys
    sys.setrecursionlimit(10 ** 7)
    (n, q) = map(int, input().split())
    event = []
    for _ in range(n):
        (s, t, x) = map(int, input().split())
        event.append((s - x, 1, x))
        event.append((t - x, -1, x))
    for i in range(q):
        event.append((int(input()), 2, i))
    event.sort()
    ans = [0] * q
    stop = set()
    hq = []
    for (t, op, x) in event:
        if op == 1:
            heappush(hq, x)
            stop.add(x)
        elif op == -1:
            stop.remove(x)
        else:
            while hq and hq[0] not in stop:
                heappop(hq)
            ans[x] = hq[0] if hq else -1
    for x in ans:
        print(x)


main()
