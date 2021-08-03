for i in range(int(input())):
    n = int(input())
    c = list(map(int, input().split()))
    d = {}
    d[0] = -1
    parity = 0
    ans = 0
    for i in range(n):
        parity ^= 1 << (c[i] - 1)
        for t in range(30):
            x = parity ^ (1 << t)
            if(x in d.keys()):
                ans = max(ans, i - d[x])
        if parity not in d.keys():
            d[parity] = i
    print(ans // 2)
