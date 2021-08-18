t = int(input())
while(t > 0):
    n = int(input())
    b = [int(x) for x in input().split()]
    p = [float(x) for x in input().split()]
    s = [0] * (10)
    yet = 2
    mx = 0
    for i in range(n):
        st = bin(b[i])
        rng = len(st) - 2
        if(rng + 2 > yet):
            for ml in range(rng + 2 - yet):
                s.append(0)
        if(rng > mx):
            mx = rng
        for k in range(2, rng + 2):
            if(st[k] == '1'):
                s[rng - k + 1] = (s[rng - k + 1] * (1 - p[i])) + ((1 - s[rng - k + 1]) * (p[i]))
    mult = 1
    ans = 0
    for i in range(0, mx):
        ans += mult * s[i]
        mult = mult * 2
    print("%.16f" % ans)
    t -= 1
