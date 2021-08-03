t = int(input())
for x in range(0, t):
    r, g, b, m = map(int, input().split())
    a = []
    c = []
    for i in range(0, 3):
        v = list(map(int, input().split()))
        v.sort(reverse=True)
        a.append(v)
    a.sort()
    for i in range(0, m):
        l = len(a[2])
        j = 0
        while(j < l):
            a[2][j] = int(a[2][j] / 2)
            j += 1
        a.sort()
    for x in a:
        c.append(max(x))
    print(max(c))
