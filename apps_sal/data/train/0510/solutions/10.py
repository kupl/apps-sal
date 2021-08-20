from bisect import bisect_left as g, insort as h
f = input
d = {chr(97 + i): [] for i in range(26)}
f()
(s, i) = (list(f()), 0)
for c in s:
    d[c] += [i]
    i += 1
for _ in range(int(f())):
    (a, b, c) = f().split()
    b = int(b) - 1
    if a > '1':
        print(sum((1 for l in d.values() if g(l, b) < len(l) and l[g(l, b)] < int(c))))
    elif s[b] != c:
        l = d[s[b]]
        l.pop(g(l, b))
        s[b] = c
        h(d[c], b)
