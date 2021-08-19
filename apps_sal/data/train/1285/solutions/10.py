# cook your dish here
for i in range(int(input())):
    h = int(input())
    f = []
    su = []
    for j in range(0, h):
        f.append(list(map(int, input().split())))
    for k in range(0, h):
        s = 0
        s1 = 0
        for l in range(0, k + 1):
            s += f[l][h + l - k - 1]
            s1 += f[h + l - k - 1][l]
        su.append(s)
        su.append(s1)
    print(max(su))
