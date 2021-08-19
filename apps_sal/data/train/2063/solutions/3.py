(n, m) = map(int, input().split())
q = [[] for i in range(n + 1)]
(r, s) = ([0] * (m + 1), 0)
for i in range(1, n + 1):
    t = list(map(int, input().split()))
    if t[0]:
        t = t[1:]
        d = set([r[j] for j in t])
        if 0 in d:
            d.remove(0)
        if len(d):
            for j in d:
                for k in q[j]:
                    r[k] = i
                q[i].extend(q[j])
                q[j] = []
            t = [j for j in t if r[j] == 0]
            for k in t:
                r[k] = i
            q[i].extend(t)
        else:
            for k in t:
                r[k] = i
            q[i] = t
    else:
        s += 1
print(s + max(sum((len(i) > 0 for i in q)) - 1, 0))
