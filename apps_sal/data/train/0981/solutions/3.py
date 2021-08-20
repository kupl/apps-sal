import sys
t = int(input())
while t:
    t = t - 1
    min = 1000000000 + 100
    n = int(input())
    d = []
    for i in input().split():
        d.append(int(i))
    d = sorted(d)
    for i in range(1, n):
        if d[i] - d[i - 1] < min:
            min = d[i] - d[i - 1]
            if min == 0:
                break
    print(min)
