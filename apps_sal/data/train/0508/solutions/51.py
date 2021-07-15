def main():
    import sys
    input = lambda : sys.stdin.readline().rstrip()

    from heapq import heappush, heappop 

    running = []
    events = []
    delete = set()

    n, q = list(map(int, input().split()))
    for _ in range(n):
        s, t, x = list(map(int, input().split()))
        time = max(s - x, 0)
        if t - x < 0:
            continue
        events.append((s - x, x, 1)) # 追加イベント
        events.append((t - x, x, 0)) # 削除イベント
    events.sort()
    ans = []
    idx = -1
    for _ in range(q):
        d = int(input())
        if d >= events[-1][0]:
            print((-1))
            continue
        while events[idx + 1][0] <= d:
            idx += 1
            if events[idx][2] == 1:
                heappush(running, events[idx][1])
                delete.discard(events[idx][1])
            else:
                delete.add(events[idx][1])
        flag = 1
        while running:
            x = heappop(running)
            if x not in delete:
                heappush(running, x)
                print(x)
                flag = 0
                break
        if flag:
            print((-1))
def __starting_point():
    main()




__starting_point()
