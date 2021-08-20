from sys import *
input = stdin.readline
n = int(input())
l = list(map(int, input().split()))
l.sort()
p = int(input())
c = 0
i = 0
while i < n:
    if l[i] <= p:
        c = c + 1
        p = p - l[i]
        i = i + 1
    elif c > 0:
        if p + l[n - 1] >= l[i]:
            p = p + l[n - 1] - l[i]
            n = n - 1
            i = i + 1
    else:
        break
print(c)
