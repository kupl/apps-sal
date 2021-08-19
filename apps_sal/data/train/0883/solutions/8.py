t = int(input())
for o in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(set(a))
    b.sort()
    if n == 1:
        print(-1)
        continue
    if len(b) > 2:
        print(-1)
        continue
    if len(b) == 1:
        if b[0] == n - 1:
            print(0)
        elif b[0] == 0:
            print(n)
        else:
            print(-1)
        continue
    pa = a.count(b[0])
    fa = a.count(b[1])
    if pa != b[1] or b[1] - b[0] != 1:
        print(-1)
        continue
    print(n - pa)
