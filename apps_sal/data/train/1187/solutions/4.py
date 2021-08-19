# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    t = 1
    tt = []
    while t <= n:
        t *= k
        v = n // t
        v -= v // k
        if tt:
            tt[-1] -= v
        tt.append(v)
    res, cnt = 0, 1
    for i, v in enumerate(tt):
        res += ((i + 2) // 2) * v
        if i & 1 == 0:
            cnt = cnt * pow((i + 2) // 2 + 1, v, 998244353) % 998244353
        #print("->", res, cnt)
    print(n - res, cnt)
