t = int(input())
for i in range(t):
    n, k = list(map(int, input().split()))
    arr = [int(x) for x in input().split()]
    d = {}
    for i in arr:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    l = []
    for i in list(d.keys()):
        if d[i] > k:
            l.append(i)
    l.sort()
    print(*l)
