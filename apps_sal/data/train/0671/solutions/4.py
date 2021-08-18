for i in range(int(input())):
    n, s = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    f, d = [], []
    for j in range(n):
        if c[j] == 1:
            f.append(j)
        else:
            d.append(j)
    ans = False
    for j in f:
        if ans:
            break
        for k in d:
            if p[j] + p[k] + s <= 100:
                ans = True
                break
    if ans:
        print("yes")
    else:
        print("no")
