t = int(input())
for i in range(0, t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    p = set(l)
    pp = list(p)
    maxx = pp[n - 1] * pp[n - 2]
    minn = pp[0] * pp[1]
    print(maxx, minn)
