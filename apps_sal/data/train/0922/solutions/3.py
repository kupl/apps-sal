t = int(input())
while t:
    m, n = map(int, input().split())
    arr = [int(i) for i in input().split()]
    brr = [int(i) for i in input().split()]
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in brr:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    z = []
    for i in d:
        if d[i] == 1:
            z.append(i)
    z.sort()
    print(*z)
    t -= 1
