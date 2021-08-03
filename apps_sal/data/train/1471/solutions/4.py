#!/bin/python
from heapq import heappush, heappop
import sys


def getDistancesBot1(a, n, m, mat, k):
    for i in range(n):
        mat.append([20000 for j in range(m)])
    heap = []
    mat[0][0] = 0
    heappush(heap, (0, 0, 0))
    while len(heap) != 0:
        item = heappop(heap)
        top = max(0, item[2] - k)
        bottom = min(n - 1, item[2] + k)
        for y in range(top, bottom + 1):
            c = k - abs(y - item[2])
            left = max(0, item[1] - c)
            right = min(m - 1, item[1] + c)
            for x in range(left, right + 1):
                if a[y][x] == 0:
                    if mat[y][x] > (item[0] + 1):
                        mat[y][x] = item[0] + 1
                        heappush(heap, (mat[y][x], x, y))


def getDistancesBot2(a, n, m, mat, k):
    for i in range(n):
        mat.append([20000 for j in range(m)])
    heap = []
    mat[0][m - 1] = 0
    heappush(heap, (0, m - 1, 0))
    while len(heap) != 0:
        item = heappop(heap)
        top = max(0, item[2] - k)
        bottom = min(n - 1, item[2] + k)
        for y in range(top, bottom + 1):
            c = k - abs(y - item[2])
            left = max(0, item[1] - c)
            right = min(m - 1, item[1] + c)
            for x in range(left, right + 1):
                if a[y][x] == 0:
                    if mat[y][x] > (item[0] + 1):
                        mat[y][x] = item[0] + 1
                        heappush(heap, (mat[y][x], x, y))


t = int(input().strip())
for i in range(t):
    [n, m, k1, k2] = list(map(int, input().strip().split(' ')))
    arr = []
    for j in range(n):
        arr.append(list(map(int, input().strip().split(' '))))
    mat1 = []
    mat2 = []
    getDistancesBot1(arr, n, m, mat1, k1)
    getDistancesBot2(arr, n, m, mat2, k2)
    minSteps = 2000
    for x in range(n):
        for y in range(m):
            minSteps = min(minSteps, max(mat1[x][y], mat2[x][y]))
    if minSteps == 2000:
        print(-1)
    else:
        print(minSteps)
