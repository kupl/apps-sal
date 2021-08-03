n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]


def d(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3], a[4] - b[4])


def m(a, b):
    t = 0
    for i in range(5):
        t += a[i] * b[i]
    return t


good_points = []
for i in range(n):
    good = True

    for j in range(n):
        if j == i:
            continue

        ab = d(p[j], p[i])

        for k in range(j + 1, n):
            if k == i:
                continue

            ac = d(p[k], p[i])

            if m(ab, ac) > 0:
                good = False
                break

        if not good:
            break

    if good:
        good_points.append(i)

print(len(good_points))
for i in good_points:
    print(i + 1)
