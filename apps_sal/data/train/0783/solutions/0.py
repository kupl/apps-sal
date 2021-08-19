epi = 10 ** (-2)


def vision(t):
    a1 = x0 + dx * t - x1
    a2 = y0 + dy * t - y1
    a3 = z0 + dz * t - z1
    b = 4 * (a1 * d1 + a2 * d2 + a3 * d3) * (a1 * d1 + a2 * d2 + a3 * d3)
    a = 4 * (a1 * a1 + a2 * a2 + a3 * a3)
    value = b - a * c
    return value


xrange = range
for _ in range(int(input())):
    (x1, y1, z1, x0, y0, z0, dx, dy, dz, cx, cy, cz, r) = list(map(int, input().split()))
    d1 = x1 - cx
    d2 = y1 - cy
    d3 = z1 - cz
    c = d1 * d1 + d2 * d2 + d3 * d3 - r * r
    low = 0
    high = 10 ** 9 + 1
    while low < high - 10 ** (-6):
        mid = low + (high - low) * 1.0 / 2
        value = vision(mid)
        if abs(value) <= epi:
            break
        elif value > 0:
            low = mid
        else:
            high = mid
    print(mid)
