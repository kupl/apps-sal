import math


class point:
    def __init__(self, a, b):
        self.x = a
        self.y = b


def fun(self):
    return self.x - (self.y / 20000)


T = int(input())
for j in range(T):
    s = input()
    N = int(input())
    t = [None] * N
    for i in range(N):
        x1, y1 = map(int, input().split())
        t[i] = point(x1, y1)

    t.sort(key=fun)
    d = 0.0
    for i in range(1, N):
        d = d + math.sqrt(((t[i].x - t[i - 1].x) ** 2) + ((t[i].y - t[i - 1].y) ** 2))
    d = round(d, 2)
    print('{:0.2f}'.format(d))
