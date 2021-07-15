def main():
    import sys
    input = lambda : sys.stdin.readline().rstrip()

    from heapq import heappush, heappop 

    running = [] # 止まりうる座標
    events = [] # 時刻順のイベント
    finished = set() # 工事が終了した座標

    n, q = map(int, input().split())
    for _ in range(n):
        s, t, x = map(int, input().split())
        events.append((s - x, x, 1)) # 追加イベント
        events.append((t - x, x, 0)) # 削除イベント
    for _ in range(q):
        d = int(input())
        events.append((d, 10**10, 2)) # 出発イベント,同じ時刻内で最後になるよう第二引数設定
    events.sort()
    for i in range(len(events)):
        temp = events[i]
        if temp[-1] == 1:
            heappush(running, temp[1])
            finished.discard(temp[1])
        elif temp[-1] == 0:
            finished.add(temp[1])
        else:
            flag = 1
            while running:
                p = heappop(running)
                if p not in finished:
                    flag = 0
                    heappush(running, p)
                    print(p)
                    break
            if flag:
                print(-1)
def __starting_point():
    main()
__starting_point()
