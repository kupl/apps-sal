import copy


class seq:

    def __init__(self, l, c):
        self.length = l
        self.final_ctr = c


t = int(input())
for _ in range(t):
    n = int(input())
    d = {}
    c = {}
    prev = {}
    ctr = {}
    li = [int(i) for i in input().split(' ')]
    n = len(li)
    for i in li:
        ctr[i] = ctr.get(i, 0) + 1
    so = sorted(ctr)
    pp = -1
    for i in so:
        prev[i] = pp
        pp = i
    mx = 1
    for i in li:
        if i in d:
            if prev[i] in d and d[prev[i]][1].final_ctr == ctr[prev[i]]:
                if d[prev[i]][1].length > max(d[i][1].length, d[i][0].length):
                    d[i][0].length = d[prev[i]][1].length
                    d[i][0].final_ctr = 0
            if c.get(prev[i], 0) > max(d[i][1].length, d[i][0].length):
                d[i][0].length = c[prev[i]]
                d[i][0].final_ctr = 0
            d[i][1].final_ctr += 1
            d[i][1].length += 1
            d[i][0].final_ctr += 1
            d[i][0].length += 1
        else:
            d.setdefault(i, [seq(0, 0), seq(0, 0)])
            if prev[i] in d:
                if d[prev[i]][1].final_ctr == ctr[prev[i]]:
                    d[i][1] = seq(d[prev[i]][1].length + 1, 1)
                    d[i][0] = seq(d[prev[i]][1].length + 1, 1)
                    if c.get(prev[i], 0) > d[i][1].length:
                        d[i][1].length = c[prev[i]] + 1
                        d[i][0].length = c[prev[i]] + 1
                        d[i][1].final_ctr = 1
                        d[i][0].final_ctr = 1
                else:
                    d[i][1] = seq(c[prev[i]] + 1, 1)
                    d[i][0] = seq(c[prev[i]] + 1, 1)
            else:
                d[i][1] = seq(1, 1)
        mx = max(mx, d[i][1].length, d[i][0].length)
        c[i] = c.get(i, 0) + 1
    print(n - mx)
'\n1\n17\n0 0 0 0 1 1 1 0 0 0 0 1 1 1 2 2 2\n4 and 6\n'
