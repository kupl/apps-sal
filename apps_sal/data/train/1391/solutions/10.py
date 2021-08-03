t = int(input())
while(t > 0):
    n, k = map(int, input().split())
    l = []
    c = 0
    for i in range(n):
        a, d, x = map(int, input().split())
        l.append((a, d, x))
    l.sort(key=lambda x: x[1])
    d = {}
    for i in l:
        if(i[2] not in d):
            d[i[2]] = i[1]
            c += 1
        else:
            if(i[0] >= d[i[2]]):
                c += 1
                d[i[2]] = i[1]
    print(c)
    t -= 1
