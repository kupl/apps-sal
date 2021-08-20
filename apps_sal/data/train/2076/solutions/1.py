n = int(input())
p = [tuple(map(int, input().split())) for i in range(n)]


def d(a, b):
    return tuple((x - y for (x, y) in zip(a, b)))


def m(a, b):
    return sum((x * y for (x, y) in zip(a, b)))


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
