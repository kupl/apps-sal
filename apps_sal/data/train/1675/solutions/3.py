test = int(input())
for _ in range(test):
    blank = input()
    n = int(input())
    points = {}
    for i in range(n):
        temp = list(map(int, input().split()))
        if temp[0] in points:
            points[temp[0]].append(temp[1])
        else:
            points[temp[0]] = [temp[1]]
    for i in points:
        points[i].sort(reverse=True)
    x1 = -1
    y1 = -1
    distance = 0.0
    xpoints = list(points.keys())
    xpoints.sort()
    for i in xpoints:
        ypoints = points[i]
        for j in ypoints:
            if x1 == -1 and y1 == -1:
                x1 = i
                y1 = j
                continue
            else:
                distance += ((x1 - i) ** 2 + (y1 - j) ** 2) ** 0.5
                x1 = i
                y1 = j
    print('%.2f' % distance)
