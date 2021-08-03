import bisect


def min_destroyed(beacons):
    beacons.sort()
    dest = []
    for i, (a, b) in enumerate(beacons):
        pos = bisect.bisect_left(beacons, (a - b, 0), hi=i)
        if pos == 0:
            dest.append(i)
        else:
            dest.append(dest[pos - 1] + i - pos)

    n = len(beacons)
    return min(d + (n - i - 1) for i, d in enumerate(dest))


def __starting_point():
    n = int(input())
    beacons = []
    for _ in range(n):
        a, b = list(map(int, input().split()))
        beacons.append((a, b))
    print(min_destroyed(beacons))


__starting_point()
