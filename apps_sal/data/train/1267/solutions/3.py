n, m, k = list(map(int, input().split()))
cost = []
for i in range(m):
    cost.append(list(map(int, input().split())))

if (m <= 5):
    c = 97
    s = []
    for i in range(n):
        s.append(chr(c + i))
    l = []

    def gen(x, c, ln):
        # print x, c, ln
        if (ln >= m):
            l.append((c, x))
        else:
            for i in range(n):
                xt = x + s[i]
                ct = c + cost[ln][ord(s[i]) - 97]
                gen(xt, ct, ln + 1)
    gen('', 0, 0)
    l.sort(reverse=True)
    print(l[k - 1][1])
