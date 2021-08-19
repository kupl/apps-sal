# coding: utf-8
# Your code here!

import sys
sys.setrecursionlimit(10**6)
readline = sys.stdin.readline  # 文字列入力のときは注意


r, c, n = [int(i) for i in readline().split()]
#xyxy = [[int(i) for i in readline().split()] for _ in range(n)]
# for i,(x1,y1,x2,y2) in enumerate(xyxy):


def addedge(x1, y1):
    if y1 == 0:
        edge.append((x1, i))
    elif x1 == r:
        edge.append((r + y1, i))
    elif y1 == c:
        edge.append((r + c + (r - x1), i))
    else:
        edge.append((r + c + r + (c - y1), i))
    return


edge = []
for i in range(n):
    x1, y1, x2, y2 = [int(i) for i in readline().split()]
    if (x1 not in (0, r) and y1 not in (0, c)) or (x2 not in (0, r) and y2 not in (0, c)):
        continue

    addedge(x1, y1)
    addedge(x2, y2)


edge.sort()
# print(edge)

ans = []
for d, i in edge:
    if ans and ans[-1] == i:
        ans.pop()
    else:
        ans.append(i)

if ans:
    print("NO")
else:
    print("YES")
