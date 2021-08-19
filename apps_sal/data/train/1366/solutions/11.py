import math


def solve():
    n = int(input())
    l = list(map(int, input().split()))
    pos = n
    for i in range(n):
        if l[i] != 0:
            pos = i
            break
    c = 0
    for j in l[::-1]:
        if j == 0:
            c += 1
        else:
            break
    if n - c - pos > 0:
        print(n - c - pos)
    else:
        print(1)


t = input()
t = int(t)
while t != 0:
    t = t - 1
    solve()
