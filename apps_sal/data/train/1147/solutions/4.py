t = int(input())
for j in range(t):
    c = 0
    f = 1
    k = 0
    n = int(input())
    s = input()
    di = {}
    for i in range(n):
        if s[i] in di.keys():
            di[s[i]] = di[s[i]] + 1
        else:
            di[s[i]] = 1
    for i in di.keys():
        if di[i] == 1 and f:
            f = 0
        elif di[i] % 2 == 1:
            k = 1
            c = c + 1
    if f and k:
        c = c - 1
    print(c)
