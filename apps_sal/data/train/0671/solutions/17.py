# cook your dish here
for T in range(int(input())):
    n, s = list(map(int, input().split()))
    p = list(map(int, input().split()))
    ls = list(map(int, input().split()))
    d = []
    f = []
    flag1 = 0
    for i in range(n):
        if ls[i] == 0:
            d.append(p[i])
        else:
            f.append(p[i])

    for j in range(len(d)):
        for k in range(len(f)):
            if (100 - s) >= (d[j] + f[k]):
                flag1 = 1
                break
    if flag1 == 1:
        print("yes")
    else:
        print("no")
