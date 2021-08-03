import bisect


def __starting_point():
    n = int(input())
    beacon = [tuple(map(int, input().split())) for _ in range(n)]
    beacon.sort()

    destroyed = [0] * n
    for i in range(n):
        lo = beacon[i][0] - beacon[i][1]
        pos = bisect.bisect_left(beacon, (lo, -1), hi=i - 1)
        if beacon[pos][0] >= lo:
            pos -= 1
        if pos < 0:
            destroyed[i] = i
        else:
            destroyed[i] = max(0, i - pos - 1 + destroyed[pos])

    best = n
    for i, v in enumerate(destroyed):
        best = min(best, v + n - i - 1)
    print(best)


__starting_point()
