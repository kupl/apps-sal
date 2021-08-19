t = int(input())
for z in range(t):
    n = int(input())
    l = map(int, input().split())
    tg = 0
    for i in sorted(l):
        if i <= tg:
            tg += 1
    print(tg)
