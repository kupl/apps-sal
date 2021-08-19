def main():
    import sys

    def input():
        return sys.stdin.readline().rstrip()
    from heapq import heappush, heappop
    running = []
    events = []
    delete = set()
    (n, q) = list(map(int, input().split()))
    for _ in range(n):
        (s, t, x) = list(map(int, input().split()))
        events.append((s - x, x, 1))
        events.append((t - x, x, 0))
    for _ in range(q):
        d = int(input())
        events.append((d, 10 ** 10, 2))
    events.sort()
    for i in range(len(events)):
        temp = events[i]
        if temp[-1] == 1:
            heappush(running, temp[1])
            delete.discard(temp[1])
        elif temp[-1] == 0:
            delete.add(temp[1])
        else:
            flag = 1
            while running:
                p = heappop(running)
                if p not in delete:
                    flag = 0
                    heappush(running, p)
                    print(p)
                    break
            if flag:
                print(-1)


def __starting_point():
    main()


__starting_point()
