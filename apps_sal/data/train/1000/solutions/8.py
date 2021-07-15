from math import ceil
g = int(input())
for i in range(g):
    a = int(input())
    l = list(map(int,input().split()))
    print(ceil(a/min(l)))
