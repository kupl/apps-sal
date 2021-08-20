t = int(input())
for _ in range(t):
    n = int(input())
    c = []
    for _ in range(0, n):
        c.append(list(map(int, input().split())))
    m = []

    def newset(c):
        for i in set(c[1:]):
            c.remove(i)
        return c

    def check(c):
        s = len(set(c[1:]))
        if s < len(c[1:]):
            check(newset(c))
        if s == 4:
            c[0] += 1
        elif s == 5:
            c[0] += 2
        elif s == 6:
            c[0] += 4
        return c[0]
    for i in c:
        m.append(check(i))
    if m.count(max(m)) > 1:
        print('tie')
    elif max(m) == m[0]:
        print('chef')
    else:
        print(m.index(max(m)) + 1)
