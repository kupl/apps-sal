T = int(input())
for j in range(T):
    s = input()
    r = input()
    t = []
    c = None
    (n, k) = (0, 0)
    for i in range(len(s)):
        if r[i] != s[i]:
            n += 1
            if c:
                t.append(c)
                k += 1
            c = 0
        elif c != None:
            c += 1
    k += 1
    t.sort()
    m = k * n
    for (i, j) in enumerate(t):
        k -= 1
        n += j
        m = min(m, k * n)
    print(m)
