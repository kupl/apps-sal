def main():
    from bisect import bisect_left
    from collections import namedtuple
    from operator import attrgetter
    import sys
    input = sys.stdin.readline
    Event = namedtuple('Event', 'pos start end')
    (N, Q) = map(int, input().split())
    events = []
    for _ in range(N):
        (s, t, x) = map(int, input().split())
        e = Event(pos=x, start=s - x, end=t - x)
        events.append(e)
    events.sort(key=attrgetter('pos'))
    D = [int(input()) for _ in range(Q)]
    ans = [-1] * Q
    see = [-1] * Q
    for e in events:
        left = bisect_left(D, e.start)
        right = bisect_left(D, e.end)
        idx = left
        while idx < right:
            if ~ans[idx]:
                idx = see[idx]
                continue
            ans[idx] = e.pos
            see[idx] = right
            idx += 1
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
