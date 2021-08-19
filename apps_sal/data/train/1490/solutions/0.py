from math import ceil
t = int(input())
for i in range(t):
    p = int(input())
    l = list(map(int, input().split()))
    maxx = 1
    for i in range(len(l)):
        maxx = max(maxx, l.count(l[i]))
    if maxx * 2 > p:
        print(maxx)
    else:
        q = p - maxx * 2
        maxx += ceil(q / 2)
        print(maxx)
