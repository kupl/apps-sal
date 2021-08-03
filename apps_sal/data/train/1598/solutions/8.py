from statistics import mean
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    d = {}
    for i in range(n):
        x, y, z = input().split()
        d[int(z)] = [x, y]
    avg = mean(d)
    a = []
    for i in d:
        if(i < avg):
            a.append(i)
    a.sort()
    for i in a:
        print(*d[i], i)
