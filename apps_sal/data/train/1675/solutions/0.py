from math import sqrt


def get_distance(x1, y1, x2, y2):
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


T = int(input())
ans = []
for _ in range(T):
    blank = input()
    N = int(input())
    C = [[] for i in range(10 ** 4 + 1)]
    for i in range(N):
        (x, y) = [int(i) for i in input().split()]
        C[x].append(y)
    distance = 0
    lastx = None
    lasty = None
    for i in range(10 ** 4 + 1):
        if C[i] != []:
            max_ci = max(C[i])
            min_ci = min(C[i])
            if lastx != None and lasty != None:
                distance += get_distance(lastx, lasty, i, max_ci)
            distance += max_ci - min_ci
            lastx = i
            lasty = min_ci
    ans.append('{:.2f}'.format(distance))
for i in ans:
    print(i)
