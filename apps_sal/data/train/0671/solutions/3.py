for _ in range(int(input())):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    f = list(map(int, input().split()))
    e, d = [], []
    for j in range(n):
        if f[j] == 1:
            e.append(j)
        else:
            d.append(j)
    an = False
    for j in e:
        if an:
            break
        for k in d:
            if p[j] + p[k] + m <= 100:
                an = True
                break
    if an:
        print("yes")
    else:
        print("no")
