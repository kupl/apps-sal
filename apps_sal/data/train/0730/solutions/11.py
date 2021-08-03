for _ in range(int(input())):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    p = list()
    for b in a:
        ans = 0
        d = [0] * 6
        for i in b[1:]:
            d[i - 1] += 1
        d = sorted(d)
        ans += d[0] * 4
        if d[1] - d[0] > 0:
            ans += (d[1] - d[0]) * 2
        if d[2] - d[1] - d[0] > 0:
            ans += (d[2] - d[1] - d[0])
        ans += b[0]
        p.append(ans)
    s = sorted(p)
    if s[n - 1] == s[n - 2]:
        print("tie")
    elif p[0] == max(p):
        print("chef")
    else:
        print(p.index(max(p)) + 1)
