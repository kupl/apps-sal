from itertools import combinations


class Point(object):

    def __init__(self, x, y):
        (self.x, self.y) = (x, y)

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


for _ in range(int(input())):
    (n, m) = map(int, input().split())
    (l, dist) = ([], [0] * (n + m - 1))
    for i in range(n):
        c = input()
        for j in range(m):
            if c[j] == '1':
                l.append(Point(i, j))
    total = 0
    for i in combinations(l, 2):
        dist[i[0].distance(i[1])] += 1
    dist.pop(0)
    for i in dist:
        print(i, end=' ')
    print()
