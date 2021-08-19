import bisect
for _ in range(int(input())):
    n = int(input())
    (x1, x2, x3) = ([], [], [])
    for i in range(n):
        (x, y) = list(map(int, input().split()))
        if x == 1:
            x1.append(y)
        if x == 2:
            x2.append(y)
        if x == 3:
            x3.append(y)
    x1.sort()
    x2.sort()
    x3.sort()
    (y1, y2, y3) = (len(x1), len(x2), len(x3))
    area = 0
    for i in range(y1):
        for j in range(i + 1, y1):
            area += abs(x1[i] - x1[j]) * (y2 + 2 * y3)
    for i in range(y3):
        for j in range(i + 1, y3):
            area += abs(x3[i] - x3[j]) * (y2 + 2 * y1)
    for i in range(y2):
        for j in range(i + 1, y2):
            area += abs(x2[i] - x2[j]) * (y1 + y3)
    area /= 2
    s1 = [0]
    for i in range(y2):
        s1.append(s1[-1] + x2[i])
    s2 = [0]
    for i in range(y2):
        s2.append(s2[-1] + x2[y2 - 1 - i])
    for i in x1:
        for j in x3:
            p1 = (i + j) / 2
            p = bisect.bisect_left(x2, p1)
            l = p
            h = y2 - l
            area += p1 * l - s1[l]
            area += s2[h] - p1 * h
    print(format(area, 'f'))
