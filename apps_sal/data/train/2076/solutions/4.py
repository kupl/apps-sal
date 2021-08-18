
from math import acos


def check(i, j, k):
    num = 0
    for l in range(0, 5):
        num += (points[j][l] - points[i][l]) * (points[k][l] - points[i][l])
    return num > 0


n = int(input())
points = [[-1, -1, -1, -1, -1]]
ans = []
for _ in range(0, n):
    pts = [int(i) for i in input().split()]
    points.append(pts)
for i in range(1, n + 1):
    put = True
    for j in range(1, n + 1):
        if j != i and put:
            for k in range(1, n + 1):
                if j != k:
                    if check(i, j, k):
                        put = False
                        break
            if not put:
                break
    if put:
        ans.append(i)
print(len(ans))
print(*ans)


"""

6
0 0 0 0 0
1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1


3
0 0 1 2 0
0 0 9 2 0
0 0 5 9 0


"""
