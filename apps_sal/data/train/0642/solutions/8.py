import sys


def fn(a, mid, d):
    b = []
    for i in range(n):
        b.append(a[i] + d)
    t = 0.0
    for i in range(n):
        if(a[i] <= t and t <= b[i]):
            t += mid
        elif(t <= b[i]):
            t = (a[i] + mid)
        else:
            return False
    return True


t = int(input())
while t:
    n, d = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    c.sort()
    l = 0
    r = max(c) + d
    for i in range(100):
        mid = (l + r) / 2
        if(fn(c, mid, d)):
            l = mid
        else:
            r = mid
    print(mid)
    t -= 1
