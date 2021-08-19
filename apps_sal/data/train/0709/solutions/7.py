t = int(input())
for i in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    e = 1
    for j in l:
        if j % e == 0:
            e = j
        else:
            break
    l.reverse()
    f = 1
    for s in l:
        if s % f == 0:
            f = s
        else:
            break
    if e > f:
        f = e
    print(f)
