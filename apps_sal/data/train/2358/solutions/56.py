import sys
import math
import heapq

input = sys.stdin.readline

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x, y):
        return Vec(self.x+x, self.y+y)

    def rotate(self, theta):
        x = self.x * math.cos(theta) - self.y * math.sin(theta)
        y = self.x * math.sin(theta) + self.y * math.cos(theta)
        return Vec(x, y)

    def theta(self):
        if self.x == 0:
            if self.y > 0:
                return math.pi/2
            elif self.y < 0:
                return 3* math.pi / 2
            else:
                return 0
        ret = math.atan(self.y / self.x)
        if self.x < 0:
            ret += math.pi
        return ret

    def dist(self, other):
        return math.sqrt((self.x - other.x)** 2 + (self.y - other.y)** 2)

    def __str__(self):
        return f'{self.x}, {self.y}'


xs, ys, xt, yt = list(map(int, input().split()))
N = int(input())
circles = [(Vec(xs, ys), 0)] # pos, r
for _ in range(N):
    x, y, r = list(map(int, input().split()))
    circles.append((Vec(x, y), r))
circles.append((Vec(xt, yt), 0))

d = [[math.inf]*(N+2) for _ in range(N+2)]
for i in range(N+2):
    for j in range(i, N+2):
        tmp = max(0, circles[i][0].dist(circles[j][0])-(circles[i][1]+circles[j][1]))
        d[i][j] = tmp
        d[j][i] = tmp
q = [(0, 0)]
visited = [False]*(N+2)
ans = math.inf
while q:
    c, i = heapq.heappop(q)
    if visited[i]:
        continue
    if i == N+1:
        print(c)
        return
    visited[i] = True
    for j in range(N+2):
        if visited[j]:
            continue
        heapq.heappush(q, (c+d[i][j], j))

