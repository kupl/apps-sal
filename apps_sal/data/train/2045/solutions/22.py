
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = list(map(int, input().split()))
conquerer = ['0'] * n
nextKnight = []
for i in range(n):
    nextKnight.append(i)

for _ in range(m):
    l, r, x = list(map(int, input().split()))
    pathList = []
    index = l - 1
    maxIndex = r
    while index < r:
        while index < n and nextKnight[index] != index:
            pathList.append(index)
            index = nextKnight[index]
        if index < r and index != x - 1:
            conquerer[index] = str(x)
            pathList.append(index)
        if index >= r:
            maxIndex = index
        index += 1
    for elem in pathList:
        if elem < x - 1:
            nextKnight[elem] = x - 1
        else:
            nextKnight[elem] = maxIndex

print(' '.join(conquerer))
